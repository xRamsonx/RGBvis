#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:23:57 2023

@author: kai
"""
from setuptools import setup

setup(
    name='rgbvis',
    version='0.0.1',    
    description='A ',
    url='https://github.com/xRamsonx/RGBvis',
    author='Kai Arnold',
    author_email='kai.arnold@design4webs.de',
    license='MIT License',
    packages=['rgbvis'],
    include_package_data=True,
    install_requires=['plotly',
                      'numpy',
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: MIT License',  
        'Operating System :: POSIX :: Linux/Windows',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)