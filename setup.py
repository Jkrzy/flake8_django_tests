#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'flake8'
]

setup_requirements = [
    'flake8'
]

test_requirements = []

setup(
    name='flake8_django_tests',
    version='0.1.0',
    description="Flake8 plugin checking Django test doctstrings for style compliance",
    long_description=readme + '\n\n' + history,
    author="Joe Krzystan",
    author_email='joe@jkrzy.com',
    url='https://github.com/jkrzy/flake8_django_tests',
    packages=find_packages(include=['flake8_django_tests']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flake8_django_tests, flake8, Django',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
        entry_points={
        'flake8.extension': [
            'DJT = flake8_django_tests:DjangoTestDocStrings',
        ],
    },
)
