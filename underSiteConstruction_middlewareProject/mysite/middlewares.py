from django.http import HttpResponse
from django.shortcuts import render

class UnderConstructionMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		print("Call From Middleware before View")
		# response = self.get_response(request)
		# response = HttpResponse("This is under construction")
		response = render(request, "mysite/siteuc.html")
		print("call From Middleware after View")
		return response