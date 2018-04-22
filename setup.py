#!/usr/bin/python

# Copyright (c) 2011 Fu Haiping.
# See LICENSE for details.

import sys
from distutils.core import setup, Extension

extra_compile_args = ['-Wall', '-pedantic', 
'-shared', '-std=gnu99', '-fPIC', '-g', '-D_GNU_SOURCE']
extra_link_args = ['-L/usr/local/lib/', '-static']

setup(
        name = 'rdb',
        version = '0.1',
        maintainer = 'watson.jiang',
        maintainer_email = 'watson.jiang@gmail.com',
        url = '',

        classifiers = [
                'Development Status :: 4 - Beta',
                'Environment :: Other Environment',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                'Operating System :: POSIX',
                'Programming Language :: C',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3.0',
                'Topic :: Database',
                'Topic :: Software Development :: Libraries'
        ],

        description = 'Python bindings for redis database library using c api',
        # long_description =

        packages = ['rdb'],
        package_dir = {'rdb': ''},

        ext_modules = [
                Extension('rdb',
                        sources = [
                                # python stuff
                                'src/initmodule.c',
                        ],
                        extra_compile_args = extra_compile_args,
                        extra_link_args = extra_link_args
                )
        ]
)


