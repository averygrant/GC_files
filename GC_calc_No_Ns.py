#!/usr/bin/env python3

#script made by Avery Grant Feb 2022
#calculate GC content from aTRAM stitcher output in multiple directories
#goals: 
#1. create a list for each taxon containing # of each nucleotide, gene length, and GC content
#2. each item in list contains all the info from goal #1 for each gene
#3. each list is copied to a taxon specific file

import os
from Bio import SeqIO
import re

#path for where you want each taxon file to be created
GC_path = "/datapool/data/ecomorph_selection/GC_files/"

#path to all the stitcher output directories
stitch_dir_path = "/datapool/data/ecomorph_selection/stitcher_output/final_stitcher_output/" 

##subset of a few output directories and files for a test
#stitch_dir_path ="/datapool/data/ecomorph_selection/stitcher_output/test_dir/"

#regular expression search term for file names to extract gene name from file
filenamesearchterm = '(^\d+\w+.)(\w+.\w+)(.stitched_exons.fasta)'

#list of all taxa names
taxanames = ["Aacoc", "Afalc", "Agwat", "AlspHabad", "Ancra", "Anpho", "Apcan", "Aqocc", "Arexp", "Atict", "Atkey", "Brant", "BrspMeorn", "Cacom", "Cfsub", "Chtex", "Cocal", "Cpobs", "Crimm", "Csafr", "Cxnum", "Dgruf", "Dimex", "Dobre", "Esbre", "Etcla", "Famar", "Fulon", "Gdort", "Hldiv", "Ibbis", "Licap", "Mgtat", "MrspMeorn", "MuspNyalb", "Nsbus", "Nylon", "Oscur", "Oxchi", "Pgvar", "Pnsp", "Popap", "PpspTymel", "Psplu", "QkspCagal", "Qupun", "RaspApsp", "Salar", "Sglip", "SlspRhame", "Slstr", "Snsp", "SpspTapor", "Tiele", "TkspTupyr", "Vegui", "Wiabs"]

##list of all directories containing gene files from aTRAM stitcher output
stitch_dirs = os.listdir(stitch_dir_path)
#print(stitch_dirs)


#created empty dictionary to add taxon as key and other info (e.g. gene length) as values 
tax_lists = {}

for taxon in taxanames:
    tax_lists[taxon] = []

#adding header to each taxon key
#NoN = no Ns in sequence aka GC content excluding the # of Ns in sequence length
for snow in tax_lists.keys():
    header = ('Gene_name', 'Taxa', '#_A', '#_C', '#_T', '#_G', '#_N', 'Gene_length', 'Gene_length_NoN', 'GC_content', 'GC_content_NoN')
    tax_lists[snow] += [header]

#print(tax_lists)

##moving into each of the directories containing stitcher output (stitch_dirs)
#os.getcwd prints directory and os.listdir prints all the files in the directory
for dir in stitch_dirs:
        os.chdir(stitch_dir_path + dir)
        for filename in os.listdir():
            if re.match(filenamesearchterm, filename): #extracting gene name from file name
                FullFile = re.search(filenamesearchterm, filename)
                FullFileString = FullFile.group(1) + FullFile.group(2) + FullFile.group(3)
                GeneName = FullFile.group(2) #saving gene name in variable
                #print(FullFile)
                #print(FullFileString)
                ReadFile = open(FullFileString, 'r') #open file with file name saved into variable from above
                #print(seq_dict)
                for ss in SeqIO.parse(ReadFile, 'fasta'): #for each sequence in file opened above
                    seqw = str(ss.seq)                    #save sequence as string
                    numA = seqw.count('A')                #count # of As
                    numC = seqw.count('C')                #count # of Cs
                    numT = seqw.count('T')                #count # of Ts
                    numG = seqw.count('G')                #count # of Gs
                    numN = seqw.count('N')                #count # of Ns
                    genelength = len(seqw)                #measure gene length
                    for bb in tax_lists.keys():           #for each of the taxon names (keys) in the tax_list dictionary
                        if ss.id == bb:  ##if the ID name from a sequence in file matches the taxon key name
                            line = (GeneName, ss.id, numA, numC, numT, numG, numN, genelength, genelength-numN, (numG+numC)/genelength*100, (numG+numC)/(genelength-numN)*100) 
                            tax_lists[bb] += [line] #add line with sequence info & GC content
                            #print(tax_lists)


allFiles = []    #create empty list to add file names to extract later
for fellow in tax_lists.keys():   #for each taxon in tax_list dict
    filename = str(fellow + '.txt')  #save as taxon.txt
    allFiles.append(filename)   #append to list
#for nim in allFiles:
#    print(nim)

#change to directory where you want the files to save to
os.chdir(GC_path)

for fellow in tax_lists.keys():   #for each taxon in dict (taxa are the keys in the dictionary)
    with open(fellow + '.txt', 'w') as f:    #open each file as f
        f.write("\n".join(str(item).strip('\(\)') for item in tax_lists[fellow])) #write each item for that taxon to file
        f.close()
    




