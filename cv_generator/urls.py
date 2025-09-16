from django.urls import path
from . import views

app_name='cv_generator'

urlpatterns = [
    path('', view=views.index, name="index"),
    path('<int:id>/', view=views.generate_cv, name="generate_cv")
]   