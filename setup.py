from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(filepath:str)->List[str]:

    '''
    this function gives list of requirements from requirements folder
    '''
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements




setup(
name = "mlproject",
version=  "0.0.1",
author= "Sai Surya Chandra Prasad",
author_email= "saisuryachandraprasad@gmail.com",
packages= find_packages(),
install_requirements = get_requirements("requirements.txt")

)