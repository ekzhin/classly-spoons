import urllib2
import json
import time
import datetime
import sys

if (len(sys.argv) < 3):
	print "Usage: python nanopool-up.py [interval seconds] [logging y/n]"
	sys.exit(1)

url='https://api.nanopool.org/v1/eth/reportedhashrate/[ID]/'

workers=[['MSIx', 20], ['2ndMSI', 70], ['DS', 50], ['1060', 18]]

while 1:
	if (sys.argv[2] == 'y'):
		f1 = open("nanopool-up.txt", "a")
		f1.write("="*50+"\r\n")
	print "="*50+"\r\n"
	total = 0
	for i in range(0,4): 
		try:
			req = urllib2.Request(url+workers[i][0], headers={'User-Agent':'Mozilla/5.0'})
			res = urllib2.urlopen(req)
			data = res.read()
			a = datetime.datetime.now()

			p = lambda:None
			p.__dict__ = json.loads(data)

			temp = p.data
			total += temp
			print str(a) + " " + workers[i][0] + " worker current hashrate: " + str(temp) + "MH/s\r\n"
			if temp < workers[i][1]:
				for x in range(1,11):
					print '\7'
					print workers[i][0] + " worker may be down!\r\n"
					time.sleep(1)
			if (sys.argv[2] == 'yes'):
				f1.write("Time: " + str(a) + " " + workers[i][0] + " worker: " + str(temp) + "MH/s\r\n")
		except:
			continue
	print "Total hashrate: " + str(total) + "MH/sec\r\n"
	if (sys.argv[2] == 'yes'):
		f1.close()
	time.sleep(float(sys.argv[1]))
