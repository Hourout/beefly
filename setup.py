from io import open
from setuptools import setup, find_packages

def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='beefly',
      version='0.8.0',
      install_requires=['tensorview>=0.3.0'],
      description='Dynamic visualization training service in Jupyter Notebook for Keras tf.keras and others.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/Hourout/beefly',
      author='JinQing Lee, Gaojie Wei',
      author_email='hourout@163.com',
      keywords=['keras-visualization', 'keras', 'tf.keras', 'plot', 'chart'],
      license='Apache License Version 2.0',
      classifiers=[
          'Framework :: Jupyter',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Visualization',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
      packages=find_packages(),
      zip_safe=False)
