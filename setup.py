from setuptools import setup, find_packages

long_description = "Chromatose is a package for storing and visualizing palettes and constructing new ones via interpolation.\n\nThe stored palettes are typically diverging, and mostly for personal record.\nVisualizations include swatches, pies, points, lines, scatters, and heatmaps.\nThere are a multitude of beautiful gradients in packages like bokeh and colorcet that are,  for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a great way to visualize the results."

setup(
    name="chromatose",
    version="0.0.4",
    description="Personal palette collection, mini-palette visualizer & interpolator",
    long_description = long_description,
    url="https://github.com/atisor73/chromatose",
    download_url="https://github.com/atisor73/chromatose/archive/v0.0.4.tar.gz",
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
