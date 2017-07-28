def start_response(status, response_headers, exc_info=None):
	if exc_info:
		try:
			# do stuff w/exc_info here
			# 在这里做事情（东西）w/exc_info
		finally:
			exc_info = None # Avoid circular ref 避免循环引用
