import os
from conans import ConanFile, tools, CMake


def get_version():
    if os.environ.get("CONAN_PACKAGE_VERSION", None):
        return f"{os.environ['CONAN_PACKAGE_VERSION']}"
    return "0.0.0"


class NiMediaConan(ConanFile):
    name = "effects"
    version = get_version()
    topics = ("media", "audio decoding")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False, "boost:without_test": True}
    requires = ["gtest/1.10.0", "boost/1.80.0"]
    generators = "cmake"
    exports_sources = "*", "!.ccls-cache/*", "!build/*", "!compile_commands.json"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include", keep_path=True)

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["audiostream", "pcm"]
