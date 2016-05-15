def app(environ, start_response):
#	for key, value in environ.items():
#		print (key, value)
	print (environ.get("QUERY_STRING"))
	data = "Hello, World!\n"
	status = "200 OK"
	headers = [
		('Content-Type','text/plain'),
		('Content-Length', str(len(data)))
	]
	start_response(status,headers)
	return iter([data])
