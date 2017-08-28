#!/usr/bin/env python
# Python script for simulation of complex models of admixture and calculation of summary statistics

'''
author: Cesar Fortes-Lima & Paul Verdu
created: 09-2017
'''

# Usage: python setup.py install


from setuptools import setup

setup(name= 'METHIS',
	version= '1',
	description= 'METHIS simulator to study complex admixture processes',
	url= 'https://github.com/cesarforteslima/methis',
	author= 'Cesar Fortes-Lima & Paul Verdu',
	author_email= 'cesar.fortes-lima@mnhn.fr',
	license= 'Github',
	packages= ['src'],
	install_requires= ['argparse'])


