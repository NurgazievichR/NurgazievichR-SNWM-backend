from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path

schema_view = get_schema_view(
   openapi.Info(
      title="SNWM API",
      default_version='v1',
      description="Ну пока что собираюсь сделать как обычную соцсеть + в планах добавить карту и парсер какой нибудь",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zr12169@auca.kg"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]