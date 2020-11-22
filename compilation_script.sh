#!/bin/sh

conan create hello-world-lib-problem

cd hello-world-problem && mkdir build && cd build 

conan install .. && cmake .. && make

pwd
