import setuptools

setuptools.setup(
    name='travis-image-status',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/travis-image-status']
)
