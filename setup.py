from pathlib import Path

from setuptools import setup

# read the contents of your README file
long_description = Path(__file__).with_name("README.md").read_text()
all_kedro_extras = (
    "api",
    "biosequence",
    "dask",
    "docs",
    "geopandas",
    "matplotlib",
    "holoviews",
    "networkx",
    "pandas",
    "pillow",
    "plotly",
    "redis",
    "spark",
    "tensorflow",
    "yaml",
)

setup(
    name="kedro-light",
    version="0.2.1",
    description="A lightweight interface to Kedro and Kedro-Viz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ellwise/kedro-light",
    author="Elliott Wise",
    author_email="ell.wise@gmail.com",
    license="MIT",
    packages=["kedro_light"],
    install_requires=["kedro", "kedro-viz"],
    extras_require={k: f"kedro[{k}]" for k in all_kedro_extras},
)
