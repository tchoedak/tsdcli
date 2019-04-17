import os
from setuptools import setup


setup(
    name='tsdcli',
    packages=['tsdcli'],
    version='0.0.3',
    description='Time Saving Data CLI',
    author='tchoedak',
    author_email='tchoedak@gmail.com',
    url='https://tsdcli.tech',
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': ['tsdcli=tsdcli.tsdcli.cli:cli'],
    },
)
