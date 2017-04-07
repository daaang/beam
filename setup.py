# lilconf: Li'l Configure
# Copyright 2017 Matt LaChance
#
# This file is part of lilconf.
#
# lilconf is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# lilconf is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with lilconf. If not, see <http://www.gnu.org/licenses/>.
from setuptools import setup
from os import walk
from os.path import abspath, dirname, join
from re import compile as re_compile
from sys import version_info
from Cython.Build import cythonize

class DevelopmentStatus:

    planning = "1 - Planning"
    pre_alpha = "2 - Pre-Alpha"
    alpha = "3 - Alpha"
    beta = "4 - Beta"
    stable = "5 - Production/Stable"
    mature = "6 - Mature"
    inactive = "7 - Inactive"

CURRENT_STATUS = DevelopmentStatus.planning
RE_PYTHON_FILE = re_compile(r"^.*\.pyx?$")

def get_path_to_base_directory():
    return abspath(dirname(__file__))

def get_file_contents(*args):
    with open(join(*args)) as the_file:
        result = the_file.read()

    return result

def all_files_under (base_dir):
    for root, dirs, filenames in walk(base_dir):
        for filename in filenames:
            yield join(root, filename)

def all_python_source_files (base_dir):
    for filename in all_files_under(base_dir):
        match = RE_PYTHON_FILE.match(filename)

        if match is not None:
            yield filename

def all_cython_source_files (base_dir):
    for filename in all_files_under(base_dir):
        if filename.endswith(".pyx"):
            yield filename

def get_ext_modules(base_dir):
    cython_files = list(all_cython_source_files(base_dir))

    if cython_files:
        return cythonize(cython_files)

def maybe_replace_collections_abc (path):
    contents = get_file_contents(path)

    if "collections.abc" in contents:
        with open(path, "w") as f:
            f.write(contents.replace("collections.abc", "collections"))

def make_valid_for_3_2 (lib_dir):
    for source_file in all_python_source_files(lib_dir):
        maybe_replace_collections_abc(source_file)

def make_backwards_compatible (base_dir):
    if version_info < (3, 3):
        print("Making backwards compatible for <3.3 ...")
        make_valid_for_3_2(join(base_dir, "lib"))

base_dir = get_path_to_base_directory()
make_backwards_compatible(base_dir)
long_desc = get_file_contents(base_dir, "README.rst")

setup(
    name="lilconf",
    version="1.0.0.dev0",
    description="Li'l Configure",
    long_description=long_desc,
    license="GPLv3",
    author="Matt LaChance",
    author_email="mattlach@umich.edu",

    classifiers=[
        " :: ".join(("Development Status", CURRENT_STATUS)),
        " :: ".join(("License", "OSI Approved",
                     "GNU General Public License v3 (GPLv3)")),
        " :: ".join(("Natural Language", "English")),
        " :: ".join(("Programming Language", "Cython")),
        " :: ".join(("Programming Language", "Python", "3", "Only")),
    ],

    packages=["lilconf"],
    package_dir={"": "lib"},
    ext_modules=get_ext_modules("lib/lilconf"),
)
