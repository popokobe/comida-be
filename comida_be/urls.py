from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    path('auth/', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('docs/', include_docs_urls(title='APIドキュメント'))]
