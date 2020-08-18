from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import *


class SearchedLinksSerializer(serializers.ModelSerializer):
	class Meta:
		model = SearchedLinks
		fields = "__all__"