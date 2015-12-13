try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Sylvia Kieha',
    'url' : 'URL',
    'download_url' : 'where to download it at',
    'author_email' : 'sylviakieha@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['sample'],
    'scripts' : [],
    'name' : 'sample'
}

setup(**config)
