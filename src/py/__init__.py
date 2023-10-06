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

	fname = os.path.join(
		os.path.dirname(__file__),
		'user_files',
		datetime.datetime.now().strftime('anki-%Y%m%d-%H%M%S.log')
	)
	os.makedirs(os.path.dirname(fname), exist_ok=True)
	fh = open(fname, "w")
	sys.stdout = Logger(sys.stdout, fh)
	sys.stderr = Logger(sys.stderr, fh)

if strvercmp(VER, get_version()) > 0:
	set_version(VER)

init()