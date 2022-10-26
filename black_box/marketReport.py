import os
import numpy as np
import pandas as pd
import calendar
from datetime import datetime
from fpdf import FPDF # used to create PDFs
import shutil

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

# create a PDF page structure
# creates a folder for charts (deletes if its exists and recreates)
# saves data for every time t
# creates a pdf matric from the data_visuals

PLOT_DIR = 'plots'

def construct():
    # Delete folder if it exists and create it again
    try:
        shutil.rmtree(PLOT_DIR)
        os.mkdir(PLOT_DIR)
    except FileNotFoundError:
        os.mkdir(PLOT_DIR)

    # Iterate overall all months in time t

    # construct data shown in document
    counter = 0
    pages_data = []
    temp = []
    n = 3 # number of data_visuals that we want per page
    # get all plots
    files = os.listdir(PLOT_DIR)
    # sot them by metric - a bit tricky because the file names are strings
    files = sorted(os.listdir(PLOT_DIR), key = lambda x: int(x.split('.')[0]))
    #Iterate over all created visualization
    for fname in files:
        #we want n per page
        if counter == n:
            pages_data.append(temp)
            temp = []
            counter = 0

        temp.append(f'{PLOT_DIR}/{fname}')
        counter += 1

    return [*pages_data, temp]