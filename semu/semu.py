""" SEMU

It is slow emulator.  
"""

import argparse

# dummy --
class SysEmu(object):
	def __init__(self, args):
		print("sysemu")
class UsrEmu(object):
	def __init__(self, args):
		print("usremu")
# -- dummy

class Semu(object):
	""" Semu class
	
	main class of starting SEMU
	"""
	def __init__(self, args):
		self.args = args
	
	def run(self):
		if self.args.debug:
			print "*" * 10
			print "debug mode"
			print "*" * 10
		if self.args.system:
			obj = SysEmu(self.args)
		elif self.args.user:
			obj = UsrEmu(self.args)



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="SEMU is slow emulator")
	parser.add_argument("--debug", action='store_true', default=False, help="for debug mode")
	parser.add_argument("--version", action='version', version='%(prog)s 0.1')
	parser.add_argument("--system", action='store_true', default=False, help="system emulation mode")
	parser.add_argument("--user", action='store_true', default=False, help="user space emulation mode")
	parser.add_argument("-m", "--memory", action='store', default=None, type=int, help="memory size")
	args = parser.parse_args()
	semu = Semu(args)
	semu.run()


