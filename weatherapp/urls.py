from django.urls import path

from .views import LocationTempView

urlpatterns = [
    path(
        "locations/<str:city>/",
        LocationTempView.as_view(),
        name="location-temp",
    )
]
