if 'wsgi.file_wrapper' in environ:
	return environ['wsgi.file_wrapper'](filelike, block_size)
else:
	return iter(lambda: filelike.read(block_size), '')


