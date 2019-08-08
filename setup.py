from setuptools import setup

setup(
    name="grandas",
    version="0.0.1",
    description="Simple and flexible graph database analysis",
    url="http://github.com/austinbrian/grandas",
    author="Brian Austin",
    author_email="austin.brian+gh@gmail.com",
    license="BSD-3",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["grandas"],
    zip_safe=False,
)
