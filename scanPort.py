#!/usr/bin/python3

from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
	target = input('Enter the host to be scanned: ')
	target_IP = gethostbyname(target)
	print('Starting scan on host: ', target_IP)
	
	for i in range(1, 10000):
		s = socket(AF_INET, SOCK_STREAM)
		conn = s.connect_ex((target_IP, i))
		if(conn == 0):
			print('Port %d: OPEN' %(i, ))
		s.close()
print('Time taken:', time.time() - startTime)