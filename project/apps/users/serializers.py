from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ShortUserSerializer(serializers.ModelSerializer):
    # tags = TagListSerializerField()
    # education = serializers.SerializerMethodField('get_education')
    # gender = serializers.SerializerMethodField('get_gender')
    #
    # def get_education(self, obj):
    #     return obj.profile.education
    #
    # def get_gender(self, obj):
    #     return obj.profile.gender

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email',
            'first_name', 'last_name',
            'last_login', 'date_joined',
            # 'education', 'gender',
        )

# class UserEditSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     first_name = serializers.CharField(required=False, max_length=10)
#     last_name = serializers.CharField(required=False, max_length=10)
#     birthday = serializers.DateField(required=False)
#
#     class Meta:
#         fields = ('email', 'first_name', 'last_name',  'birthday')


# class UserAdditionSerializer(UserCreationForm):
#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#     # captcha = ReCaptchaField()
#
#     def save(self, validated_data):
#         return User(**validated_data)
#
#     class Meta:
#         model = User
#         fields = {'username', 'password1', 'password2', 'email'}