#!/usr/bin/env python

"""
Demonstrates plotting chromosome ideograms and genes (or any features, really)
using matplotlib.
1) Assumes a file from UCSC's Table Browser from the "cytoBandIdeo" table,
saved as "ideogram.txt". Lines look like this::
    #chrom  chromStart  chromEnd  name    gieStain
    chr1    0           2300000   p36.33  gneg
    chr1    2300000     5300000   p36.32  gpos25
    chr1    5300000     7100000   p36.31  gneg
2) Assumes another file, "ucsc_genes.txt", which is a BED format file
   downloaded from UCSC's Table Browser. This script will work with any
   BED-format file.
"""
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle,Circle
from matplotlib.collections import BrokenBarHCollection,PatchCollection
import numpy as n
import pandas as pd
import os.path

# Use cached file if it exists or retreive data from P7 Impala
filename = "kaviar_results.txt"
if os.path.isfile(filename):
  print "Using kaviar_results.txt"
  kaviar = pd.read_csv(filename)
else:
  # Set up connection to P7 Impala
  print("Getting Kaviar Data from P7 Impala...")
  from impala.util import as_pandas
  from impala.dbapi import connect
  conn = connect(host='ec2-54-86-98-154.compute-1.amazonaws.com',port=21050)
  cur = conn.cursor()

  # Describe Kaviar
  cur.execute('use p7_ref_grch37')
  cur.execute('describe kaviar')
  print("Describing Kaviar fields...")
  print('\n'.join(' - '.join(elems) for elems in cur.fetchall()))

  # Getting Kaviar Data
  # this query retrieves chrom 8 p arm 0-23100000
  print("Selecting data from kaviar for chromosome 8 pos 0-23100000")
  cur.execute('select chrom, pos, allele_freq from kaviar where chrom = "8"')
  #cur.execute('select chrom, pos, allele_freq from kaviar where chrom = "8" and pos >= 0 and pos <= 23100000')
  kaviar = as_pandas(cur) # this will take a relatively long time
  kaviar["chrom"] = 'chr' + kaviar["chrom"].astype(str) # need to add chr to the front to match the ideogram and ucsc_genes
  kaviar.to_csv("kaviar_results.txt")
  print("Finished saving kaviar data")

kaviar["start"] = kaviar["pos"]
kaviar["end"] = kaviar["pos"]
kaviar["width"] = kaviar.end - kaviar.start +10
kaviar['colors'] = '#43a822' # green

# bin kaviar data
binned_kaviar = pd.DataFrame(columns=('chrom','start','end','avg','max_af','min_af'))
for chrom, group in kaviar.groupby('chrom'):
	width = group.shape[0]
	binsize = 10000
	num_bins = width/binsize
	for bin in range(0,num_bins+1):
	  bin_start = binsize*bin
	  bin_end = binsize*(bin+1)
	  if bin_end >= width:
	    bin_end = width-1
	  avg = n.ma.average(group[bin_start:bin_end]['allele_freq'])
	  bin_name = 'bin'+str(bin)
	  min_af = min(group[bin_start:bin_end]['allele_freq'])
	  max_af = max(group[bin_start:bin_end]['allele_freq'])
	  start_pos = group[bin_start:bin_start+1]['pos'][bin_start]
	  end_pos = group[bin_end:bin_end+1]['pos'][bin_end]
	  local = {'chrom':chrom,'start':start_pos, 'end':end_pos, 'avg':avg, 'max_af':max_af, 'min_af':min_af }
	  binned_kaviar.loc[bin] = local

binned_kaviar['colors'] = '#43a822' # green
# Here's the function that we'll call for each dataframe (once for chromosome
# ideograms, once for genes).  The rest of this script will be prepping data
# for input to this function
#
def chromosome_collections(df, y_positions, height,  **kwargs):
    """
    Yields BrokenBarHCollection of features that can be added to an Axes
    object.
    Parameters
    ----------
    df : pd.DataFrame
        Must at least have columns ['chrom', 'start', 'end', 'color']. If no
        column 'width', it will be calculated from start/end.
    y_positions : dict
        Keys are chromosomes, values are y-value at which to anchor the
        BrokenBarHCollection
    height : float
        Height of each BrokenBarHCollection
    Additional kwargs are passed to BrokenBarHCollection
    """
    del_width = False
    if 'width' not in df.columns:
        del_width = True
        df['width'] = df['end'] - df['start']
    for chrom, group in df.groupby('chrom'):
        print chrom
        yrange = (y_positions[chrom], height)
        xranges = group[['start', 'width']].values
        yield BrokenBarHCollection(
            xranges, yrange, facecolors=df['colors'], **kwargs)
    if del_width:
        del df['width']

# Here's the function that we'll call for binned_kaviar
#
def kaviar_collections(df, y_positions, height,  **kwargs):
    """
    Yields PatchesCollection of features that can be added to an Axes
    object.
    Parameters
    ----------
    df : pd.DataFrame
        Must at least have columns ['chrom', 'start', 'end', 'avg', 'max_af', 'min_af', 'color']. If no
        column 'width', it will be calculated from start/end.
    y_positions : dict
        Keys are chromosomes, values are y-value at which to anchor the PatchesCollection
    height : float
        Height of each PatchesCollection
    Additional kwargs are passed to PatchesCollection
    """
    del_width = False
    if 'width' not in df.columns:
        del_width = True
        df['width'] = df['end'] - df['start']
    for chrom, group in df.groupby('chrom'):
        print chrom
        max_allele = max(group['max_af'])
        min_allele = min(group['min_af'])
        # min_allele is 0 and max_allele is height
        #  height = 100%, max_allele = X%?
        factor = height/max_allele
        patches = []
        floor = Rectangle((group['start'][0],kaviar_ybase[chrom]),group['width'][0],0.01)
        patches.append(floor)
        for index,row in group.iterrows():
            y2 = kaviar_ybase[chrom] + (row['max_af']*factor)
            p2 = Rectangle((row['start'],y2),row['width'],0.01, color='red')
            patches.append(p2)
            y3 = kaviar_ybase[chrom] + (row['min_af']*factor) + 0.1
            p3 = Rectangle((row['start'],y3),row['width'],0.01, color='blue')
            patches.append(p3)
            y1 = kaviar_ybase[chrom] + (row['avg']*factor) + 0.1
            p = Rectangle((row['start'],y1),row['width'],0.01, color='green')
            patches.append(p)
        pc= PatchCollection(patches, match_original=True, **kwargs)
        yield pc
    if del_width:
        del df['width']


# Height of each ideogram
chrom_height = 1

# Spacing between consecutive ideograms
chrom_spacing = 2

# Height of the gene track. Should be smaller than `chrom_spacing` in order to
# fit correctly
gene_height = 0.4

# Padding between the top of a gene track and its corresponding ideogram
gene_padding = 0.1

# Width, height (in inches)
figsize = (8, 4)

# Decide which chromosomes to use
chromosome_list = ['chr%s' % i for i in range(1, 23) + ['M', 'X', 'Y']]
#chromosome_list = ['chr8']

# Keep track of the y positions for ideograms and genes for each chromosome,
# and the center of each ideogram (which is where we'll put the ytick labels)
ybase = 0
chrom_ybase = {}
gene_ybase = {}
kaviar_ybase = {}
chrom_centers = {}

# Iterate in reverse so that items in the beginning of `chromosome_list` will
# appear at the top of the plot
for chrom in chromosome_list[::-1]:
    chrom_ybase[chrom] = ybase
    chrom_centers[chrom] = ybase + chrom_height / 2.
    gene_ybase[chrom] = ybase - gene_height - gene_padding
    kaviar_ybase[chrom] = ybase - gene_height*2 - gene_padding*2
    ybase += chrom_height + chrom_spacing

# Read in ideogram.txt, downloaded from UCSC Table Browser
ideo = pd.read_table(
    'ideogram.txt',
    skiprows=1,
    names=['chrom', 'start', 'end', 'name', 'gieStain']
)

# Filter out chromosomes not in our list
ideo = ideo[ideo.chrom.apply(lambda x: x in chromosome_list)]

# Add a new column for width
ideo['width'] = ideo.end - ideo.start

# Colors for different chromosome stains
color_lookup = {
    'gneg': (1., 1., 1.),
    'gpos25': (.6, .6, .6),
    'gpos50': (.4, .4, .4),
    'gpos75': (.2, .2, .2),
    'gpos100': (0., 0., 0.),
    'acen': (.8, .4, .4),
    'gvar': (.8, .8, .8),
    'stalk': (.9, .9, .9),
}

# Add a new column for colors
ideo['colors'] = ideo['gieStain'].apply(lambda x: color_lookup[x])


# Same thing for genes
genes = pd.read_table(
    'ucsc_genes.txt',
    names=['chrom', 'start', 'end', 'name'],
    usecols=range(4))
genes = genes[genes.chrom.apply(lambda x: x in chromosome_list)]
genes['width'] = genes.end - genes.start
genes['colors'] = '#2243a8'

fig = plt.figure(figsize=figsize)
ax = fig.add_subplot(111)

# Now all we have to do is call our function for the ideogram data...
print("adding ideograms...")
for collection in chromosome_collections(ideo, chrom_ybase, chrom_height):
    ax.add_collection(collection)

# ...and the gene data
print("adding genes...")
for collection in chromosome_collections(
    genes, gene_ybase, gene_height, alpha=0.5, linewidths=0
):
    ax.add_collection(collection)

print("adding kaviar...")
for collection in kaviar_collections(
    binned_kaviar, kaviar_ybase, gene_height, alpha=0.5
):
    ax.add_collection(collection)
print("finished adding kaviar")

# Axes tweaking
ax.set_yticks([chrom_centers[i] for i in chromosome_list])
ax.set_yticklabels(chromosome_list)
ax.axis('tight')
plt.show()
