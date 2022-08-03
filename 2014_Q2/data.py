import numpy as np
import pandas as pd
import re
import glob

files = glob.glob("*.csv")

As = np.array([])
Bs = np.array([])

for file in files:
	csvfile_1 = pd.read_csv(file,delimiter=',', header=0)     #read the dataset in a dataframe using pandas

	a = csvfile_1['failure'].sum()
	b = csvfile_1['failure'].count()

	As = np.append(As, a)
	Bs = np.append(Bs, b)

	print (a)            #filename['column_name'].sum ()  :  sum of a certain column
	print (b)          #filename['column_name'].count ()  :  count of a certain column
                         #using filename['column_name'].S() : we can replace 'S' with median, std, mean and ....

#print (csvfile_1.loc[:, ['date', 'failure']])    #filename.loc : show a certain column or row by choosing their name

#print (csvfile_1.sum (axis = 0))


np.savetxt('dataAB.csv',np.array([As,Bs]).T,fmt='%.18e', delimiter = ',')


#np.savetxt("dataAB.csv", np.array([As, Bs]).T)
#print (csvfile_1['date'])     # show a column by write the column's name
#print (csvfile_1.describe())    # filename.describe() :show the summary of statistics (count, mean, std, min, max , ....)
#print (csvfile_1.iloc [:,0:5])          # filename.iloc : show a certain column or row by choosing their column or row number 
