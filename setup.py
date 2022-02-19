from setuptools import find_packages, setup

setup(
    name="plex-toolbox",
    version="0.1",
    packages=find_packages(),
    scripts=["scripts/download-album"],
    install_requires=["pathvalidate", "plexapi", "tqdm"],
    author="Martin Patz",
    author_email="mailto@martin-patz.de",
    description="A loose collection of scripts to interact with "
    "a Plex Media Server (PMS).",
    license="GNU GENERAL PUBLIC LICENSE",
    license_file="LICENSE",
)
