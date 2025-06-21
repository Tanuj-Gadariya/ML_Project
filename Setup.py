from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' 

def get_Requirements(file_path:str)->List[str]:
    '''
    This fuction will return the list of Requirements
    '''
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()
        Requirements=[req.replace('/n','') for req in Requirements]
        
        if HYPEN_E_DOT in Requirements:
            Requirements.remove(HYPEN_E_DOT)

    return Requirements

setup(
name ='ML_Project',
version ='0.0.1',
author='Tanuj Gadariya',
author_email='gadariyatanuj9@gmail.com',
packagea= find_packages(),
install_requires=get_Requirements('Requirements.txt')
       



)