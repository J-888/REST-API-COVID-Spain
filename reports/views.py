# from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from reports.models import Report
from reports.serializers import ReportSerializer

class JSONResponse(HttpResponse):
	# An HttpResponse that renders its content into JSON.
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

# API Services
@csrf_exempt # TODO only POST requires csrf token
def report_list(request):
	# List all code report, or create a new report.

	if request.method == 'GET':
		reports = Report.objects.all()
		serializer = ReportSerializer(reports, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ReportSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt # TODO only POST, PUT and DELETE requires csrf token
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
