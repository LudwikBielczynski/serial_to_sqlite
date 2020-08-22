from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='repositories',
      version='0.0.1',
      description='Repositories layer needed for python applications to work',
      author='Ludwik Bielczynski',
      author_email='ludwik.bielczynski@gmail.com',
      long_description=long_description,
      packages=['repositories'],
     )
