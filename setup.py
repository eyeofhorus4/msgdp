import codecs
import os
import re
from setuptools import setup, find_packages


###################################################################
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_PATH = os.path.join("src", "msgdp", "__init__.py")
META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


###################################################################
NAME = find_meta("name")
DESCRIPTION = find_meta("description")
LICENSE = find_meta("license")
URI = find_meta("uri")
VERSION = find_meta("version")
AUTHOR = find_meta("author")
AUTHOR_EMAIL = find_meta("author_email")
MAINTAINER = find_meta("maintainer")
MAINTAINER_EMAIL = find_meta("maintainer_email")
KEYWORDS = ["class", "attribute", "boilerplate"]
LONG = (
    read("README.rst") + "\n\n" +
    "Release Information\n" +
    "===================\n\n" +
    re.search("(\d+.\d.\d \(.*?\)\n.*?)\n\n\n----\n\n\n",
              read("CHANGELOG.rst"), re.S).group(1) +
    "\n\n`Full changelog " +
    "<{uri}en/stable/changelog.html>`_.\n\n".format(uri=URI) +
    read("AUTHORS.rst")
)
PACKAGES = find_packages(where="src")
PACKAGE_DIR = {"": "src"}
ZIP_SAFE=False
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = []
INCLUDE_PACKAGE_DATA = True


###################################################################
"""
This method will extract the metadata from:
      /src/msgdp/__init__.py file.
"""
if __name__ == "__main__":
    setup(
        name=NAME,
        description=DESCRIPTION,
        license=find_meta("license"),
        url=URI,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        keywords=KEYWORDS,
        long_description=LONG,
        packages=PACKAGES,
        package_dir=PACKAGE_DIR,
        zip_safe=ZIP_SAFE,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        # include_package_data=INCLUDE_PACKAGE_DATA,
    )
