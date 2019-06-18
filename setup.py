from setuptools import setup

setup(
    name='jeraconv',
    version='0.1.0',
    packages=['tests', 'jeraconv'],
    package_data={'jeraconv': ['data/*.json']},
    url='https://github.com/slangsoft/jeraconv',
    license='MIT',
    author='slangsoft',
    author_email='slangsoft@gmail.com',
    description='jeraconv (Japanese Era Name Converter) is a converter that converts Japanese eras to West calendar.',
    keywords='jeraconv japanese era',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
