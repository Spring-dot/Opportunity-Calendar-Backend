from django.urls import path, include

app_name = "oppcal"

urlpatterns = [
    path("intern/", include("oppcal.urls_folder.intern")),
]
