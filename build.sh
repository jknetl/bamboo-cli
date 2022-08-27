#!/bin/bash

# build pip
python setup.py sdist bdist_wheel

# build distribution
pyinstaller src/main.py
