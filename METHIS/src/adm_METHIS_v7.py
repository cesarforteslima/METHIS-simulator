#!/usr/bin/env python
# Python script for simulation and estimation of summary statistics

'''
author: Cesar Fortes-Lima & Paul Verdu
created: 01-2017
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
parser.add_argument('-1g,', '--first_gen', type=int, help='First generation of admixture')
parser.add_argument('-g', '--gen', required=True, type=int, help='Number of generations since founding')
parser.add_argument('-i', '--input_snp', required=True, type=str, help='Parfile input to run fsc25. Only if Ne and nb_SNPs is different than 1000 and 10000')
parser.add_argument('-Ne', '--Ne', type=str, default= 1000, help='Hybride effective population size at foundation, default= 1000')
parser.add_argument('-s','--sampling', default=100/100/100, type=str, help='Sample size sampled for each population (s1, s2, and adm) in the ASD analysis, default= 100')
parser.add_argument('-N', '--nb_SNP', type=int, default= 10000, help='Number of SNPs in each source population, default= 10000')
parser.add_argument('-sim', '--nb_simulations', type=int, help='Number of simulations, default= 10000')
parser.add_argument('-t', '--nb_threads', default=1, type=str, help='Number of threads, default= 1. [all] for the maximum number of threads available')
parser.add_argument('-p', '--plots', type=str, default='None', help='Plotting MDS based on ASD for each generation [Last_gen, All_gen, or None]')
parser.add_argument('-ms1', '--model_s1', type=str, help="Forward-in-time admixture model for the source population s1")
parser.add_argument('-ms2', '--model_s2', type=str, help="Forward-in-time admixture model for the source population s2")
parser.add_argument('-s1g0', '--sourcepop1', type=str, help="Proportion from the source population 1")
parser.add_argument('-s2g0', '--sourcepop2', type=str, help="Proportion from the source population 2")
parser.add_argument('-s1', '--list_s1', type=str, help="Proportion list from the source population 1 at each generation")
parser.add_argument('-s2', '--list_s2', type=str, help="Proportion list from the source population 2 at each generation")
parser.add_argument('-r', '--rel_ind', type=str, default=0.05, help='Threshold of proportion of related individuals allowed in the ASD analysis, default= 5 per cent')

args=parser.parse_args()
	
usage="python adm_METHIS.py --gen {generations#} --wdir {path/directory#} ...' \
[help= python adm_METHIS.py --help]"

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
intro += '****	 		Information at http://github.com/cesarforteslima/methis		****\n'
intro += '#-------------------------------------------------------------------------------------------\n'

#########################################################################################################
### parametres taux d'admixture (listes de 20 parametres, la somme des premiers parametres de chaque liste doit valoir 1)


################################################################################################################################################

