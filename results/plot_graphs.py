__author__ = 'oliver'


import matplotlib
matplotlib.use('Agg') # Or any other X11 back-end


import numpy as np
import matplotlib.pyplot as pyplot
import pickle
import sys
import math
from numpy import genfromtxt

# First arg is file to de-pickle, second arg is "isTest"
work_dir = 'results/'
def main(argv):
    for filename in argv:

        data = genfromtxt(work_dir+filename,delimiter=',')

        if data.shape[0] >1:
            fig = pyplot.figure(figsize=(6, 6))
            axes = pyplot.gca()
            pyplot.grid()
            axes.set_ylim([0, data[:,4].max()])
            axes.set_xlim([0, data[:,0].max()])
            pyplot.xlabel('Epochs')
            pyplot.ylabel('Loss')
            pyplot.title('Loss')


            pyplot.plot(data[:,0], data[:,4], linewidth=2, label=filename, color='#FC474C')
            # pyplot.plot(fractions, pdj[:,1], linewidth=2, label='torso', color='#8DE047')
            # pyplot.plot(fractions, pdj[:,2], linewidth=2, label='arms', color='#FFDD50')
            # pyplot.plot(fractions, pdj[:,3], linewidth=2, label='legs', color='#53A3D7')

            pyplot.legend(loc='upper left', shadow=True, fontsize='medium')

            pyplot.savefig(work_dir+'detections')

if __name__=="__main__":
    main(sys.argv[1:])