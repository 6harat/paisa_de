import re
from codecs import open
from setuptools import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='paisa_de',
    version='0.0.1',
    description='Expense Management App',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Gulats/paisa_de',
    author='Gulats',
    author_email='bharat.gulati.certi@gmail.com',
    packages=['paisa_de'],
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
		'aiocontext>=0.1.1',
        'aiodns>=2.0.0',
        'aiohttp>=4.0.0a0',
		'attrs>=19.1.0',
		'cattrs>=0.9.0',
        'cchardet>=2.1.4',
		'Cython>=0.29.7',
		'matplotlib>=3.1.0',
		'numpy>=1.16.2',
		'pydash>=4.7.5'
	],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=[
        'faker',
        'nose'
    ],
)
