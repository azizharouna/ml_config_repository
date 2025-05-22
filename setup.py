from setuptools import setup, find_packages

setup(
    name="ml_config_repository",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=6.0",
    ],
    python_requires=">=3.8",
)