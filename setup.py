from setuptools import setup


# Description
with open('README.md') as file:
    long_description = file.read()


setup(
    name='pypar',
    version='0.0.1',
    description='Python phoneme alignment representation',
    author='Max Morrison',
    author_email='maxrmorrison@gmail.com',
    url='https://github.com/maxrmorrison/pypar',
    install_requires=['numpy'],
    packages=['pypar'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['alignment', 'duration', 'phoneme', 'speech'],
    license='MIT',
    install_requires=['numpy'])
