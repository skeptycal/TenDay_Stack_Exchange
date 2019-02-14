import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TenDays: Stack Exchange Data",
    version="0.0.1",
    author="Michael Treanor",
    author_email="skeptycal@gmail.com",
    description="A tremendous 10 day whirlwind tour of data analysis using Stack Exchange Data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skeptycal/TenDay_Stack_Exchange.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ]
)