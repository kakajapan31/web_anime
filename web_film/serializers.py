from rest_framework import serializers
from .models import *

class Film_serializer(serializers.ModelSerializer):
    class Meta:
        model = Phim
        fields = ('ten_phim', 'ngay_khoi_chieu', 'quoc_gia', 'mo_ta', 'thoi_luong', 'so_tap', 'luot_xem')

class Author_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dao_dien
        fields = ('ten_tac_gia', 'nam_sinh', 'quoc_gia', 'chieu_cao', 'so_truong', 'so_thich')

class Actor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dien_vien
        fields = ('ten_dien_vien', 'nam_sinh', 'quoc_gia', 'chieu_cao', 'so_truong', 'so_thich')

class Genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = The_loai
        fields = ('ten_the_loai', 'mo_ta')

class Film_th_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tap_phim
        fields = ('phim', 'tap_thu', 'url')

class Question_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text')

class Choice_serializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text')