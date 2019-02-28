from conans import ConanFile, CMake
import os

class BolideplayerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        if self.settings.os == "Arduino":
            # Tests need to be uploaded to Arduino to run. So do nothing for now
            pass
        else:
            self.run(".%sexample" % os.sep)
