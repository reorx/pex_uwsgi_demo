#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


package_name = 'pex_uwsgi_demo'


def get_requires():
    try:
        with open('requirements.txt', 'r') as f:
            requires = [i for i in map(lambda x: x.strip(), f.readlines()) if i]
        return requires
    except IOError:
        return []


def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''


pkgs = find_packages()
print 'packages:', pkgs
requires = get_requires()
print 'requires:', requires


setup(
    # license='License :: OSI Approved :: MIT License',
    name=package_name,
    version='0.1.0',
    author='',
    author_email='',
    description='',
    url='',
    long_description=get_long_description(),
    # packages=[
    #     'project_sketch',
    #     'project_sketch/_module'
    # ],
    # Or use (make sure find_packages is imported from setuptools):
    packages=pkgs,
    # Or if it's a single file package
    #py_modules=[package_name],
    install_requires=requires,
    # package_data={}
    # entry_points={'console_scripts': ['foo = package.module:main_func']}
)
