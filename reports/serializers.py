from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = ('id', 'ca', 'date', 'cases', 'deceases', 'cured', 'hospitalized','uci','accIncidence','diffCases')

	"""pk = serializers.IntegerField(read_only=True)

	ca = serializers.CharField()
	date = serializers.DateField()
	cases = serializers.IntegerField()
	deceases = serializers.IntegerField()
	cured = serializers.IntegerField()
	
	hospitalized = serializers.IntegerField()
	uci = serializers.IntegerField()
	accIncidence = serializers.IntegerField()
	diffCases = serializers.IntegerField()

	def create(self, validated_data)	
		# Create and return a new `Report` instance, given the validated data.
		return Report.objects.create(**validated_data)

	def update(self, instance, validated_data):
		# Update and return an existing `Report` instance, given the validated data.
		instance.ca = validated_data.get('ca', instance.ca)
		instance.date = validated_data.get('date', instance.date)
		instance.cases = validated_data.get('cases', instance.cases)
		instance.deceases = validated_data.get('deceases', instance.deceases)
		instance.cured = validated_data.get('cured', instance.cured)
		
		instance.hospitalized = validated_data.get('hospitalized', instance.hospitalized)
		instance.uci = validated_data.get('uci', instance.uci)
		instance.accIncidence = validated_data.get('accIncidence', instance.accIncidence)
		instance.diffCases = validated_data.get('diffCases', instance.diffCases)

		instance.save()
		return instance"""