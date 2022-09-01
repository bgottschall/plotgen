from setuptools import setup
import os

setup(
   name='plotgen',
   scripts=['plotgen'],
   version='0.6.0',
   description=('A plotly plotting script generator and data parser'),
   long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
   author='Björn Gottschall',
   author_email='info@bgottschall.de',
   url='https://github.com/bgottschall/plotgen',
   license='MIT',
   license_files=['LICENSE'],
   classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ],
   keywords='tables graph plot parser',
   python_requires='>=3.7',
   install_requires=[
       'argcomplete>=1.12.3', 
       'plotly>=5.1.0', 
       'numpy>=1.21.1', 
       'pandas>=1.3.1', 
       'xopen>=1.1.0', 
       'kaleido>=0.2.1', 
       'seaborn>=0.11.1'
       ],
)   
