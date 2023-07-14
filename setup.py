from setuptools import setup
  
setup(
    name='happy_customer',
    version='0.1',
    description='A package to predict happy customers',
    author='Zihui Ouyang',
    author_email='makingsurgeon@gmail.com',
    packages=['my_package'],
    install_requires=[
        'scikit-learn',
        'pandas',
    ],
)