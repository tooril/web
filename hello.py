import urlparse
def app(environ, start_response):
#	for key, value in environ.items():
#		print (key, value)
	q = environ.get("QUERY_STRING")
#	print (q)
	#data = urlparse.parse_qs(q)
	data = ['x=1\r\n','x=2\r\n','y=3\r\n','y=\r\n']
#	for k,v in data.items():
#		print(k,v)
	status = "200 OK"
	headers = [
		('Content-Type','text/plain'),
		('Content-Length', str(len(data)))
	]
	start_response(status,headers)
	return [data]
