import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="start-django",
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)