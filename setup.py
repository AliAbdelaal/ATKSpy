from setuptools import setup

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='atkspy',
      version='0.5.1',
      description='A python package that supports SOAP interface to communicate with the Microsoft ATKS',
      long_description= long_description,
      url='https://github.com/AliAbdelaal/ATKSpy',
      author='Ali Abdelaal',
      author_email='aliabdelaal369@gmail.com',
      license='MIT',
      packages=['atkspy'],
      install_requires=[
          'zeep',
      ],
      python_requires='>=3',
      zip_safe=False)