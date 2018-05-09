from setuptools import setup

setup(name='virshdumpparser',
      version='0.2',
      description='Parser to parse the virsh dump xml files',
      url='https://github.com/petersinghanburaj/virshdumpparser',
      author='Petersingh Anburaj',
      author_email='panburaj@redhat.com',
      packages=['virshdumpparser'],
      install_requires=['terminaltables'],
      platforms=['Linux'],
      package_dir={'virshdumpparser': 'virshdumpparser'},
      entry_points={'console_scripts': ['virshdumpparser=virshdumpparser.cli:main']}
      )
