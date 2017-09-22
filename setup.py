#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='drawingapp',
    version='0.0.1',
    description='An app for drawing stuff',
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
