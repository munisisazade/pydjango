import setuptools
import sys
import os
import shutil
from distutils.sysconfig import get_python_lib

with open("README.md", "r") as fh:
    long_description = fh.read()



if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    path = lib_paths[0]
    if os.path.isdir(os.path.join(path, "pydjango-{}-py3.6.egg".format(__import__("pydjango").VERSION))):
        root_path = os.path.join(path, "pydjango-{}-py3.6.egg".format(__import__("pydjango").VERSION))
        shutil.copytree("pydjango/conf/_development", os.path.join(root_path, "pydjango/conf/_development"))
    # os.path.join(path)


setuptools.setup(
    name="pydjango",
    version=__import__("pydjango").VERSION,
    author="Munis Isazade",
    author_email="munisisazade@gmail.com",
    description="PyDjango, create django application with command line interface.",
    long_description=long_description,
    license='MIT',
    url="https://github.com/munisisazade/pydjango",
    scripts=['pydjango/script/create_django.py'],
    entry_points={'console_scripts': [
        'create_django = pydjango.core.management:execute_from_command_line',
    ]},
    platforms=['any'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)