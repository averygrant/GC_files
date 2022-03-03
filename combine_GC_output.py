#! /usr/bin/env python

#this script was created 5 Jan 2022. Its purpose is to combine data into specified groups. It finds all matching taxa names and combines the rest of the data as sum, mean, unique occurances, etc. Output can be easily changed by altering the calculation for each column, e.g. changing the # of As from 'sum' to 'mean'

import pandas as pd
import csv
import itertools

#read in datafile
tax_data = pd.read_csv('GC_AllTaxa_NoN.txt')

#determine the calculation to be done with each column (sum, mean, min, unique, etc)
#mean
aggregation_functions_mean = {'Gene_name': 'nunique', '#_A': 'sum', '#_C': 'sum', '#_T': 'sum', '#_G': 'sum', '#_T': 'sum', 'Gene_length': 'mean', 'Gene_length_NoN': 'mean', 'GC_content': 'mean', 'GC_content_NoN': 'mean'}

#median
aggregation_functions_med = {'Gene_name': 'nunique', '#_A': 'sum', '#_C': 'sum', '#_T': 'sum', '#_G': 'sum', '#_T': 'sum', 'Gene_length': 'mean', 'Gene_length_NoN': 'mean', 'GC_content': 'mean', 'GC_content_NoN': 'median'}

#max
aggregation_functions_max = {'Gene_name': 'nunique', '#_A': 'sum', '#_C': 'sum', '#_T': 'sum', '#_G': 'sum', '#_T': 'sum', 'Gene_length': 'mean', 'Gene_length_NoN': 'mean', 'GC_content': 'mean', 'GC_content_NoN': 'max'}

#min
aggregation_functions_min = {'Gene_name': 'nunique', '#_A': 'sum', '#_C': 'sum', '#_T': 'sum', '#_G': 'sum', '#_T': 'sum', 'Gene_length': 'mean', 'Gene_length_NoN': 'mean', 'GC_content': 'mean', 'GC_content_NoN': 'min'}

#for each aggregation function, group by matching taxon name and save to dataframe
full_df_mean = tax_data.groupby(['Taxa']).agg(aggregation_functions_mean)
full_df_med = tax_data.groupby(['Taxa']).agg(aggregation_functions_med)
full_df_min = tax_data.groupby(['Taxa']).agg(aggregation_functions_min)
full_df_max = tax_data.groupby(['Taxa']).agg(aggregation_functions_max)


#save each file to CSV
full_df_mean.to_csv('GC_content_Taxon_mean.csv')
full_df_med.to_csv('GC_content_Taxon_median.csv')
full_df_min.to_csv('GC_content_Taxon_min.csv')
full_df_max.to_csv('GC_content_Taxon_max.csv')

