# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools, RunEnvironment

class VulkanTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            with tools.environment_append(RunEnvironment(self).vars), tools.chdir('bin'):
                self.run(f'.{os.sep}test_package')
