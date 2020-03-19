from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api/v0/', include('apiv0.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('docs/', include_docs_urls(title='APIドキュメント'))]
