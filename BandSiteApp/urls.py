from BandSite import settings
from BandSiteApp import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'BandSite'

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
