from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='Ghetto_Chara_Builder',
      version=version,
      description="A very simple D&D Character Builder",
      long_description="""\
A very simple D&D Character Builder""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jeffrey Ness',
      author_email='jness@flip-edesign.com',
      url='',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      package_data = {
          'Ghetto_Chara_Builder': ['*.db'],
      },
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points= {
          'console_scripts': ['Ghetto_Chara_Builder = ghetto_chara_builder.CharaBuilder:main']
        },
      )
