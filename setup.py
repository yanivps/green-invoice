# Always prefer setuptools over distutils
# To use a consistent encoding
from setuptools import setup, find_packages
from os import path

from codecs import open

here = path.abspath(path.dirname(__file__))
__version__ = None
with open("green_invoice/version.py") as f:
    exec(f.read())

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requires = f.readlines()

setup(
    name="green_invoice",
    version=__version__,
    author="Yaniv Pinchas",
    url="https://github.com/yanivps/green-invoice",
    license="LICENSE",
    description="A Python 3 module to interact with the Green Invoice API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requires,
    setup_requires=requires,
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
