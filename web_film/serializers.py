from rest_framework import serializers
from .models import *

class Film_serializer(serializers.ModelSerializer):
    class Meta:
        model = Phim
        fields = '__all__'

class Author_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dao_dien
        fields = '__all__'

class Actor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dien_vien
        fields = '__all__'

class Genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = The_loai
        fields = '__all__'

class Film_th_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tap_phim
        fields = '__all__'

class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Nhan_xet
        fields = '__all__'

class Question_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text')

class Choice_serializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
