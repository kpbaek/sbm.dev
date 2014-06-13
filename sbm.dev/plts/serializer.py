from tastypie.serializers import Serializer
class MySerializer(Serializer):
	def format_datetime(self, data):
		return data.strftime("%Y-%m-%d %H:%M")
