from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "hello"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "libhello/1.0.0"

    def build(self):
        print("OWWW")
        cmake = CMake(self)
        cmake.configure(source_folder="")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
