import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="StorageAdapter",  # Replace with your own username
    version="0.0.1",
    author="Travis Thomas",
    author_email="travis.s.thomas@gmail.com",
    description="An adapter to interface with various storage back-ends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/travisthomas/StorageAdapter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
