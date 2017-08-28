#!/usr/bin/env python
# Python script for simulation of complex models of admixture and calculation of summary statistics

'''
author: Cesar Fortes-Lima & Paul Verdu
created: 01-2017
'''

import os, sys, argparse
import random, time, numpy
import pdb, psutil
import numpy as np
import subprocess
from subprocess import Popen
import multiprocessing
from multiprocessing import Pool
from tqdm import tqdm
from collections import deque
import glob, shutil

global args, parser

usage="METHIS simulator basic usage:  (see manual for further information) "

parser=argparse.ArgumentParser(usage)

parser.add_argument('-d', '--wdir', required=True, help='Path to working directory with the input files')
parser.add_argument('-M', '--model_name', type=str, help='Name of the simulated admixture model, which will be used to name the folder with all simulations generated based on that model')
#parser.add_argument('-1g', '--first_gen', default=1, type=int, help='First generation of admixture')
parser.add_argument('-g', '--gen', required=True, type=int, help='Number of generations since foundation')
parser.add_argument('-i', '--input_snp', required=True, type=str, help='Parfile input to run fsc25. Only if Ne and nb_SNPs is different than 1000 and 10000')
parser.add_argument('-fsc', '--fastsimcoal2', default=None, type=str, help='Running fsc25 and/or converting fsc25 output format. Note about extension files: [inputname].par and [outpoutname]_1_1.arp . Only if Ne and nb_SNPs is different than 1000 and 10000. Please, create your own parfile')
parser.add_argument('-N', '--nb_SNP', default=50000, type=int, help='Number of independent SNPs, default= 50000')
parser.add_argument('-Ne', '--Ne', default=1000, type=str, help='Effective population size at foundation, default= 1000/Con/default. Change with Neg0/model[Con, Inc, Dec, or All]/Negn[min-max, or default]')
parser.add_argument('-s1', '--list_s1', required=True, type=str, help='Parameters for the source population s1: sourcepop1[proportion of s1g0]/model[Con, Inc, Dec, or All]/trend[min-max, or default]/s1g1[min-max, linear, or default]/s1gn[min-max, or default]')
parser.add_argument('-s2', '--list_s2', required=True, type=str, help='Parameters for the source population s2: sourcepop2[proportion of s2g0]/model[Con, Inc, Dec, or All]/trend[min-max, or default]/s2g1[min-max, linear, or default]/s2gn[min-max, or default]')
parser.add_argument('-s', '--sampling', default=100/100/100, type=str, help='Sample size sampled for each population (s1, s2, and adm) in the ASD analysis, default= 100')
parser.add_argument('-r', '--rel_ind', default=0.05, type=str, help='Threshold of proportion of related individuals allowed in the ASD analysis, default= 5 per cent')
parser.add_argument('-sim', '--nb_simulations', default=10, type=int, help='Number of simulations, default= 10')
parser.add_argument('-ts', '--nb_threads', default=1, type=str, help='Number of threads, default= 1. [All] for the maximum number of threads available')
parser.add_argument('-p', '--plots', type=str, default=None, help='Plotting MDS based on ASD matrix for the last generation, or for each generation [Last_gen, All_gen, or None]')
parser.add_argument('-c', '--check_data', default=True, help='Checking parameters before running the script, default=True')
parser.add_argument('-ss', '--sumstat_only', default=None, help='Keep only summary statistics for each model and remove simulate data, default=None')

args=parser.parse_args()


intro='\n'
intro += '#-------------------------------------------------------------------------------------------\n'
intro += '#****             		METHIS simulator Version 1.0.0				****\n'
intro += '#****             		   Copyright 2016-2017					****\n'
intro += '#****             		by C. Fortes-Lima & P. Verdu				****\n'
intro += '#****											****\n'
intro += '#****             	Admixture models based on Verdu & Rosenberg. 2011		****\n'
intro += '#****             		doi: 10.1534/genetics.111.132787			****\n'
intro += '#****	 		Information at http://github.com/cesarforteslima/methis		****\n'
intro += '#-------------------------------------------------------------------------------------------\n'
intro += '#-------------------------------------------------------------------------------------------\n'


#########################################################################################################




