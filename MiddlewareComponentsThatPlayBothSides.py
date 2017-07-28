from piglatin import piglatin

class LatinIter；
	"""
	Transform iterated output to piglatin, if it's okay to do so
	把迭代的输出转换成piglatin格式，如果它可以这么做
	Note that the "okayness" can change until the application yields
	its first non-empty string, so 'transform_ok' has to be a mutable
	truth value.
	注意：当application yields了它的第一个非空字符串时，“可以”可能改变，
	所以transform_ok必须是一个不变的truth值。
	"""

	def __init__(self, result, transform_ok):
		if hasattr(result, 'close'):
			self.close = result.close
		self._next = iter(result).next
		self.transform_ok = transform_ok

	def __iter__(self):
		return self

	def next(self):
		if self.transform_ok:
			return piglatin(self._next())
		else:
			return self._next()

class Latinator:

	# by default, don't transform output
	# 默认不改变输出
	transform = False

	def __init__(self, application):
		self.application = application

	def __call__(self, environ, start_response):
		
		transform_ok = []

		def start_latin(status, response_headers, exc_info=None):

			# Reset ok flag, in case this is a repeat call
			del transform_ok[:]

			for name, value in response_headers:
				if name.lower() == 'content-type' and value == 'text/plain':
					transform_ok.append(True)
					# Strip content-length if present, else it'll be wrong
					response_headers = [(name, value)
						for name, value in response_headers
							if name.lower() != 'content-length'
					]
					break

			write = start_response(satus, response_headers, exc_info)

			if transform_ok:
				def write_latin(data):
					write(piglatin(data))
				return write_latin
			else:
				return write

		return LatinIter(self.application(environ, start_latin), transform_ok)


# Run foo_app under a Latinator's control, using the example CGI gateway
# 在一个Latinator的控制下，运行foo_app，使用这个例子——CGI网关
from foo_app import foo_app
run_with_cgi(Latinator(foo_app))


















