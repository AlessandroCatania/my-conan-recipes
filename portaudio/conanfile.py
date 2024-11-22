from conan import ConanFile
from conan.tools.files import get
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps
import os

class PortAudioConan(ConanFile):
    name = "portaudio"
    version = "19.7.0"
    license = "MIT"
    url = "https://github.com/PortAudio/portaudio"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*"

    def source(self):
        get(self, 
            url=f"https://github.com/PortAudio/portaudio/archive/refs/tags/v{self.version}.tar.gz",
            destination=self.source_folder,
            strip_root=True)

    def layout(self):
        self.folders.source = "src"
        self.folders.build = "build"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["portaudio"]
        self.cpp_info.includedirs = [os.path.join(self.package_folder, "include")]
        self.cpp_info.libdirs = [os.path.join(self.package_folder, "lib")]
