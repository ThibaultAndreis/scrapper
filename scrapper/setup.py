import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scraper",
    version="0.1",
    author="Andreis Thibault & Sapa baptiste",
    description="this package scrape price from cdisount",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThibaultAndreis/scrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bs4',
        'requests',
    ],
    python_requires='>=3.6',
)
