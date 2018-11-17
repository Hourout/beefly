from io import open
from setuptools import setup, find_packages

def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='beefly',
      version='0.4.0',
      install_requires=['matplotlib', 'notebook', 'tensorflow>=1.12.0'],
      description='Dynamic visualization training service in Jupyter Notebook for Keras tf.keras and others.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/Hourout/beefly',
      author='JinQing Lee, Gaojie Wei',
      author_email='hourout@163.com',
      keywords=['keras-visualization', 'keras', 'tf.keras', 'plot', 'chart'],
      license='MIT',
      classifiers=[
          'Framework :: Jupyter',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Visualization',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
      packages=find_packages(),
      zip_safe=False)
