from conans import ConanFile, CMake, tools
import os


class BolideplayerConan(ConanFile):
    name = "BOLIDE_Player"
    version = "develop"
    license = "LGPL"
    url = "https://github.com/Dr-QP/BOLIDE_Player"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "*", "!build/*", "!test_package/*"

    def configure(self):
        self.requires(self.drQpRequire("HAL"))

    def drQpRequire(self, packageName):
        return "%s/develop@%s/%s" % (packageName, self.user, self.channel)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=".")
        self.copy("*BOLIDE_Player.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
        self.cpp_info.libs = ["BOLIDE_Player"]
