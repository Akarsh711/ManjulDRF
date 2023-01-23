from django.contrib.auth.models import User, Group
from .models import Todo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TodoSerializer(serializers.ModelSerializer):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get('fields', None)
        if field_names:
            return field_names

        return super(TodoSerializer, self).get_field_names(*args, **kwargs)

    class Meta:
        model = Todo
        fields = ['id', 'user_id', 'name', 'done', 'date_created', 'date_completed']
