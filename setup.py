#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='plotgen',
    version='0.4.1',
    scripts=['plotgen'],
    author="Björn Gottschall",
    author_email="github.mail@bgottschall.de",
    description="A plotly plotting script generator and data parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bgottschall/plotgen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'plotly>=5.1.0',
        'numpy>=1.21.1',
        'pandas>=1.3.1',
        'xopen>=1.1.0',
        'kaleido>=0.2.1',
        'seaborn>=0.11.1'
    ],
    python_requires=">=3.6"
)
