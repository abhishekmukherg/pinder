from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

VERSION = "0.8b"
requirements = ['httplib2']

# if Python < 2.6 add simplejson to required packages
import platform
major, minor, build = platform.python_version_tuple()
if (int(major) == 2) and (int(minor) < 6):
    requirements.append('simplejson')

setup(
    name='pinder',
    version=VERSION,
    description='Python API for Campfire.',
    license='BSD',
    author='Lawrence Oluyede',
    author_email='l.oluyede@gmail.com',
    url='http://github.com/pinder',
    packages=['pinder'],
    package_data = {
        '': ['CHANGELOG', 'LICENSE', 'README', 'TODO'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=requirements,
    zip_safe=False,
) 
