from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from astronauts import api
from astronauts import views as astronauts_views

urlAPIpatterns = [
    path('astronauts/', api.AstronautList.as_view()),
    path('astronauts/<int:pk>/', api.AstronautDetail.as_view())
]

urlAPIpatterns = format_suffix_patterns(urlAPIpatterns)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', astronauts_views.index, name='home'),
] + urlAPIpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)