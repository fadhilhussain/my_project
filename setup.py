from setuptools import find_packages,setup
from typing import List

hyphon = '-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function return the requirments list packages 
    '''

    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n"," ")for req in requirments]
    
    if hyphon in requirments:
        requirments.remove(hyphon)

    return requirments

setup(
    name= 'endtoend',
    version= '0.0.1',
    author= 'fadhil_hussain',
    author_email= 'ibnhussainkv@gmail.com',
    packages= find_packages(),
    install_requires = get_requirments('requirements.txt'),
)