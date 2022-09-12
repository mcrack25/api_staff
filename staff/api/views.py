from rest_framework import viewsets

from staff.api.filters import DepartmentFilter, StaffFilter
from staff.api.serializers import DepartmentSerializer, StaffSerializer
from staff.models import Department, Staff


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_class = StaffFilter


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilter
