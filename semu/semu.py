""" SEMU

It is slow emulator.  
"""

import argparse

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


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="SEMU is slow emulator")
	parser.add_argument("--debug", action='store_true', default=False, help="for debug mode")
	parser.add_argument("--version", action='version', version='%(prog)s 0.1')
	args = parser.parse_args()
	semu = Semu(args)
	semu.run()


