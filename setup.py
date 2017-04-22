from setuptools import setup

setup(name='bokehpivot',
      version='0.1',
      description='Class for apps that require bokeh pivot functionality',
      url='http://github.com/mmowers/bokehpivot',
      author='Matt Mowers',
      author_email='Matthew.Mowers@nrel.gov',
      packages=['bokehpivot'],
      install_requires=[
          'pandas',
          'bokeh',
      ],
)
