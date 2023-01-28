from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.5"
DESCRIPTION = "A python module to convert text quotes into graphical images"
LONG_DESCRIPTION = DESCRIPTION

setup(
    name="Quote2Image",
    version=VERSION,
    author="NotCookey",
    url="https://github.com/NotCookey/Quote2Image",
    author_email="kanao.nishimiya@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=["Pillow==9.2.0"],
    keywords=[
        "quotes",
        "images",
        "text",
        "conversion",
        "quote2image",
        "quote to image",
        "quote text to image",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
