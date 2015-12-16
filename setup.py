from setuptools import setup


setup(
    name='pySyringe',
    version='1.2.0',
    description='Pythonic dependency injection container',
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
