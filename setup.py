from setuptools import setup
import os
import re

setup(
   name='plotgen',
   scripts=['plotgen'],
   version=re.search('__version__.+\n', open(os.path.join(os.path.dirname(__file__), 'plotgen')).read()).group(0).split('\'')[1],
   description=('A plotly plotting script generator and data parser'),
   long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
   long_description_content_type='text/markdown',
   author='Björn Gottschall',
   author_email='info@gottschall.no',
   url='https://github.com/bgottschall/plotgen',
   license='MIT',
   license_files=['LICENSE'],
   classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ],
   keywords='tables graph plot parser plotly',
   python_requires='>=3.9',
   install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines(),
)
