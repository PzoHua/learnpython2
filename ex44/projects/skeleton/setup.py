try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
