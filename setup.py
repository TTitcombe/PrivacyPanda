from setuptools import setup

import privacypanda

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="privacypanda",
    version=privacypanda.__version__,
    description="Anonymizing pandas dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords="anonymization privacy pandas privacy-preserving data science",
    url="https://github.com/TTitcombe/privacypanda",
    author="Tom Titcombe",
    author_email="t.j.titcombe@gmail.com",
    license="Apache 2.0",
    packages=["privacypanda"],
    install_requires=["numpy", "pandas"],
    include_package_data=True,
    python_requires=">=3.7",
)
