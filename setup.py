from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ZobisFavy/mylibrary',
    author='Okafor Favour',
    author_email='zoba.nuela@gmail.com'
)
   