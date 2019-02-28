from conans import ConanFile, CMake, tools
import os


class BolidePlayerConan(ConanFile):
    name = "BOLIDE_Player"
    version = "develop"
    license = "LGPL"
    url = "https://github.com/Dr-QP/BOLIDE_Player"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "*", "!build/*", "!test_package/*", "!.travis*", "!.vs*"

    def configure(self):
        if self.settings.os == "Arduino":
            del self.options.shared

    def requirements(self):
        self.requires(self.drQpRequire("HAL/develop"))
        if self.settings.os == "Arduino":
            self.requires(self.drQpRequire("arduino-stl/1.0.0"))

    def build_requirements(self):
        if self.settings.os == "Arduino":
            self.build_requires(self.drQpRequire("arduino-board-xyzrobot/1.0.0"))
            self.build_requires(self.drQpRequire("arduino-toolchain/[~=1.8]"))

    def drQpRequire(self, packageName):
        return "%s@%s/%s" % (packageName, self.user, self.channel)
        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
        self.cpp_info.libs = ["BOLIDE_Player"]
