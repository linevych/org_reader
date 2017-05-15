import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='org_reader',
    version='0.1',
    packages=[
        'org_reader',
    ],
    include_package_data=True,
    url='https://github.com/linevich/org_reader',
    license='BSD 3-clause',
    long_description=README,
    author='Matthew Snyder, Anton Linevych',
    author_email='mail@linevich.net',
    description='Org-mode reader for Pelican.',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
