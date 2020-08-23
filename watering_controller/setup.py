from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='watering_controller',
      version='0.0.1',
      description='Scheduler and controller for the valves',
      author='Ludwik Bielczynski',
      author_email='ludwik.bielczynski@gmail.com',
      long_description=long_description,
      packages=['watering_controller'],
     )
