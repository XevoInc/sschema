#!/usr/bin/python3

import os
import setuptools


setuptools.setup(
    name='sschema',
    version='0.0.1',
    description='A library and prebuilt schemas for handling edge sensor data',
    author='Martin Kelly',
    author_email='mkelly@xevo.com',
    license='Apache',
    python_requires='>=3',
    install_requires=['PyYAML>=3.12'],
    packages=['sschema',
              'sschema.formatchecker',
              'sschema.handler'],
    package_data={'sschema': ['schema/*']},
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Natural Language :: English',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3 :: Only',
                 'Topic :: Software Development :: Embedded Systems',
                 'Topic :: Software Development :: Testing :: Acceptance',
                 ],
)
