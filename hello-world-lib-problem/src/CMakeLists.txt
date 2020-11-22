# stop if cmake version is below 3.0
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

# project name and enable C++ support
project(hello_library LANGUAGES CXX)

# Setup conan and include everything.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# require C++14
set(CMAKE_CXX_STANDARD 14)

file(GLOB PROJECT_SOURCE "*.cpp")


#Generate the shared library from the sources
add_library(hello SHARED ${PROJECT_SOURCE})
