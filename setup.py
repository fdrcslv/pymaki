from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pymaki',
      version=0.02,
      description='Maki icons in python',
      long_description= readme(),
      url='',
      author='Federico Silvestri',
      author_email='Silvestri.federico.14@gmail.com',
      license='MIT',
      packages=['pymaki'],
      zip_safe=False,
      include_package_data=True
)
