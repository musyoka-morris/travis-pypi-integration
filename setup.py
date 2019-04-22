from os import path
from setuptools import setup, find_packages
from travis_pypi_integration import __version__

dirname = path.abspath(path.dirname(__file__))
with open(path.join(dirname, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='Travis Pypi Integration sample',
    version=__version__,
    packages=find_packages(),
    description='Sample Travis CI + Pypi integration',
    url='https://github.com/musyoka-morris/travis-pypi-integration',
    license='MIT',
    author='Musyoka Morris',
    author_email='musyokamorris@gmail.com',
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7'
    ],
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3',
    keywords='Travis CI, Pypi, integration, CI, CD, automated distribution',
    include_package_data=True,
    long_description=long_description,
)
