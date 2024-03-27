"""
This file is used to install the package.
"""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="github_scraper",
    version="0.1",
    packages=find_packages(where="."),
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        scraper=cli.handler:scraper
    """,
)
