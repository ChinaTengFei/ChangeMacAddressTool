import uuid
import os
import sys

def upDateAddress(upDateAddress):
	os.system('sudo /sbin/ifconfig enp0s31f6 down')

	os.system('sudo ifconfig enp0s31f6 hw ether '+upDateAddress)

	os.system('sudo /sbin/ifconfig enp0s31f6 up')

def checkValue(value):
	if len(value) != 2:
		return False

	try:
		int(value, 16)
	except:
		return False
	return True

mac=open("/sys/class/net/enp0s31f6/address").read();
pyMac=mac.replace(':','').upper()[0:-1]
print('init macAddress:'+pyMac)
inputMac = 'TT'
print len(sys.argv)
if len(sys.argv)==2:
	inputMac = sys.argv[1]
elif not checkValue(inputMac):
	inputMac = raw_input()

if not checkValue(inputMac):
	exit(0)
# F 4 : 8 E : 3 8 : A 0 : D 1 : 4 F
newMac = (str((hex(int(pyMac,16)+1)))[2:-2] +inputMac).upper()

print('new PymacAddress:'+newMac)
localMac=''
#x for index,x in enumerate(newMac) if x%2==0

for index,x in enumerate(newMac):
	print x,
	localMac+=x
	if((index+1)%2==0 and index!=len(newMac)-1):
		print':',
		localMac+=':'

print
upDateAddress(localMac)
print 'localMac'+localMac

