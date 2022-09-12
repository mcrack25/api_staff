from django import forms
from django.db.models import Q
from django_filters import rest_framework as filters

from staff.models import Department, Post, Staff


class StaffFilter(filters.FilterSet):
    post = filters \
        .ModelMultipleChoiceFilter(
            field_name='post__title',
            queryset=Post.objects.all(),
            widget=forms.CheckboxSelectMultiple(),
            label='Должности',
            required=False,
        )
    department = filters \
        .ModelMultipleChoiceFilter(
            field_name='department__title',
            queryset=Department.objects.all(),
            widget=forms.CheckboxSelectMultiple(),
            label='Подразделения',
            required=False,
        )
    fullname = filters.CharFilter(method='filter_by_fullname', label='ФИО')

    def filter_by_fullname(self, queryset, name, value):
        return queryset.filter(_fullname__icontains=value)

    class Meta:
        model = Staff
        fields = ['post', 'department', 'fullname']


class DepartmentFilter(filters.FilterSet):
    parents = filters.BooleanFilter(method='filter_by_has_parent', label='Есть родитель')

    def filter_by_has_parent(self, queryset, name, value):
        return queryset.filter(~Q(parent__isnull=value))

    class Meta:
        model = Department
        fields = ['id', 'parents']
