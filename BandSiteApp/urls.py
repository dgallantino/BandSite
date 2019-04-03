from BandSite import settings
from BandSiteApp import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'BandSite'

urlpatterns = [
	path('', ),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
