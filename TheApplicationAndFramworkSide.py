def simple_app(environ, start_response):
	"""可能是最简单的application对象"""
	status = '200 OK'
	response_headers = [('Content-type', 'text/plain')] # plain text:纯文本
	start_response(status, response_headers)
	return ['Hello world!\n']

class AppClass:
	"""
	产生相同的输出（和上述的simple_app相比），但是是使用类。
	
	（注意：AppClass就是这里的application，
	所以调用它（即AppClass）时，会返回一个AppClass的实例，
	该实例是可迭代的，会按照规范要求返回application callable的值）

	如果我们想使用AppClass的实例作为application对象，我们要实现一个__call__方法，
	该方法会被调用执行application，并且我们需要创建一个实例供server或者网关使用。
	"""
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response

	def __iter__(self):
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		self.start(status, response_headers)
		yield "Hello world!\n"



