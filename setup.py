from setuptools import setup, find_packages

setup(
    name='kpc_connector_utils',
    packages=find_packages(),
    version='0.1.9',
    description='Connector utils and configs',
    author='Praiwan N.',
    author_email='npraiwan@outlook.com',
    url='https://github.com/praiwann/kpc-connector-utils',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'boto3>=1.0.0',
    ],
)
