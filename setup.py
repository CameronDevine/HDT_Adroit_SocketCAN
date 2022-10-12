import setuptools

setuptools.setup(
    name="AdroitComs",
    version="0.0.1",
    author="Cameron Devine",
    author_email="camdev@uw.edu",
    description="A package for communicating with HDT Adroit robots over CAN.",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'python-can',
        'numpy',
    ]
)
