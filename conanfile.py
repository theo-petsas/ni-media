import os
from conans import ConanFile, tools, CMake

class NiMediaConan(ConanFile):
    name = "ni-media"
    topics = ("media", "audio decoding")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["NIMEDIA_TESTS"] = "OFF"
        cmake.definitions["NIMEDIA_ENABLE_FLAC_DECODING"] = "OFF"
        cmake.definitions["NIMEDIA_ENABLE_OGG_DECODING"] = "OFF"
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs = ["audiostream", "pcm"]
