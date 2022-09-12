from rest_framework import serializers

from staff.models import Department, Post, Staff


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'title']


class StaffSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Staff
        fields = ['id', 'fullname', 'lname', 'fname', 'sname', 'number', 'post', 'department', 'photo']
