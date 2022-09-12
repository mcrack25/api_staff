from rest_framework import routers
from staff.api.views import StaffViewSet, DepartmentViewSet


router = routers.DefaultRouter()
router.register('staff', StaffViewSet)
router.register('departments', DepartmentViewSet)
