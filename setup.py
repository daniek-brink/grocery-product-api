
# System imports
from setuptools import setup, find_packages

with open('requirements_pip.txt') as f:
    requirements = f.read().splitlines()
print(requirements)
requirements = [x for x in requirements if x[:4] != 'http']
print(requirements)

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setup(name='grocery_product_api',
      version='0.0.0.0',
      description='Add products to inventory API',
      long_description=readme,
      long_description_content_type='text/markdown',
      license='PROPRIETY',
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      zip_safe=False,
      requires=[])
