#!/usr/bin/env python
# Python script for simulation and estimation of summary statistics

'''
author: Cesar Fortes-Lima & Paul Verdu
created: 09-2017
'''

import os, sys, argparse, pdb
import random, time, numpy
import numpy as np
import datetime, shutil, psutil
import collections
from collections import deque
from collections import Counter
from tqdm import tqdm
import subprocess
from subprocess import Popen

global args, parser
parser=argparse.ArgumentParser()

parser.add_argument('-d', '--wdir', required=True, help='Path to working directory of input files')
parser.add_argument('-m', '--model_name', help='Name of the simulated admixture model, which will be used to name the folder with all simulations generated based on that model')
parser.add_argument('-g', '--gen', required=True, type=int, help='Number of generations since founding')
parser.add_argument('-i', '--input_snp', required=True, type=str, help='Parfile input to run fsc25. Only if Ne and nb_SNPs is different than 1000 and 10000')

args=parser.parse_args()
	
usage="python adm_METHIS.py --gen {generations#} --wdir {path/directory#} ...' [help= python adm_METHIS.py --help]"

args=parser.parse_args()

#########################################################################################################


intro='\n'
intro += '#-------------------------------------------------------------------------------------------\n'
intro += '****             		METHIS simulator Version 1.0.0				****\n'
intro += '****             		   Copyright 2016-2017					****\n'
intro += '****             		by C. Fortes-Lima & P. Verdu				****\n'
intro += '****											****\n'
intro += '****             	Admixture models based on Verdu & Rosenberg. 2011		****\n'
intro += '****             		doi: 10.1534/genetics.111.132787			****\n'
intro += '****	 	Information at https://github.com/cesarforteslima/METHIS-simulator	****\n'
intro += '#-------------------------------------------------------------------------------------------\n'

print intro

#########################################################################################################


################################################################################################################################################

