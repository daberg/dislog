from setuptools import setup


setup(
    author='daberg',
    description="Implementation of discrete logarithm algorithms",
    install_requires=['sympy>=1.4'],
    name='dislog',
    packages=['dislog', 'dislog.util'],
    version='1.0'
)
