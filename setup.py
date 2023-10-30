from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(filename: str = "requirements.txt") -> List[str]:
    ''' Function returns a list of required packages'''
    requirements = []
    with open(filename) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="End-to-end ML Project",
    version="0.0.1",
    author="Kyle Rodriguez",
    author_email="kylearodriguez10@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
