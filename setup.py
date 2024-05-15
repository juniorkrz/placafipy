from setuptools import setup
from pathlib import Path


# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')


setup(
    name='PlacaFipy',
    version="1.0.3",
    packages=['placafipy'],
    install_requires=[
        'beautifulsoup4==4.12.3',
        'Unidecode==1.3.8',
        'requests==2.31.0'
    ],
    author='Antônio Roberto Júnior',
    author_email='pix@jrkrz.com',
    description='Consultas FIPE pela placa do veículo.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/juniorkrz/placafipy',
    license='MIT',
    keywords='placa fipe veiculo'
)