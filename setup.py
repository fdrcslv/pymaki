from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='python-maki-icons',
      version=0.01,
      description='Maki icons in python',
      long_description= readme(),
      url='',
      author='Federico Silvestri',
      author_email='Silvestri.feerico.14@gmail.com',
      license='MIT',
      packages=['python-maki-icons'],
      install_requires=[
        'xml',
      ],
      zip_safe=False,
      include_package_data=True
)
