"""install script for sphinx-natbib"""

from setuptools import setup

if __name__ == '__main__':
    setup(
        #main
        name='sphinx-natbib',
        version='0.1',
        packages=['natbib'],
        requires=['sphinx', 'pybtex'],

        # metadata
        author='W. Nielson',
        author_email='',
        maintainer='Philipp Meier',
        maintainer_email='pmeier82@gmail.com',
        description='sphinx extension to use bibtex files')
