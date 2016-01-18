from setuptools import setup

setup(name='random_animal',
      version='0.1',
      description='Script that generates a random adjective and animal',
      url='http://github.com/Thorrik58/random_animal',
      author='Thorrik58',
      license='MIT',
      packages=['random_animal'],
      package_data={'': ['adjectives.txt', 'animals.txt']},
      zip_safe=False)
