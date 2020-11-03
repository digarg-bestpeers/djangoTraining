# Function based middleware
def my_middleware(get_Response):
	print("One Time Intialization")		# Configration code when url hit first time
	def my_function(request):
		print("This is before view")
		resposne = get_Response(request)
		print("This is after view")
		return resposne
	return my_function


