from setuptools import setup, find_packages


setup(
    name="chromatose",
    version="0.0.2",
    description="Personal palette collection & mini-palette visualizer",
    long_description = "Personal palette collection in `palettes` & mini-palette visualizer with `palplot`",
    url="https://github.com/atisor73/chromatose",
    download_url="https://github.com/atisor73/chromatose/archive/v0.0.2.tar.gz",
    license="MIT",
    author='Rosita Fu',
    author_email='rosita.fu99@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','scipy','pandas','bokeh','colour'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Visualization"
    ]
)