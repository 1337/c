import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="c",
    version="0.0.2",
    author="Brian",
    author_email="brian@ohai.ca",
    description="Android battery history analyZer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1337/c",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ),
)
