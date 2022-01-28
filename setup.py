from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="morpheus-mcpi",
    version="2.0",
    description="Hacked client utilities for Minecraft Pi.",
    url="https://github.com/bigjango13/Morpheus-2",
    author="bigjango13",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["morpheus"],
    install_requires=["keyboard", "pysimplegui", "mcpi"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "morpheus = morpheus.__main__:start",
            "mcpi-spectator = morpheus.spectator_mode:switch",
        ]
    },
)
