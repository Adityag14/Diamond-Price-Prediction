from setuptools import find_packages,setup
from typing import List

def get_requriments(file_path:str)->List[str]:
    requriments=[]
    with open(file_path) as obj:
        requriments=obj.readlines()
        requriments=[req.replace('\n',"") for req in requriments]
        
        return requriments
    
setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='Aditya Gawande',
    author_email='gawandeadi2@gmail.com',
    installation_requirements=get_requriments('requriments.txt'),
    packages=find_packages()
)