#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:27:24 2021

@author: schorb
"""

import numpy as np
import pyEM as em

#import pybdv
from pybdv import transformations as tf
import mrcfile as mrc
import glob
import re
import sys
import os

import time
import shutil

from skimage import io

import bdv_tools as bdv


cluster = True


bdv_unit = 'um'
zstretch = 1
timept = 0

submit_interval = 2 # time to wait between submitting jobs to not overload the group share IO
blocksize = 8
break_interval = 30


outformat='.n5'

chunks = list((32,192,192))
downscale_factors = list(([1,2,2],[1,2,2],[1,2,2],[1,2,2],[1,4,4]))

indir = '/g/schwab/Tobias/Tomography/joined/'
suffix = sys.argv[1]


indir = os.path.join(indir,suffix)

fileslist = os.path.join('/g/schwab/Tobias/MoBIE/',suffix+'_joinfiles.txt')

outdir = os.path.join('/g/schwab/Tobias/MoBIE/data/tomo/images/bdv-n5',suffix)



with open(fileslist,'r') as f:
    joinlist=f.read().splitlines()



if not os.path.exists(outdir):
    os.makedirs(outdir)

idx = 0

for file in joinlist:
    file_comp = file.split('_')
    file =os.path.join(indir,file_comp[0],file_comp[1]+'.join')
    
    base = os.path.splitext(file.split(indir)[1])[0]
        
    outfile = os.path.join(outdir,re.sub('/','_',base))+outformat
    
    if os.path.exists(os.path.join(outdir,re.sub('/','_',base)+'.xml')):
        print('Skipping '+base+'. It already exists.')
        continue

    if os.path.exists(outfile):
        print('re-doing '+base+'.')
        shutil.rmtree(outfile)
        #continue
    idx += 1
    
    if idx%blocksize == 0:
        time.sleep(break_interval)
    else:
        time.sleep(submit_interval)

    print('converting '+base+' into BDV format.')
    
    # get pixel size

    mfile = mrc.mmap(file,permissive = 'True')
    tomopx = mfile.voxel_size.x / 10000 # in um
    del(mfile)
    mat=np.eye(4)*tomopx
    mat[2,2] = tomopx*zstretch
    mat[3,3] = 1
    
    tf_tr = tf.matrix_to_transformation(mat).tolist()

    setup_id = 0

    view=dict()

    view['resolution'] = [tomopx,tomopx,tomopx*zstretch]
    view['setup_id'] = setup_id
    view['setup_name'] = os.path.basename(base)

    view['OriginalFile'] = file

    view['trafo'] = dict()
    view['trafo']['Scaling'] = tf_tr

    view['attributes'] = dict()

    # view['attributes']['displaysettings'] = dict({'id':setup_id,'color':bdv.colors['W'],'isset':'true'})
    # view['attributes']['displaysettings']['Projection_Mode'] = 'Average'

    # data = mfile.data


    # # check if volume is rotated
    # if data.shape[0]/data.shape[1]>5:
    #     data = np.swapaxes(data,0,1)

    # data0 = np.swapaxes(data,0,2)
    # data1 = np.fliplr(data0)
    # data2 = np.swapaxes(data1,0,2)

   # print(outfile)
    
    
    bdv.write_bdv(outfile,file,view,outf='.n5',blow_2d=zstretch,downscale_factors=downscale_factors,cluster=cluster,infile=file,chunks=chunks)
    del(view)
