# from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from reports.models import Report
from reports.serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from django.views.generic.base import RedirectView

class JSONResponse(HttpResponse):
	# An HttpResponse that renders its content into JSON.
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

# class ReportsApiView(generics.ListCreateAPIView):
class ReportsApiView(APIView):
	"""
	Return a list of all existing reports.
	"""
	
	queryset = Report.objects.all()
	serializer_class = ReportSerializer

	def get(self, request):
		reports = Report.objects.all()

		# region filtering
		regionParam = request.GET.get('ca')
		if regionParam is not None:
			# reports = reports.filter(ca=regionParam)
			reports = reports.filter(ca__iexact=regionParam.strip()) 

		# date filtering
		dateParam = request.GET.get('date')
		if dateParam is not None:	# exact date filtering
			reports = reports.filter(date=dateParam)
		else:	# range date filtering
			startdate = request.GET.get('startdate')
			enddate = request.GET.get('enddate')
			
			if startdate is not None or enddate is not None: # at least one date range param provided
				if startdate is None:
					startdate = datetime.min
				if enddate is None:
					enddate = datetime.max

				reports = reports.filter(date__range=[startdate, enddate])
		
		data = ReportSerializer(reports, many=True).data
		return Response(data)


"""
# API Services
@csrf_exempt # TODO only POST requires csrf token
def report_list(request):
	# List all code report, or create a new report.

	if request.method == 'GET':
		reports = Report.objects.all()

		regionParam = request.GET.get('ca')
		if regionParam is not None:
			reports = reports.filter(ca=regionParam)

		serializer = ReportSerializer(reports, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ReportSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)
"""

# @csrf_exempt # TODO only POST, PUT and DELETE requires csrf token
def report_detail(request, pk):
	# Retrieve, update or delete a report.

	try:
		report = Report.objects.get(pk=pk)
	except Report.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ReportSerializer(report)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ReportSerializer(report, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		report.delete()
		return HttpResponse(status=204)


class GithubRedirectView(RedirectView):
  url = "https://github.com/J-888/REST-API-COVID-Spain"