from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages


setup(
    name='echoapp',
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
    entry_points="""\
    [console_scripts]
    echoapp = echoapp.__main__:main
    """
)
