from pathlib import Path
from setuptools import setup


# read the contents of your README file
long_description = Path(__file__).with_name("README.md").read_text()

setup(
    name="kedro-light",
    version=0.2,
    description="A lightweight interface to Kedro and Kedro-Viz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ellwise/kedro-light",
    author="Elliott Wise",
    author_email="ell.wise@gmail.com",
    license="MIT",
    packages=["kedro_light"],
    install_requires=["kedro", "kedro-viz"],
)
