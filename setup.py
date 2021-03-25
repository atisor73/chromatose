from setuptools import setup, find_packages

long_description = "Chromatose is a package for storing and visualizing palettes, constructing new ones via interpolation or extraction.\n\nThe stored palettes are for personal record, featuring diverging and continuous palettes.\nVisualizations include swatches, pies, points, lines, scatters, and heatmaps.\nThere are a multitude of beautiful gradients in packages like bokeh and colorcet that are, for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few intermediary points. The underlying algorithm uses a combination of linear and polynomial splines in customizable color space metrics RGB, HSL, or HSV. Heatmaps are a great way to visualize the results.\n To extract palettes from images, chromatose employs k-means clustering and median-cut algorithms."

setup(
    name="chromatose",
    version="1.0.0",
    description="Personal palette collection, palette visualizer, interpolator, and extractor",
    long_description=long_description,
    url="https://github.com/atisor73/chromatose",
    download_url="https://github.com/atisor73/chromatose/archive/v1.0.0.tar.gz",
    license="MIT",
    author='Rosita Fu',
    author_email='rosita.fu99@gmail.com',
    packages=find_packages(),
    entry_points ={ 'console_scripts':
                        ['chromatrieve = chromatose.chromatrieve:main',
                         'chromextract = chromatose.chromextract:main'
                        ] },
    install_requires=['numpy','scipy','pandas','bokeh'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Visualization"
    ]
)
