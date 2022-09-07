from pathlib import Path

from kedro.pipeline import node
from kedro.pipeline.modular_pipeline import pipeline

from kedro_light.kedro import io, run
from kedro_light.kedro_viz import show

readme = Path(__file__).with_name("README.md").read_text()
readme = "\n".join(readme.split("\n")[1:])  # drop heading line

__doc__ = readme
