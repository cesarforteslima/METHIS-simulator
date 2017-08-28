#! /usr/bin/Rscript

library(e1071)
library(optparse)
args=(commandArgs(TRUE))

option_list <- list(
	make_option(c("-G", "--gen"), type="integer", help="Number of generations since admixture"),
	make_option(c("-Z", "--gen0"), type="integer", help="Number of previous generations"),
	make_option(c("-D", "--dir"), help="Path directory of input files"),
	make_option(c("-M", "--model_s1"), help="Pattern of admixture model for source population s1"),
	make_option(c("-N", "--model_s2"), help="Pattern of admixture model for source population s2"),
	make_option(c("-L", "--sourcepop1g0"), help="Admixture contribution for the source population 1 in the previous generation"),
	make_option(c("-I", "--sourcepop1"), help="Admixture contribution for the source population 1"),
	make_option(c("-S", "--sourcepop2g0"), help="Admixture contribution for the source population 2 in the previous generation"),
	make_option(c("-T", "--sourcepop2"), help="Admixture contribution for the source population 2"),
	make_option(c("-A", "--size_s1"), help="Sampling population 1"),
	make_option(c("-B", "--size_s2"), help="Sampling population 2"),
	make_option(c("-C", "--size_adm"), help="Sampling population adm")
	)

opt <- parse_args(OptionParser(option_list=option_list))

setwd(paste(opt$dir,"/Summary_statistics/",sep=""))

##########################################################





