from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))
DESCRIPTION = "dfm is a linux tools for Dot's Files Manager. (backup or restore)"
KEYWORDS = ['dfm', 'dotfiles', 'backup', 'backup-script', 'linux', 'python']
AUTHORS = 'lisuke'
URL = 'http://github.com/lisuke/dfm'
EMAIL = '1657787678@qq.com'

with open(path.join(DIR, 'requirements.txt')) as f:
    INSTALL_PACKAGES = f.read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

# get __version__ from _version.py
ver_file = path.join('dfm', '_version.py')
with open(ver_file) as f:
    exec(f.read())

VERSION = __version__

setup(
    name='dfm',
    packages=['dfm'],
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version=VERSION,
    url=URL,
    author=AUTHORS,
    author_email=EMAIL,
    keywords=KEYWORDS,
    license = "GPLv3",
    tests_require=[
        # 'pytest'
    ],
    include_package_data = True,
    platforms = "any",
    python_requires = '>=3',
    entry_points = {
        'console_scripts': [
            'dfm = dfm.dfm:main'
        ]
    }
)