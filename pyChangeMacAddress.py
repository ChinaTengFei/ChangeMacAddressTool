import uuid
import os

def upDateAddress(upDateAddress):
	os.system('sudo /sbin/ifconfig enp0s31f6 down')

	os.system('sudo ifconfig enp0s31f6 hw ether '+upDateAddress)

	os.system('sudo /sbin/ifconfig enp0s31f6 up')
	

mac=open("/sys/class/net/enp0s31f6/address").read();
pyMac=mac.replace(':','').upper()[0:-1]
print('init macAddress:'+pyMac)

newMac = str((hex(int(pyMac,16)+1)).upper())[2:]

print('new PymacAddress:'+newMac)
localMac=''
#x for index,x in enumerate(newMac) if x%2==0

for index,x in enumerate(newMac):
	print x,
	localMac+=x
	if((index+1)%2==0 and index!=len(newMac)-1):
		print':',
		localMac+=':'
upDateAddress(localMac)
print 'localMac'+localMac

