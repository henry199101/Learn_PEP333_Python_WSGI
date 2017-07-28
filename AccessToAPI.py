environ['wsgi.file_wrapper'] = FileWrapper
result = application(environ, start_response)

try:
	if isinstance(result, FileWrapper):
		# check if result.filelike is usable w/platform-specific
		# API, and if so, use that API to transmi the result.
		# If not, fall through to normal iterable handing
		# loop below.
	
	for data in result:
		# etc.

finally:
	if hasattr(result, 'close'):
		result.close()


