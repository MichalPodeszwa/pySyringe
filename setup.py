import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


setup(
    name='pySyringe',
    version='1.0',
    description='Pythonic dependency injection container',
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
    author='Michał Podeszwa',
    author_email='michal.podeszwa@gmail.com',
    url='https://github.com/michalpodeszwa/pySyringe',
    keywords='di ioc container dependency injection',
    packages=['pysyringe'],
    include_package_data=True,
    zip_safe=False,
)
