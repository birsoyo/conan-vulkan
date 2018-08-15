# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class VulkanConan(ConanFile):
    name = 'vulkan'
    version = '1.1.82.0'
    description = '<Description of Vulkan here>.'
    url = 'https://github.com/birsoyo/conan-vulkan'
    homepage = 'https://github.com/original_author/original_lib'
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = '<Indicates License type of the packaged library>'

    # Packages the license for the conanfile.py
    exports = ['LICENSE.md']

    settings = 'os', 'arch'

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = 'source_subfolder'
    build_subfolder = 'build_subfolder'

    def build(self):
        prefix_url = f'https://sdk.lunarg.com/sdk/download/{self.version}'
        win_url = f'{prefix_url}/windows/VulkanSDK-{self.version}-Installer.exe'
        mac_url = f'{prefix_url}/mac/vulkansdk-macos-{self.version}.tar.gz'
        lin_url = f'{prefix_url}/linux/vulkansdk-linux-x86_64-{self.version}.tar.gz'

        if self.settings.os == 'Windows':
            tools.download(win_url, 'vulkan-installer.exe')
            self.run('vulkan-installer.exe /S')
        else:
            tools.get(url, keep_permissions=True)

    def package(self):
        self.copy(pattern='LICENSE', dst='licenses', src=self.source_subfolder)

        if self.settings.os == 'Windows':
            location = f'C:\\VulkanSDK\\{self.version}'
            inc_folder = os.path.join(location, 'Include')
            if self.settings.arch == 'x86':
                lib_folder = os.path.join(location, 'Lib32')
            elif self.settings.arch == 'x86_64':
                lib_folder = os.path.join(location, 'Lib')

        self.copy(pattern='*', dst='include', src=inc_folder)
        self.copy(pattern='*', dst='lib', src=lib_folder)

    def package_info(self):
        self.cpp_info.libs = ['vulkan-1']
