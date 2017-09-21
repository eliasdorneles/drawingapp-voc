#!/usr/bin/env python
import io
from setuptools import setup, find_packages

with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='drawingapp',
    version='0.0.1',
    description='An app for drawing stuff',
    long_description=long_description,
    author='Elias Dorneles',
    author_email='eliasdorneles@gmail.com',
    license='BSD license',
    packages=find_packages(
        exclude=['docs', 'tests', 'android']
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD license',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'Drawing App',
            'bundle': 'org.pybee.elias'
        },
    }
)
