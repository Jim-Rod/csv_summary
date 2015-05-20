'''
20140213

Import CSV Data - Dict
Save as JASON?
Basic Stats
Save to file
Find Key Words
Generate Reports...
Generate Plots

'''
import csv
import numpy as np
import matplotlib as mpl
from scipy.stats import nanmean



filename = '20140211_ING.csv'



###____________ Helper ___________###

def number_fields(data):
    '''gets numeric fields from loaded csv data'''
    names = data.dtype.names
    dtypes = data.dtype
    NUM_FIELDS = []
    for i in range(len(names)):
        if ('float' in str(dtypes[i])) or ('int' in str(dtypes[i])):
            NUM_FIELDS.append(str(names[i]))
    return NUM_FIELDS

            
def string_fields(data):
    '''gets text fields from loaded csv data'''
    names = data.dtype.names
    dtypes = data.dtype
    STRING_FIELDS = []
    for i in range(len(names)):
        if 'S' in str(dtypes[i]):
            STRING_FIELDS.append(str(names[i]))
    return STRING_FIELDS
    
def count_vals(array):
    vals = len(array)
    for i in array:
        if np.isnan(i):
            vals = vals - 1
    return vals 

def number_summary(data, num_fields):
    '''take data and numeric feilds and do stuff'''
    sum_dict = {}
    for i in num_fields:
        sum_dict[i] = {}
        sum_dict[i]['Mean'] = nanmean(data[i])
        sum_dict[i]['#Values'] = count_vals(data[i])
        sum_dict[i]['Max'] = np.nanmax(data[i])
        sum_dict[i]['Min'] = np.nanmin(data[i])
    return sum_dict


    
  
###________ reports _________###

def basic_report(filename):
    '''prints summary report form file'''
    data = np.recfromcsv(filename)
    NUM_COL = len(data.dtype.names)
    NUM_ROW = len(data)
    NAMES = data.dtype.names
    DTYPES = data.dtype
    print('--------------------')
    print('---- CSV REPORT ----')
    print('--------------------')
    print('')
    print('Filename: \t %s' % filename)
    print('')
    print('# records: \t %s' % NUM_ROW)
    print('# columns: \t %s' % NUM_COL)
    print('')
    print('--------------------')
    print('- name     -     data type ')
    for i in range(len(NAMES)):
        print('-- %s \t %s --' % (NAMES[i], DTYPES[i]))
    print('--------------------')
        
                   
def numeric_report(filename):
    data = np.recfromcsv(filename)
    fields = number_fields(data)
    d = number_summary(data, fields)
    print('------------------------')
    print('---- NUMERIC REPORT ----')
    print('------------------------')
    print('')
    print('Filename: \t %s' % filename)
    print('')
    print('--------------------')
    for i in fields:
        print('FIELD: \t\t %s' % i)
        print('#Values: \t %s' % d[i]['#Values'])
        print('Max: \t\t %s' % d[i]['Max'])
        print('Min: \t\t %s' % d[i]['Min'])
        print('Mean: \t\t %s' % round(d[i]['Mean'], 2))
        print('--------------------')
        print('')


###________ main _________###

def main(filename):
    basic_report(filename)
    print("")
    numeric_report(filename)

main(filename)



