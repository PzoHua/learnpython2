#_*_coding=utf-8_*_

# 该文件在安装项目的时候会用到

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': '习题49配置信息',
	'author': 'puzhonghua',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': '191......',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname',
}

setup(**config)
