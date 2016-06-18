from cpu.Cpu import Cpu

class Soc(object):
	def __init__(self, args):
		self.args = args
		self.cpu = Cpu(args)

	
