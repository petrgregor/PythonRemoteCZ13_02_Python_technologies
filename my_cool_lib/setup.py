from setuptools import setup, find_packages

setup(
    name="my_cool_lib",
    version=0.1,
    author="Petr Gregor",
    author_email="pe.gregor@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description="Super usefull library"
)