from setuptools import setup, find_packages

setup(
    name="vector_modeling",
    version="0.1.0",
    author="Junjie Lu",
    author_email="lujj95@gmail.com",
    description="A small, lightweight library for vector operations",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JunjieLu95/vector_modeling",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)