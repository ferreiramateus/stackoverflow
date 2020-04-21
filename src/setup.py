"""Stack Overflow project setup."""

import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="stack_overflow",
    version="0.1",
    author="Mateus Ferreira",
    author_email="mateusalberto@hotmail.co.uk",
    description="Stack Overflow package",
    long_description='stack_overflow bot',
    long_description_content_type="text/markdown",
    url="https://github.com/ferreiramateus/stackoverflow.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: HUB :: EY License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
