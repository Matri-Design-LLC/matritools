from setuptools import setup, find_packages

setup(
    name='matritools',
    version='0.2.0',
    packages=find_packages(include=['matritools', 'matritools.*']),
    install_requires=[
        'pandas>=1.1.3',
    ]
)