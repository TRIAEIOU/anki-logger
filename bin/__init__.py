import sys, os, datetime
from .ankiutils import *

LBL = "Logger"
VER = "1.0.0"

def init():
	class Logger:
		def __init__(self, std, log):
			self.log = log
			self.std = std
			if getattr(std, 'write', None) is not None:
				self.write = self._write
			if getattr(std, 'flush', None) is not None:
				self.flush = self._flush
			if getattr(std, 'mode', None) is not None:
				self.mode = std.mode
			if getattr(std, 'encoding', None) is not None:
				self.encoding = std.encoding
		
		def _write(self, s):
			self.log.write(s)
			self.std.write(s)

		def _flush(self):
			self.log.flush()
			self.std.flush()

	now = datetime.datetime.now()
	log = open(
		os.path.join(
			os.path.dirname(__file__),
			now.strftime('anki-log-%Y%m%d-%H%M%S.txt')
		), "w"
	)
	print(f"log file: {log}")

	sys.stdout = Logger(sys.stdout, log)
	sys.stderr = Logger(sys.stderr, log)

if strvercmp(VER, get_version()) > 0:
	set_version(VER)

init()