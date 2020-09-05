from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="chromatose",
    version="0.0.1",
    description="personal palette collection & visualizer",
    long_description = readme,
    long_description_content_type="text/markdown",
    url="https://github.com/atisor73/chromatose",
    author='Rosita Fu',
    author_email='rosita.fu99@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','scipy','panel','pandas','bokeh'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ]
)