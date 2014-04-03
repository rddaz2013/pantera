from setuptools import setup

setup(name='pantera',
      version='0.1',
      description='Pantera is a toolset for using and extending Cantera in Python.',
      url='http://github.com/charlesreid1/pantera',
      author='Charles Reid',
      author_email='root@charlesmartinreid.com',
      license='MIT',
      packages=['pantera','pantera.gases','pantera.reactors'],
      zip_safe=False)
