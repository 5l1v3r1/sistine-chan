import os
from setuptools import setup, find_packages


def install_requires():
    filepath = os.path.dirname(__file__)
    with open(os.path.join(filepath, 'requirements.txt')) as fobj:
        return fobj.read().splitlines()

setup(
    zip_safe = False,
    name = "Sistine-chan",
    version = "0.1",
    packages = find_packages(),
    author='x0lzs3c',
    author_email='xolzsec@protonmail.com',
    url='update...',
    description='Sistine-chan feat Facebook Messenger bot',
    entry_points = {
        'console_scripts': [
                'sischan = sischan.cmds.main:main',
                'sischan_primitive = sischan.cmds.primitive_worker:main',
                'sischan_scheduler = sischan.cmds.scheduler_worker:main'
            ]
    },
    install_requires = install_requires(),
    classifiers=[
        'Programming Language :: Python'
    ]
)
