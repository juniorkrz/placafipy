from setuptools import setup

setup(
    name='FiPy',
    version='1.0.0',
    packages=['fipy'],
    install_requires=[
        'beautifulsoup4==4.12.3',
        'Unidecode==1.3.8',
        'requests==2.31.0'
    ],
    author='Antônio Roberto Júnior',
    author_email='pix@jrkrz.com',
    description='Consultas FIPE pela placa do veículo.',
    url='https://github.com/juniorkrz/fipy',
    license='MIT',
    keywords='placa fipe veiculo'
)
