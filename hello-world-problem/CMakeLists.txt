# stop if cmake version is below 3.0
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

# project name and enable C++ support
project(helloworld LANGUAGES CXX)


# require C++14
set(CMAKE_CXX_STANDARD 14)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


#define the executable
add_executable(helloworld src/main.cpp)

target_link_libraries(helloworld ${CONAN_LIBS})
