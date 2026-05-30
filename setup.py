from setuptools import setup, find_packages

setup(
name="Análisis histórico de LaLiga (1995-2025)",
version="1.0",
author="ChiurazziLorenzo",
packages=find_packages(),
install_requires=[
"pandas",
"matplotlib",
"networkx"
],
python_requires=">=3.10"
)