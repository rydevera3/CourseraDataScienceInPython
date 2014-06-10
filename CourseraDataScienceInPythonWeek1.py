"""
Created on Mon Jun  9 17:42:06 2014

@author: Ryan de Vera
Codes for Coursera's Data Science Track in Python
"""

""" Given a list in Python x=[3,5,1,10,6,2] what code will set the elements less
or equal to 6 equal to zero """

""" For this a list comprehension can be used """
x=[3,5,1,10,12,6]
y=[0 if i<=6 else i for i in x]

""" Will return y = [0,0,0,10,12,0] """

""" Import csv file to Data Frame """

import pandas as pd
t = pd.read_csv("hw1_data.csv")

" To Show the First 2 rows "
t.head(2)
" To find the number of rows in the data frame "
count = len(t.index)
" To view the last 2 rows of the data frame "
t.tail(2)

"Extract the 47th element from the Ozone column"
l = t["Ozone"][47]
print l

"Find the number of missing values in Ozone Column"
import numpy as np
print len(t["Ozone"].index[t["Ozone"].apply(np.isnan)])

""" Find the mean of the Ozone column with the missing values removed """
l = t["Ozone"]
l = l[~np.isnan(l)]
print np.mean(l)

""" np.isnan(x) will give true if the value in a Nan ~ gives the opposite """

""" Extract the data that has Ozone>31 and Temp>90 and find the mean value of
Solar.R for this data """

ndata = t[np.logical_and(t["Ozone"]>31,t["temp"]>90)]
print np.mean(ndata["Solar.R"])

""" Note: the logical operators & and "and" will not work it will produce an error
"The truth value of an array with more than one element is ambiguous. Use a.any() 
or a.all()" which is an error that occurs when trying to compare expression involving
numpy arrays. For more details see 
"http://stackoverflow.com/questions/12647471/the-truth-value-of-an-array-with-more-than-one-element-is-ambigous-when-trying-t" """

""" Find the mean value of Temp in the Month of June (MOnth=6) """
print(np.mean(t["Temp"][t["Month"]==6]))

""" Find the max value in Ozone when the month is May (Month==5) """
np.max(t["Ozone"][t["Month"]==5])



