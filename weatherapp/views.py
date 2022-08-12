from django.http import JsonResponse
from rest_framework.views import APIView
from .utils import get_temperature
from rest_framework.status import HTTP_400_BAD_REQUEST


class LocationTempView(APIView):
    """
    Returns location temperature details (maximum,minimum,average,median) for a range of days.
    """

    def get(self, request, city):
        days = request.GET.get('days')
        if days:
            try:
                days = int(days)
            except ValueError:
                return JsonResponse(
                    {"error": "Invalid days, number expected"}, status=HTTP_400_BAD_REQUEST)
        result = get_temperature(city, days)
        if not result:
            return JsonResponse({"error": "No data"},
                                status=HTTP_400_BAD_REQUEST)
        return JsonResponse(result)
