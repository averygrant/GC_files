#hey

scripts to calculate GC content. 'GC_calac_No_Ns.py' extracts info per taxon per gene from multiple aTRAM stitcher output directories. 'combine_GC_ouput.py' groups output by taxon. Before this can be used, you need to combine all individual output files from 'GC_calc_No_Ns.py'

After running 'GC_calc_No_Ns.py', I used 'awk FNR!=1 *.txt > ALL.txt' to combine all output files to one file without the header. I manually add the header back on to the new, large file that contains the info for all taxa. 
