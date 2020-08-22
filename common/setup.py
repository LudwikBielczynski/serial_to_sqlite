from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='common',
      version='0.0.1',
      description='Common used between different modules',
      author='Ludwik Bielczynski',
      author_email='ludwik.bielczynski@gmail.com',
      long_description=long_description,
      packages=['common'],
     )
