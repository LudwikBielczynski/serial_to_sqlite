from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='sensor_handler',
      version='0.0.1',
      description='Everything needed to handle the sensors',
      author='Ludwik Bielczynski',
      author_email='ludwik.bielczynski@gmail.com',
      long_description=long_description,
      packages=['sensor_handler'],
     )
