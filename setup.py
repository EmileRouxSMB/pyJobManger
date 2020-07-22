from setuptools import setup
import pyJobManger

setup(name='pyJobManger',
      version=pyJobManger.__version__,
      description="A Python simulation manger for batch running",
      long_description="",
      author='Emile Roux',
      author_email='emile.Roux@univ-smb.fr',
      license='GPL v3',
      packages=['pyJobManger'],
      zip_safe=False,
      url='https://github.com/EmileRouxSMB/pyJobManger',
      install_requires=[
          "numpy",
          "scipy",
          "matplotlib",
          "pandas",
          "jupyter",
          "nbconvert",
          ],
      package_data={
      '': ['*'], },
      include_package_data = True
      )
