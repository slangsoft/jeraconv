from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jeraconv',
    version='0.2.1',
    packages=['tests', 'jeraconv'],
    package_data={'jeraconv': ['data/*.json']},
    url='https://github.com/slangsoft/jeraconv',
    license='MIT',
    author='slangsoft',
    author_email='slangsoft@gmail.com',
    description='jeraconv (Japanese Era Name Converter) is a converter that converts Japanese eras to West calendar.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='jeraconv japanese era',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
)
