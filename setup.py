from setuptools import find_packages, setup

setup(
    name="sandbox",
    packages=find_packages(exclude=["sandbox_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
