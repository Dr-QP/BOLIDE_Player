#!/usr/bin/env python3

from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy
import os


class ArduinoPackager(ConanMultiPackager):
    def addArduino(self, options={}):
        if os.getenv("CONAN_DOCKER_IMAGE") or os.getenv("CONAN_USE_DOCKER"):
            # Arduino builds fail if conan was lunched with docker image specification
            return None

        self.add(settings={
            "os": "Arduino",
            "os.board": "XYZrobot1280",
            "compiler": "gcc",
            "compiler.version": "5.4",
            "compiler.libcxx": "libstdc++11",
            "arch": "avr"
        }, options=options, env_vars={
            "CC": "gcc"
        }, build_requires={
            "*": ["arduino-toolchain/1.8.8@conan/testing"]
        })


if __name__ == "__main__":
    builder = ArduinoPackager(build_policy="outdated",
        upload="https://api.bintray.com/conan/anton-matosov/general",
        login_username="anton-matosov",
        username="conan",
        channel="testing",
        stable_branch_pattern="release/*",
    )

    if os.getenv("DRQP_NATIVE_BUILD") == "1":
        builder.add()

    if os.getenv("DRQP_ARDUINO_BUILD") == "1":
        builder.addArduino()

    if os_info.is_linux:
        filtered_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            filtered_builds.append(
                [settings, options, env_vars, build_requires])
            new_options = copy.copy(options)
            new_options["arduino-sdk:host_os"] = "linux32"
            filtered_builds.append(
                [settings, new_options, env_vars, build_requires])
        builder.builds = filtered_builds

    builder.run()
