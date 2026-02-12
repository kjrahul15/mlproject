from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    Docstring for get_requirements
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
name='mlproject',
version='0.1.0',
author='Rahul K J',
author_email='kjrahul49@gmail.com',
packages=find_packages(),
#install_requires=['numpy', 'pandas', 'seaborn'], or we can use the get_requirements function to read from requirements.txt
install_requires=get_requirements('requirements.txt'),
)