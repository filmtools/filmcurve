from setuptools import setup, find_packages
from codecs import open
from os import path

def readme():
    with open('README.md') as f:
        return f.read()

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='FilmCurve',
    version='2.0.3',
    description='Finds X (or Y) value for a given Y (or X, resp.) on a film density curve.',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='film developing density polynomial interpolation',
    url='http://github.com/filmtools/filmcurve',
    author='Carsten Witt',
    author_email='filmspeed@filmspeed.org',
    license='MIT',
    packages=find_packages(),
    install_requires=[
      'numpy',
      'matplotlib',
      'argparse'
    ],
    scripts=['bin/filmcurve'],
    include_package_data=True,
    zip_safe=False)
