from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Ignore -e . line
        requirements = [req for req in requirements if req != HYPEN_E_DOT]
    return requirements
    

setup(
    name='mlproject',
    version='0.0.1',
    author='Ammar',
    email='ammarzafar028@gmail',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
