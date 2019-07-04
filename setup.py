# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:09:44 2019

@author: jltsa
"""

from setuptools import find_packages, setup

setup(
      name='flaskr',
      version='1.0.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
              'flask',
              ],
        
      )