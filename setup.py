from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pibiaddress/__init__.py
from pibiaddress import __version__ as version

setup(
	name="pibiaddress",
	version=version,
	description="Mark Addresses on a Map",
	author="pibiCo",
	author_email="pibico.sl@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
