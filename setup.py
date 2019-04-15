from setuptools import setup


setup(
    name='tsdcli',
    packages=['tsdcli'],
    version='0.0.2',
    install_requires=[
        'click'
    ],
    entry_points={'console_scripts': ['tsdcli=tsdcli.cli:cli']},
)
