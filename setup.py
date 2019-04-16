import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dokr',
    version='0.1',
    scripts=['dokr'],
    author="Leonardo Nascimento",
    author_email="lnascimento1988@gmail.com",
    description="A validation utils package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lsnascimento/bula",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ]
)