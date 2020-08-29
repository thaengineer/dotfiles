#!/usr/bin/env python
import sys
import subprocess as s
import random as r
from os import listdir, path

# 'sudo openvpn /etc/openvpn/ovpn_udp/us4506.nordvpn.com.udp.ovpn'
def openvpn_status():
	try:
		pid = s.check_output('pgrep -x openvpn', shell=True).decode().strip('\n')
	except s.CalledProcessError:
		pid = ''

	if pid != '':
		print(f'')
	else:
		print(f'')


def openvpn_toggle():
	ovpn_dir = '/etc/openvpn/ovpn_udp'
	ovpn_files = [ovpn for ovpn in listdir(ovpn_dir)]
	ovpn_file = path.join(ovpn_dir, r.choice(ovpn_files))

	try:
		pid = s.check_output('pgrep -x openvpn', shell=True).decode().strip('\n')
	except s.CalledProcessError:
		pid = ''

	if pid != '':
		s.call(f'sudo kill -9 {pid}', shell=True)
	else:
		try:
			s.call(f'sudo openvpn {ovpn_file} &', shell=True)
		except KeyboardInterrupt:
			pass


def main():
	try:
		if sys.argv[1] == '--toggle':
			openvpn_toggle()
		else:
			openvpn_status()
	except:
		openvpn_status()


if __name__ == '__main__':
	main()
