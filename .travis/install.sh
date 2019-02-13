#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update
    brew upgrade python
elif [[ -z "$CONAN_DOCKER_IMAGE" ]]; then
    sudo dpkg --add-architecture i386
    sudo apt update
    sudo apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386 multiarch-support
fi

pip3 install conan conan_package_tools --upgrade

conan user
