from setuptools import setup, find_packages

setup(
name="Analisis_historico_de_LaLiga_19952025",
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