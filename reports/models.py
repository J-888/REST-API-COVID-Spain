from django.db import models



class Report(models.Model):
	
	ca = models.CharField(max_length=50)
	date = models.DateField()
	cases = models.IntegerField(blank=True, null=True)
	deceases = models.IntegerField(blank=True, null=True)
	cured = models.IntegerField(blank=True, null=True)

	hospitalized = models.IntegerField(blank=True, null=True)
	uci = models.IntegerField(blank=True, null=True)
	accIncidence = models.IntegerField(blank=True, null=True)
	diffCases = models.IntegerField(blank=True, null=True)
