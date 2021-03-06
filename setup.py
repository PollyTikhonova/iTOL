#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

VERSION = '1.0'

wd = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(wd, 'README.rst')) as f:
        return f.read()


setup(name='iTOL',
      version=VERSION,
      description='Python API for phylogenetic tree visualization in Interactive Tree of Life (http://iTOL.embl.de)',
      long_description=readme(),
      url='https://github.com/iBiology/iTOL',
      author='FEI YUAN',
      author_email='yuanfeifuzzy@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests>=2.12.4'],
      entry_points={
          'console_scripts': ['itol=iTOL.iTOL:main']},
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Production/Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          ],
      keywords='phylogeny tree visualization biology bioinformatics'
      )

if __name__ == '__main__':
    pass
