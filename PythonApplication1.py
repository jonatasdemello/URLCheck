import csv
import requests
import sys
import traceback

fileout = 'out.csv'

def checkURL( url ):
	try:
		# r = requests.get('https://api.github.com', auth=('user', 'pass'))
		#r = requests.get('http://www.google.com')
		#print r.status_code
		#print r.headers['content-type']
		r = requests.get(url, timeout=30)
		return r.status_code
	except:
		return ''.join(traceback.format_stack())
        #return sys.exc_info()[0]

#filename = "OccLinkCL"
#filename = "OccLinkPR1"
filename = "OccLinkBR1"
#filename = "OccLinkEC1"
#filename = "OccLinkMX1"

with open(filename +'.csv','rb') as file:
    contents = csv.reader(file)
    matrix = list()
    for row in contents:
        matrix.append(row)

#And then access F13 with matrix[5][12].
#print len(matrix)

#for n in range(1, 5):
for n in range(1, len(matrix)):
	#print matrix[n][4]
	print matrix[n][0]
	result = checkURL(matrix[n][4])
	matrix[n][6] = result

resultFile = open(filename +'_out.csv', 'wb')

wr = csv.writer(resultFile, dialect='excel')
#wr.writerows(lines)

wr.writerows(matrix)