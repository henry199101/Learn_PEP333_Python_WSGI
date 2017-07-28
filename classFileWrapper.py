class FileWrapper:

	def __init__(self, filelike, blksize=8192): # blksize即是block size
		self.filelike = filelike
		self.blksize = blksize
		if hasattr(filelike, 'close'):
			self.close = filelike.close

	def __getitem__(self, key):
		data = self.filelike.read(self.blksize)
		if data:
			return data
		raise IndexError