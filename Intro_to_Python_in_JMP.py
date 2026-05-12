# tutorial from https://community.jmp.com/t5/JMPer-Cable/Getting-started-with-Python-integration-in-JMP-18/ba-p/768700
import jmputils

# list packages installed
jmputils.jpip('list')

#install a new package through jpip
jmputils.jpip('install', 'pandas')

#update jpip
jmputils.jpip('install --upgrade', 'pip setuptools')

#run JSL in a Python script
import jmp

#the jmp.run_jsl() function encloses the .jsl in triple apostrophes

jmp.run_jsl(
	'''
	//this is a JSL comment
	open()
	'''
)

#Sending a data table from python to JMP
import pandas as pd

#MPC62.csv is saved in the same folder as this script
#this file comes from  NIST Engineering Statistics Handbook, accessed January 30, 2026, https://www.itl.nist.gov/div898/handbook/prc/section2/prc263.htm
pd_dt=pd.read_csv("MPC62.csv")
print(pd_dt.head())

#Python Get() is the JMP function to get an object from Python and import it to JMP

jmp.run_jsl(
	'''
	jmp_dt = Python Get(pd_dt);
	'''
)

#use the jmp.DataTable() function
print(pd_dt.columns)
jmp_dt=jmp.DataTable("Data Table created with Python", len(pd_dt))


#jmp_dt.new_column(pd_dt.columns[0],jmp.DataType.Character)
#jmp_dt[0]=pd_dt[pd_dt.columns[0]].astype(str)

#adding all columns
for i in range(len(pd_dt.columns)):
	jmp_dt.new_column(pd_dt.columns[i],jmp.DataType.Character)
	jmp_dt[i]=pd_dt[pd_dt.columns[i]].astype(str)
