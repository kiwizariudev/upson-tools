from setuptools import setup

setup(
    name="upson" ,
    version ="1.0.0",
    author="kiwizariu",
    py_modules=["main"],
    install_requires=open("requirements.txt").read().splitlines(),
)