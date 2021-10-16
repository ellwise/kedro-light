from setuptools import setup
from os import path


# read the contents of your README file
curr_dir = path.abspath(path.dirname(__file__))
with open(path.join(curr_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kedro-light",
    version="0.1",
    description="A lightweight interface to Kedro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ellwise/naive-bayes-explainer",
    author="Elliott Wise",
    author_email="ell.wise@gmail.com",
    license="MIT",
    packages=["kedro_light"],
    install_requires=["kedro"],
    include_package_data=True,
    zip_safe=False,
)
