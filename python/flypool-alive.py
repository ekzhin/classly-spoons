import urllib2
import json
import time
import datetime
import sys

if (len(sys.argv) < 3):
	print "Usage: python flypool-up.py [interval seconds] [logging y/n]"
	sys.exit(1)

url1='https://api-zcash.flypool.org/miner/[ID]/worker/'
url2='/currentStats'

workers=[['msi', 1500, 2200], ['2ndmsi', 1200, 1900], ['3rdmsi', 800, 1300], ['aero3x1080ti', 1200, 1800], ['980m', 100, 240]]

while 1:
	if (sys.argv[2] == 'y'):
		f1 = open("flypool-up.txt", "a")
		f1.write("="*50+"\r\n")
	print "="*50+"\r\n"
	total = 0
	for i in range(0,5): 
		try:
			req = urllib2.Request(url1+workers[i][0]+url2, headers={'User-Agent':'Mozilla/5.0'})
			res = urllib2.urlopen(req)
			data = res.read()
			a = datetime.datetime.now()

			p = lambda:None
			p.__dict__ = json.loads(data)

			data2 = str(p.data).replace('u\'','"')
			data2 = data2.replace('\'','"')

			q = lambda:None
			q.__dict__ = json.loads(data2)

			temp = q.currentHashrate
			total += temp
			print str(a) + " " + workers[i][0] + ": " + str(temp) + "H/s (reported " + str(workers[i][2])+")\r\n"
			if temp < workers[i][1]:
				for x in range(1,11):
					print '\7'
					print workers[i][0] + " worker may be down!\r\n"
					time.sleep(1)
			if (sys.argv[2] == 'yes'):
				f1.write("Time: " + str(a) + " " + workers[i][0] + " worker: " + str(temp) + "H/s\r\n")
		except:
			continue
	print "Total hashrate: " + str(total) + "Sols/sec\r\n"
	if (sys.argv[2] == 'yes'):
		f1.close()
	time.sleep(float(sys.argv[1]))
