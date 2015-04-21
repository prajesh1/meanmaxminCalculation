'''
   <Statistical computation for 7 layer of biological data.>
    Copyright (C) <2015>  <Prajesh Ravindran>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
 '''

import csv
import numpy as np


def contextBuilder(spreadSheets,contextFile):
	with open(contextFile, "w") as csv_file:
		for filename in spreadSheets:
			with open(filename,'r') as fileRoot:
				fileRoot = np.array(list(csv.reader(fileRoot, delimiter = '\t')))
				fileRoot = fileRoot.transpose()
				writer = csv.writer(csv_file, delimiter=',')
				for line in fileRoot:              #creates csv context file
					writer.writerow(line)

def retainAboveHalf(contextFile,fiftyPercentFile):
	with open(contextFile,'r') as fileRoot:
				fileRoot = np.array(list(csv.reader(fileRoot, delimiter = ',')))
				for line in fileRoot:
					count = 0
					for i in range(1,len(line)):
						try:
							if(float(line[i])>float(0)):
								count= count+1
						except ValueError as detail:
							count = -99              #for lines without floating values
							
					line.append(count)
				with open(fiftyPercentFile, "w", newline='') as csv_file:
					writer = csv.writer(csv_file, delimiter=',')
					for line in fileRoot:
						if(line[len(line)-1]):
							writer.writerow(line)

def retainAboveHalfCompute(contextFile,computeFiftyPercentFile):
	with open(contextFile,'r') as fileRoot:
				fileRoot = np.array(list(csv.reader(fileRoot, delimiter = ',')))
				for line in fileRoot:
					count = 0
					for i in range(1,len(line)):
						try:
							if(float(line[i])>float(0)):
								count= count+1
						except ValueError as detail:
							pass
							
					line.append(count)
				with open(computeFiftyPercentFile, "w", newline='') as csv_file:
					writer = csv.writer(csv_file, delimiter=',')
					for line in fileRoot:
						if(line[len(line)-1]):
							writer.writerow(line)		

#This function transposes each line from fifty percent file and prints it in descriptive stat file
def printIndividualLine(descriptiveStatFile,computeFiftyPercentFileRoot):
	with open(descriptiveStatFile, "w", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		#print(computeFiftyPercentFileRoot)
		print(descriptiveStatFile)
		
		for line in computeFiftyPercentFileRoot:
			writer.writerow(line)  #print indviudal lines
			
#This function prints the calculates, prints and returns the sum of each column of individual line
def printIndividualLineSum(descriptiveStatFile,computeFiftyPercentFileRoot):
	with open(descriptiveStatFile, "a", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		try:
			
			
			sum = np.sum(computeFiftyPercentFileRoot,axis=0)
			writer.writerow('') #print single blank row
			writer.writerow(sum) #print the sum for each of column of individual line
			return sum
		except TypeError as detail:
				print('descriptive status error is '+str(detail))

def printPercentOfIndividualLine(descriptiveStatFile,computeFiftyPercentFileRoot,IndividualLinesum):
	with open(descriptiveStatFile, "a", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		xx= computeFiftyPercentFileRoot
		writer.writerow('') #print single blank row
		writer.writerow('') #print single blank row
		for line in computeFiftyPercentFileRoot:
						line = np.divide(line,IndividualLinesum)
						writer.writerow(line)
		temp = xx
		count=0
		writer.writerow('')
		writer.writerow('')
		#print(xx)
		for line2 in xx:
						myInt = 100  #multiple each value by 100 to get percent value
						#print("before")
						#print(line2)
						line2 = np.divide(line2,IndividualLinesum)
						#print(line2)
						line2 = [lineval * myInt for lineval in line2]
						writer.writerow(line2)
						temp[count] = line2
						count = count +1
						#else:
						#	xx= temp

def printMedian(descriptiveStatFile,uniqueDiets,concatenatedFileRoot):
	with open(descriptiveStatFile, "a", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow('')
		writer.writerow('median')
		for diet in uniqueDiets:
			median = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
			dt = np.array(diet)
			xx=np.delete(median,0,axis=1) 
			xx = xx.astype(float)
			xx = np.median(xx,axis=0)
			xx = xx.astype(str)
			xx = np.insert(xx,0,diet)
			writer.writerow(xx)	

def printMax(descriptiveStatFile,uniqueDiets,concatenatedFileRoot):
	with open(descriptiveStatFile, "a", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow('')
		writer.writerow('maximum')
		for diet in uniqueDiets:
			maximum = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
			dt = np.array(diet)
			xx=np.delete(maximum,0,axis=1) 
			xx = xx.astype(float)
			xx = np.max(xx,axis=0)
			xx = xx.astype(str)
			xx = np.insert(xx,0,diet)
			writer.writerow(xx)

def printMin(descriptiveStatFile,uniqueDiets,concatenatedFileRoot):
	with open(descriptiveStatFile, "a", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow('')
		writer.writerow('Minimum')
		for diet in uniqueDiets:
			minimum = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
			dt = np.array(diet)
			xx=np.delete(minimum,0,axis=1) 
			xx = xx.astype(float)
			xx = np.min(xx,axis=0)
			xx = xx.astype(str)
			xx = np.insert(xx,0,diet)
			writer.writerow(xx)																											
					
def descriptiveStat(computeFiftyPercentFile,descriptiveStatFile):
		with open(computeFiftyPercentFile,'r') as computeFiftyPercentFileRoot:
				computeFiftyPercentFileRoot = np.array(list(csv.reader(computeFiftyPercentFileRoot, delimiter = ',')))
				computeFiftyPercentFileRoot = computeFiftyPercentFileRoot.transpose()	
				computeFiftyPercentFileRoot = np.delete(computeFiftyPercentFileRoot,len(computeFiftyPercentFileRoot)-1,0)	
				xx = computeFiftyPercentFileRoot
				printIndividualLine(descriptiveStatFile,computeFiftyPercentFileRoot)#prints individual line

				computeFiftyPercentFileRoot=np.delete(computeFiftyPercentFileRoot,0,axis=0) # removing the header string values conatining 7 level families	
				computeFiftyPercentFileRoot = computeFiftyPercentFileRoot.astype(float)
				IndividualLinesum = printIndividualLineSum(descriptiveStatFile,computeFiftyPercentFileRoot) #prints the sum
				
				printPercentOfIndividualLine(descriptiveStatFile,
					computeFiftyPercentFileRoot,IndividualLinesum)
					
				fileRoot= computeFiftyPercentFileRoot
				diets=retriveDiets(fiftyPercentFile)
				del diets[-1]
				del diets[0]
				diets = np.array([diets])
				uniqueDiets = np.unique(diets)
				#print(unique)
				concatenatedFileRoot=np.concatenate((diets.T,fileRoot),axis=1)
				
				printMedian(descriptiveStatFile,uniqueDiets,concatenatedFileRoot)
				
				printMax(descriptiveStatFile,uniqueDiets,concatenatedFileRoot)
				printMin(descriptiveStatFile,uniqueDiets,concatenatedFileRoot)	
				'''
				writer.writerow('rounded')
				for diet in uniqueDiets:
					median = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
					maximum = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
					minimum = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
					dt = np.array(diet)
					#
					median=np.delete(median,0,axis=1) 
					median = median.astype(float)
					median = np.median(median,axis=0)
					median = median.astype(str)
					
					#
					minimum=np.delete(minimum,0,axis=1) 
					minimum = minimum.astype(float)
					min = np.min(minimum,axis=0)
					minimum = minimum.astype(str)
					#
					maximum=np.delete(maximum,0,axis=1) 
					maximum = maximum.astype(float)
					maximum = np.max(maximum,axis=0)
					maximum = maximum.astype(str)
					#median=np.array(median)
					median.round(decimals=2)
					#print(np.around(median,decimals=2))
					print(median)
					'''	
						

def retriveDiets(fiftyPercentFile):
	with open(fiftyPercentFile,'r') as dietRoot:
				dietRoot = np.array(list(csv.reader(dietRoot, delimiter = ',')))
				dietRoot = dietRoot[dietRoot[:,0]=='diet'][0].tolist()	
				#print(dietRoot)
				return dietRoot				
						
if __name__ == "__main__":
	spreadSheets = ["p_bacterial_mapping_L2.txt","p_bacterial_mapping_L3.txt",
	"p_bacterial_mapping_L4.txt","p_bacterial_mapping_L5.txt","p_bacterial_mapping_L6.txt"]
	contextFile = "context.csv"
	fiftyPercentFile = "fifty.csv"
	computeFiftyPercentFile = "computefifty.csv"
	descriptiveStatusFile = "descriptiveStat.csv"
	contextBuilder(spreadSheets,contextFile)
	retainAboveHalf(contextFile,fiftyPercentFile)
	retainAboveHalfCompute(contextFile,computeFiftyPercentFile)
	descriptiveStat(computeFiftyPercentFile,descriptiveStatusFile)
