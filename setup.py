"""
 Installation script for accelerated upgrade
"""
import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from version import get_version

import re

DESCRIPTION = 'Description'
with codecs.open('README.md', 'r', encoding='UTF-8') as readme:
    LONG_DESCRIPTION = ''.join(readme)

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
]

packages = [
    'vertest',
]

NAME = 'vertest'

# setup_args["version"] = "1.0.0"

setup_args = dict(

    name=NAME,
    version="1.0.0",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Klaudiusz Staniek',
    author_email='klstanie [at] cisco.com',
    url='https://github.com/kstaniek/version',
    download_url='https://github.com/kstaniek/version/tarball/{}'.format(get_version()),
    keywords='version test',
    tests_require=['tox'],
    platforms=['any'],
    packages=packages,
    package_data={'': ['LICENSE', ], },
    package_dir={'vertest': 'vertest'},
    include_package_data=True,
    install_requires=[],
    data_files=[],
    license='Apache 2.0',
    classifiers=CLASSIFIERS,
    zip_safe=False
)


if __name__=="__main__":
          if 'upload' in sys.argv:
              import package
              package.__version__.verify(setup_args['version'])
          setup(**setup_args)