import numpy as np
import pandas as pd
import re
import glob

files = glob.glob("*.csv")

#A_0 = np.array([])
#B_0 = np.array([])

A_1 = np.array([])
B_1 = np.array([])
A_2 = np.array([])
B_2 = np.array([])
A_3 = np.array([])
B_3 = np.array([])
A_4 = np.array([])
B_4 = np.array([])
A_5 = np.array([])
B_5 = np.array([])
A_6 = np.array([])
B_6 = np.array([])
A_7 = np.array([])
B_7 = np.array([])
A_8 = np.array([])
B_8 = np.array([])
A_9 = np.array([])
B_9 = np.array([])
A_10 = np.array([])
B_10 = np.array([])
A_11 = np.array([])
B_11 = np.array([])
A_12 = np.array([])
B_12 = np.array([])
A_13 = np.array([])
B_13 = np.array([])
A_14 = np.array([])
B_14 = np.array([])
A_15 = np.array([])
B_15 = np.array([])
for file in files:
	print(file)
	csvfile_1 = pd.read_csv(file,delimiter=',', header=0)     #read the dataset in a dataframe using pandas

	HGST_HMS5C4040ALE640 = csvfile_1[csvfile_1['model'] == 'HGST HMS5C4040ALE640']
	HGST_HMS5C4040BLE640 = csvfile_1[csvfile_1['model'] == 'HGST HMS5C4040BLE640']
	Hitachi_HDS5C4040ALE630 = csvfile_1[csvfile_1['model'] == 'Hitachi HDS5C4040ALE630']
	ST4000DM000 = csvfile_1[csvfile_1['model'] == 'ST4000DM000']
	ST6000DX000 = csvfile_1[csvfile_1['model'] == 'ST6000DX000']
	TOSHIBA_MD04ABA400V = csvfile_1[csvfile_1['model'] == 'TOSHIBA MD04ABA400V']
	TOSHIBA_MD04ABA500V = csvfile_1[csvfile_1['model'] == 'TOSHIBA MD04ABA500V']
	WDC_WD60EFRX = csvfile_1[csvfile_1['model'] == 'WDC WD60EFRX']
	HGST_HUH728080ALE600 = csvfile_1[csvfile_1['model'] == 'HGST HUH728080ALE600']
	ST8000DM002 = csvfile_1[csvfile_1['model'] == 'ST8000DM002']
	ST8000NM0055 = csvfile_1[csvfile_1['model'] == 'ST8000NM0055']
	ST10000NM0086 = csvfile_1[csvfile_1['model'] == 'ST10000NM0086']
	ST12000NM0007 = csvfile_1[csvfile_1['model'] == 'ST12000NM0007']
	WDC_WD30EFRX = csvfile_1[csvfile_1['model'] == 'WDC WD30EFRX']
	WDC_WD40EFRX = csvfile_1[csvfile_1['model'] == 'WDC WD40EFRX']


#	a_0 = csvfile_1['failure'].sum()
#	b_0 = csvfile_1['failure'].count()

	a_1 = HGST_HMS5C4040ALE640['failure'].sum()
	b_1 = HGST_HMS5C4040ALE640['failure'].count()
	a_2 = HGST_HMS5C4040BLE640['failure'].sum()
	b_2 = HGST_HMS5C4040BLE640['failure'].count()
	a_3 = Hitachi_HDS5C4040ALE630['failure'].sum()
	b_3 = Hitachi_HDS5C4040ALE630['failure'].count()
	a_4 = ST4000DM000['failure'].sum()
	b_4 = ST4000DM000['failure'].count()
	a_5 = ST6000DX000['failure'].sum()
	b_5 = ST6000DX000['failure'].count()
	a_6 = TOSHIBA_MD04ABA400V['failure'].sum()
	b_6 = TOSHIBA_MD04ABA400V['failure'].count()
	a_7 = TOSHIBA_MD04ABA500V['failure'].sum()
	b_7 = TOSHIBA_MD04ABA500V['failure'].count()
	a_8 = WDC_WD60EFRX['failure'].sum()
	b_8 = WDC_WD60EFRX['failure'].count()
	a_9 = HGST_HUH728080ALE600['failure'].sum()
	b_9 = HGST_HUH728080ALE600['failure'].count()
	a_10 = ST8000DM002['failure'].sum()
	b_10 = ST8000DM002['failure'].count()
	a_11 = ST8000NM0055['failure'].sum()
	b_11 = ST8000NM0055['failure'].count()
	a_12 = ST10000NM0086['failure'].sum()
	b_12 = ST10000NM0086['failure'].count()
	a_13 = ST12000NM0007['failure'].sum()
	b_13 = ST12000NM0007['failure'].count()
	a_14 = WDC_WD30EFRX['failure'].sum()
	b_14 = WDC_WD30EFRX['failure'].count()
	a_15 = WDC_WD40EFRX['failure'].sum()
	b_15 = WDC_WD40EFRX['failure'].count()

#	A_0 = np.append(A_0, a_0)
#	B_0 = np.append(B_0, b_0)

	A_1 = np.append(A_1, a_1)
	B_1 = np.append(B_1, b_1)
	A_2 = np.append(A_2, a_2)
	B_2 = np.append(B_2, b_2)
	A_3 = np.append(A_3, a_3)
	B_3 = np.append(B_3, b_3)
	A_4 = np.append(A_4, a_4)
	B_4 = np.append(B_4, b_4)
	A_5 = np.append(A_5, a_5)
	B_5 = np.append(B_5, b_5)
	A_6 = np.append(A_6, a_6)
	B_6 = np.append(B_6, b_6)
	A_7 = np.append(A_7, a_7)
	B_7 = np.append(B_7, b_7)
	A_8 = np.append(A_8, a_8)
	B_8 = np.append(B_8, b_8)
	A_9 = np.append(A_9, a_9)
	B_9 = np.append(B_9, b_9)
	A_10 = np.append(A_10, a_10)
	B_10 = np.append(B_10, b_10)
	A_11 = np.append(A_11, a_11)
	B_11 = np.append(B_11, b_11)
	A_12 = np.append(A_12, a_12)
	B_12 = np.append(B_12, b_12)
	A_13 = np.append(A_13, a_13)
	B_13 = np.append(B_13, b_13)
	A_14 = np.append(A_14, a_14)
	B_14 = np.append(B_14, b_14)
	A_15 = np.append(A_15, a_15)
	B_15 = np.append(B_15, b_15)
#	print (a_1)            #filename['column_name'].sum ()  :  sum of a certain column
#	print (b_1)          #filename['column_name'].count ()  :  count of a certain column
#	print (a_2)
#	print (b_2)
                         #using filename['column_name'].S() : we can replace 'S' with median, std, mean and ....

#print (csvfile_1.loc[:, ['date', 'failure']])    #filename.loc : show a certain column or row by choosing their name

#print (csvfile_1.sum (axis = 0))

#np.savetxt('AlldataAB.txt',np.array([A_0,B_0]).T,fmt='%.18e', delimiter = ',')
np.savetxt('1-HGST HMS5C4040ALE640.csv',np.array([A_1,B_1]).T,fmt='%.18e', delimiter = ',')
np.savetxt('2-HGST HMS5C4040BLE640.csv',np.array([A_2,B_2]).T,fmt='%.18e', delimiter = ',')
np.savetxt('3-Hitachi HDS5C4040ALE630.csv',np.array([A_3,B_3]).T,fmt='%.18e', delimiter = ',')
np.savetxt('4-ST4000DM000.csv',np.array([A_4,B_4]).T,fmt='%.18e', delimiter = ',')
np.savetxt('5-ST6000DX000.csv',np.array([A_5,B_5]).T,fmt='%.18e', delimiter = ',')
np.savetxt('6-TOSHIBA MD04ABA400V.csv',np.array([A_6,B_6]).T,fmt='%.18e', delimiter = ',')
np.savetxt('7-TOSHIBA MD04ABA500V.csv',np.array([A_7,B_7]).T,fmt='%.18e', delimiter = ',')
np.savetxt('8-WDC WD60EFRX.csv',np.array([A_8,B_8]).T,fmt='%.18e', delimiter = ',')
np.savetxt('9-HGST HUH728080ALE600.csv',np.array([A_9,B_9]).T,fmt='%.18e', delimiter = ',')
np.savetxt('10-ST8000DM002.csv',np.array([A_10,B_10]).T,fmt='%.18e', delimiter = ',')
np.savetxt('11-ST8000NM0055.csv',np.array([A_11,B_11]).T,fmt='%.18e', delimiter = ',')
np.savetxt('12-ST10000NM0086.csv',np.array([A_12,B_12]).T,fmt='%.18e', delimiter = ',')
np.savetxt('13-ST12000NM0007.csv',np.array([A_13,B_13]).T,fmt='%.18e', delimiter = ',')
np.savetxt('14-WDC WD30EFRX.csv',np.array([A_14,B_14]).T,fmt='%.18e', delimiter = ',')
np.savetxt('15-WDC WD40EFRX.csv',np.array([A_15,B_15]).T,fmt='%.18e', delimiter = ',')


#print (csvfile_1['date'])     # show a column by write the column's name
#print (csvfile_1.describe())    # filename.describe() :show the summary of statistics (count, mean, std, min, max , ....)
#print (csvfile_1.iloc [:,0:5])          # filename.iloc : show a certain column or row by choosing their column or row number 
