from django.core.management.base import BaseCommand, CommandError
from reports.models import Report

from urllib.request import urlopen
from urllib.error import URLError
import csv
import codecs
from datetime import datetime

class Command(BaseCommand):
	help = 'Reloads the whole dataset'

	def add_arguments(self, parser):
		parser.add_argument('url', nargs=1, type=str)


	def handle(self, *args, **options):

		url = options['url'][0]

		try:
			rawtext = urlopen(url).read()
		except URLError:
			print("Invalid url")
			return
		
		lines = rawtext.splitlines()
		stats = csv.reader(codecs.iterdecode(lines, 'utf-8'))

		firstRow = True
		regionIndex = -1
		dateIndex = -1
		casesIndex = -1
		deceasesIndex = -1		
		curedIndex = -1
		
		hospitalizedIndex = -1
		uciIndex = -1
		accIncidenceIndex = -1
		diffCasesIndex=-1

		for row in stats:
			if firstRow:
				firstRow = False
				headings = [x.upper() for x in row]

				try:
					regionIndex = headings.index("CCAA")
					dateIndex = headings.index("FECHA")
					casesIndex = headings.index("CASOS")
					accIncidenceIndex = headings.index("IA")
					uciIndex = headings.index("UCI")
					deceasesIndex = headings.index("MUERTES")
					hospitalizedIndex = headings.index("HOSPITALIZADOS")
					curedIndex = headings.index("CURADOS")
					diffCasesIndex = headings.index("NUEVOS")
				except ValueError:
					print("Invalid csv headers")
					return
		
				Report.objects.all().delete()	# Now its safe to drop table
			else:
				region = row[regionIndex]
				validDate = True

				try:
					date = datetime.strptime(row[dateIndex], '%Y-%m-%d').date()
				except ValueError:
					validDate = False
					print("Skipped row: Invalid date for region",  region, ":", row[dateIndex])
				
				if validDate:
					cases = strToInt(row[casesIndex])
					deceases = strToInt(row[deceasesIndex])
					cured = strToInt(row[curedIndex])

					hospitalized = strToInt(row[hospitalizedIndex])
					uci = strToInt(row[uciIndex])
					accIncidence = strToFloat(row[accIncidenceIndex])
					diffCases = strToInt(row[diffCasesIndex])

					
					Report(
						ca = region,
						date = date,
						cases = cases,
						deceases = deceases,
						cured = cured,

						hospitalized = hospitalized,
						uci = uci,
						accIncidence = accIncidence,
						diffCases = diffCases,
					).save()
		
		print("DONE")


def strToInt(str):
	try:
		return int(float(str))
	except ValueError:
		return None

def strToFloat(str):
	try:
		return float(str)
	except ValueError:
		return None