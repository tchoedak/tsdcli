from setuptools import setup


setup(
    name='tsdcli',
    packages=['tsdcli'],
    version='0.0.1',
    install_requires=[
        'click'
    ],
    entry_points={'console_scripts': ['tsdcli=tsdcli.cli:cli']},
)
