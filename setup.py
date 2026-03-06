#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='CryptoPlus',
      version='1.0.1',
      description='PyCrypto Cipher extension',
      author='Christophe Oosterlynck',
      author_email='tiftof@gmail.com',
      packages = find_packages('src'),
      install_requires = ['pycryptodome', 'packaging>=20.0'],
      package_dir={'': 'src'}
     )

