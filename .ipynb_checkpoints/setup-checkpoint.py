from setuptools import setup, find_packages

from os import path
direc = path.abspath(path.dirname(__file__))
with open(path.join(direc, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="chromatose",
    version="0.0.3",
    description="Personal palette collection, mini-palette visualizer & interpolator",
    long_description = long_description,
    url="https://github.com/atisor73/chromatose",
    download_url="https://github.com/atisor73/chromatose/archive/v0.0.3.tar.gz",
    license="MIT",
    author='Rosita Fu',
    author_email='rosita.fu99@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','scipy','pandas','bokeh'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Visualization"
    ]
)
