from common.views import IndexView,search
from django.urls import path

app_name = 'common'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('search', search, name='search'),
]
