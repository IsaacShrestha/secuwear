from django.conf.urls import url, include
from . import views

from rest_framework import routers


router=routers.DefaultRouter(trailing_slash=False)
router.register(r'CollectedData', views.CollectedDataViewSet)


urlpatterns = [
	#url(r'^$',views.home, name='home'),
	url(r'^api/', include(router.urls)),

]