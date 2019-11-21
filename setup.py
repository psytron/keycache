from setuptools import setup

setup(
    name='keycache', # Needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/psytron/keycache',
    author='Mico Malecki',
    author_email='m@psytron.com',
    packages=['keycache'], # Needed to actually package
    install_requires=['pyAesCrypt','cryptography','pyyaml'],# Needed for dependencies
    version='0.22',
    license='PSYTRON', # Can be anything
    description='KeyCache stores the blobs.'
    # long_description=open('README.txt').read(), # Readme eventually (there will be a warning)
)