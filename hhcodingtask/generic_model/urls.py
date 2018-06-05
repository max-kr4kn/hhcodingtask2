from django.conf.urls import url
from . import views


app_name = 'generic_model'
urlpatterns = [
    url(regex=r'^create/$', view=views.CreateGenericModelView.as_view(), name='create'),
]
