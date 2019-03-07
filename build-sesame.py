#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sesame import build_template_default

def main():
    builder = build_template_default.get_builder(build_types=['RelWithDebInfo'])
    builder.run()

if __name__ == '__main__':
    main()
