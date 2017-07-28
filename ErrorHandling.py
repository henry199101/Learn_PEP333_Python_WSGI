try:
	# regular application code here
	status = '200 Froody'
	response_headers = [("content-type", "text/plain")]
	start_response(status, response_headers)
	return ["normal body goes here"]
except:
	# XXX should trap runtime issues likes MemoryError, KeyboardInterrupt
	# XXX应该捕捉（trap）运行环境问题，比如内存错误，键盘妨碍
	# 	in a separate handler before this bare 'except:'...
	status = "500 Oops"
	response_headers = [("content-type", "text/plain")]
	start_response(satus, response_headers, sys.exc_info())
	return ["error body goes here"]