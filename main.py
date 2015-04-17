#test changes to test git

import csv
import numpy as np


def contextBuilder(spreadSheets,contextFile):
	with open(contextFile, "w") as csv_file:
		for filename in spreadSheets:
			with open(filename,'r') as fileRoot:
				fileRoot = np.array(list(csv.reader(fileRoot, delimiter = '\t')))
				fileRoot = fileRoot.transpose()
				writer = csv.writer(csv_file, delimiter=',')
				for line in fileRoot:
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
							count = -99
							
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

def descriptiveStatus(computeFiftyPercentFile,descriptiveStatusFile):
		with open(computeFiftyPercentFile,'r') as fileRoot:
				fileRoot = np.array(list(csv.reader(fileRoot, delimiter = ',')))
				fileRoot = fileRoot.transpose()	
				fileRoot = np.delete(fileRoot,len(fileRoot)-1,0)	
				xx = fileRoot
				with open(descriptiveStatusFile, "w", newline='') as csv_file:
					writer = csv.writer(csv_file, delimiter=',')
					for line in fileRoot:
						writer.writerow(line)
						#print(line)
					try:
						fileRoot=np.delete(fileRoot,0,axis=0) # removing the header string values conatining 7 level families
						xx = fileRoot.astype(float)
						#print(fileRoot)
						sum = np.sum(xx,axis=0)
						writer.writerow(sum)
						
					except TypeError as detail:
						print('descriptive status error is '+str(detail))
						
					sum = np.sum(xx,axis=0)
					writer.writerow('')
					writer.writerow('')
					for line in xx:
						line = np.divide(line,sum)
						writer.writerow(line)
					writer.writerow('')
					writer.writerow('')
					temp = xx
					count=0
					for line in xx:
						myInt = 100
						line = np.divide(line,sum)
						line = [x * myInt for x in line]
						writer.writerow(line)
						temp[count] = line
						count = count +1
					else:
						xx= temp
						
					#print(xx)
					fileRoot= xx
					diets=retriveDiets(fiftyPercentFile)
					#diets = np.array([['__Free Choice Timothy Hay, No Pellets__',	'__Free Choice Timothy Hay, No Pellets__',	'__Free Choice Timothy Hay, No Pellets__',	'__Free Choice Timothy Hay, No Pellets__',	'__Free Choice Timothy Hay, Test Pellet Diet E__',	'__Free Choice Timothy Hay, Test Pellet Diet E__',	'__Free Choice Timothy Hay, Test Pellet Diet E__',	'__Free Choice Timothy Hay, Test Pellet Diet E__',	'__Free Choice Timothy Hay, Test Pellet Diet P__',	'__Free Choice Timothy Hay, Test Pellet Diet P__',	'__Free Choice Timothy Hay, Test Pellet Diet P__',	'__Free Choice Timothy Hay, Test Pellet Diet P__',	'__Free Choice Timothy Hay, Test Pellet Diet P__',	'__No Hay, Test Pellet Diet E__',	'__No Hay, Test Pellet Diet E__',	'__No Hay, Test Pellet Diet E__',	'__No Hay, Test Pellet Diet E__',	'__No Hay, Test Pellet Diet E__',	'__No Hay, Test Pellet Diet P__',	'__No Hay, Test Pellet Diet P__',	'__No Hay, Test Pellet Diet P__',	'__No Hay, Test Pellet Diet P__',	'__No Hay, Test Pellet Diet P__',	'__No Hay, Test Pellet Diet M__',	'__No Hay, Test Pellet Diet M__',	'__No Hay, Test Pellet Diet M__',	'__No Hay, Test Pellet Diet M__',	'__No Hay, Test Pellet Diet M__']])
					#diets = diets.pop(0)
					del diets[-1]
					del diets[0]
					#diets = diets.pop(len(diets)-1)
					#diets = np.delete(diets,len(diets)-1,0)
					#print(diets)
					diets = np.array([diets])
					uniqueDiets = np.unique(diets)
					#print(unique)
					concatenatedFileRoot=np.concatenate((diets.T,fileRoot),axis=1)
					#print(values.shape)
					#print(fileRoot.shape)
					#print(concatenatedFileRoot.shape)
					#print(concatenatedFileRoot)
					###median = concatenatedFileRoot[concatenatedFileRoot[:,0]=='__Free Choice Timothy Hay, No Pellets__']
					#print(median)
					#median=np.delete(median,0,axis=1) 
					#median = median.astype(float)
					#median = np.median(median,axis=0)
					#print(median)
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
					writer.writerow('')
					writer.writerow('max')
					for diet in uniqueDiets:
						median = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
						dt = np.array(diet)
						xx=np.delete(median,0,axis=1) 
						xx = xx.astype(float)
						xx = np.max(xx,axis=0)
						xx = xx.astype(str)
						xx = np.insert(xx,0,diet)
						writer.writerow(xx)
					writer.writerow('')
					writer.writerow('min')
					#min = concatenatedFileRoot[0:1]
					#min=np.delete(min,0,axis=1)
					count = 0
					for diet in uniqueDiets:
						median = concatenatedFileRoot[concatenatedFileRoot[:,0]==diet]
						dt = np.array(diet)
						xx=np.delete(median,0,axis=1) 
						xx = xx.astype(float)
						xx = np.min(xx,axis=0)
						xx = xx.astype(str)
						
						xx = np.insert(xx,0,diet)
						#min[count] =xx
						#count = count +1
						writer.writerow(xx)
					writer.writerow('')
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
						
						

def retriveDiets(fiftyPercentFile):
	with open(fiftyPercentFile,'r') as dietRoot:
				dietRoot = np.array(list(csv.reader(dietRoot, delimiter = ',')))
				dietRoot = dietRoot[dietRoot[:,0]=='diet'][0].tolist()	
				#print(dietRoot)
				return dietRoot				
						

						
					
					
					



			

if __name__ == "__main__":
	spreadSheets = ["li_bacterial_mapping_L2.txt","li_bacterial_mapping_L3.txt",
	"li_bacterial_mapping_L4.txt","li_bacterial_mapping_L5.txt","li_bacterial_mapping_L6.txt"]
	contextFile = "context.csv"
	fiftyPercentFile = "fifty.csv"
	computeFiftyPercentFile = "computefifty.csv"
	descriptiveStatusFile = "descriptiveStatus.csv"
	contextBuilder(spreadSheets,contextFile)
	retainAboveHalf(contextFile,fiftyPercentFile)
	retainAboveHalfCompute(contextFile,computeFiftyPercentFile)
	descriptiveStatus(computeFiftyPercentFile,descriptiveStatusFile)