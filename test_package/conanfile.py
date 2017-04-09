import conans
import os


channel = os.getenv('CONAN_CHANNEL', 'wat')
username = os.getenv('CONAN_USERNAME', 'cblp')


class ConanFile(conans.ConanFile):
    settings = {'os', 'compiler', 'build_type', 'arch'}
    requires = 'SwarmPlusPlus/0.0@{}/{}'.format(username, channel)
    generators = 'cmake'

    def build(self):
        cmake = conans.CMake(self.settings)
        # Current dir is 'test_package/build/<build_id>'
        # and CMakeLists.txt is in 'test_package'
        cmake.configure(
            self, source_dir=self.conanfile_directory, build_dir='./'
        )
        cmake.build(self)

    def imports(self):
        self.copy('*.dll', 'bin', 'bin')
        self.copy('*.dylib', 'bin', 'bin')

    def test(self):
        self.run(os.path.join('bin', 'test'))
