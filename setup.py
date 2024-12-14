from setuptools import setup, find_packages
from typing import List
dot = '-e .'
def get_requirements() -> List[str]:
    requirements= []
    with open('requirements.txt') as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if dot in requirements:
            requirements.remove(dot)
    return requirements        
setup(
    name='Noj',
    version='0.0.1',
    description='PyLib',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)