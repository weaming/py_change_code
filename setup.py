# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

gh_repo = "https://github.com/weaming/py_change_code"

setup(
    name="py-change-code",  # Required
    version="0.1.0",  # Required
    # This is a one-line description or tagline of what your project does.
    description="Convert between simple and traditional Chinese",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    keywords="language",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={},  # Optional
    project_urls={"Bug Reports": gh_repo, "Source": gh_repo},  # Optional
)
