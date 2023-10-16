from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='howlong',
    version='0.0.1',
    license='MIT License',
    author='Gabriel Carvalho',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='contatotrabalhogab@gmail.com',
    keywords='time execution python',
    packages=['./'],
    install_requires=['time'],)