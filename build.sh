#!/bin/bash

# Debug Mode
set -ex
BUILD_DIR="cmake_build"

# PIPELINE: configure,build,package
cmake -B ${BUILD_DIR} -DCMAKE_BUILD_TYPE=Debug
cmake --build ${BUILD_DIR}
cmake --build ${BUILD_DIR} --target package

# localhost, mkdir build && cd build
# cmake ..
# make
# make install
# make package; cpack
