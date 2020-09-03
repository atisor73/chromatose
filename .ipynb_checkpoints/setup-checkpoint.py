from setuptools import setup, find_packages

setup(
    name="chromatose",
    version="0.0.1",
    description='personal palette storage & visualizer',
    author='Rosita Fu',
    author_email='rosita.fu99@gmail.com',
    packages=['pigmentosa'],
    install_requires=['numpy','pandas','bokeh']
)