from rest_framework import viewsets
from staff.models import Staff, Department
from staff.api.serializers import StaffSerializer, DepartmentSerializer
from staff.api.filters import StaffFilter, DepartmentFilter


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_class = StaffFilter


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilter
