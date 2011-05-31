from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='EmptyTestPkg',
      version=version,
      description="Empty package for test purpose only",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='empty',
      author='Bruno Binet',
      author_email='binet.bruno@gmail.com',
      url='https://github.com/bbinet/EmptyTestPkg',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
