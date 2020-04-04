from django.db import models



class Report(models.Model):
	
	ca = models.CharField(max_length=50)
	date = models.DateField()
	cases = models.IntegerField(default=None)
	deceases = models.IntegerField(default=None)
	cured = models.IntegerField(default=None)

	hospitalized = models.IntegerField(default=None)
	uci = models.IntegerField(default=None)
	accIncidence = models.IntegerField(default=None)
	diffCases = models.IntegerField(default=None)
