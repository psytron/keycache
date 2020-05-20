from setuptools import setup

setup(
    name='keycache', # Needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/psytron/keycache',
    author='Mico Malecki',
    author_email='m@psytron.com',
    packages=['keycache'], # Needed to actually package
    install_requires=['pyAesCrypt','cryptography','pyyaml'],# Needed for dependencies
    version='0.25.6',
    license='Apache 2.0', # Can be anything
    description='Keycache is an AES encrypted keyvalue store for sensitive credentials.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)