from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view
from project.main.views.utils import UtilsViewSet, descriptionView
from project.main.views.users import UserViewSet
from project.main.views.students import StudentViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', UtilsViewSet, base_name="utils")
router.register(r'users', UserViewSet, base_name='user')
router.register(r'students',StudentViewSet,base_name='student')

urlpatterns = [
    path('', include(router.urls)),
    path('openapi', get_schema_view(
        title="DRF-Starter",
        description="API for DRF-Starter"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
