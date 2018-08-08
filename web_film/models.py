from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    id_correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class The_loai(models.Model):
    ma_the_loai = models.AutoField(primary_key=True)
    ten_the_loai = models.CharField(max_length=50)
    mo_ta = models.TextField(blank=True, null=True)
    hinh = models.ImageField(null=True)

    def __str__(self):
        return self.ten_the_loai

class Dao_dien(models.Model):
    ma_tac_gia = models.AutoField(primary_key=True)
    ten_tac_gia = models.CharField(max_length=100)
    nam_sinh = models.IntegerField(default=0)
    quoc_gia = models.CharField(max_length=50)
    hinh = models.ImageField(null=True)
    chieu_cao = models.CharField(max_length=10)
    so_truong = models.CharField(max_length=100)
    so_thich = models.CharField(max_length=100)
    the_loai = models.ManyToManyField(The_loai)

    def __str__(self):
        return self.ten_tac_gia

class Dien_vien(models.Model):
    ma_dien_vien = models.AutoField(primary_key=True)
    ten_dien_vien = models.CharField(max_length=100)
    nam_sinh = models.IntegerField(default=0)
    quoc_gia = models.CharField(max_length=50)
    hinh = models.ImageField(null=True)
    chieu_cao = models.CharField(max_length=10)
    so_truong = models.CharField(max_length=100)
    so_thich = models.CharField(max_length=100)
    the_loai = models.ManyToManyField(The_loai)

    def __str__(self):
        return self.ten_dien_vien

class Phim(models.Model):
    ma_phim = models.AutoField(primary_key=True)
    ten_phim = models.CharField(max_length=100)
    ngay_khoi_chieu = models.CharField(max_length=20)
    quoc_gia = models.CharField(max_length=50)
    hinh = models.ImageField(null=True)
    mo_ta = models.TextField(blank=True, null=True)
    thoi_luong = models.CharField(max_length=20)
    so_tap = models.IntegerField(default=1)
    luot_xem = models.IntegerField(default=0)
    the_loai = models.ManyToManyField(The_loai)
    dao_dien = models.ManyToManyField(Dao_dien)
    dien_vien = models.ManyToManyField(Dien_vien)

    def __str__(self):
        return self.ten_phim

class Tap_phim(models.Model):
    ma_tap = models.AutoField(primary_key=True)
    tap_thu = models.IntegerField(default=1)
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.phim.ten_phim + " tap " + str(self.tap_thu)

class Nhan_xet(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE, db_column='phim', related_name='nhan_xet', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='nguoi_nhan_xet', on_delete=models.CASCADE)
    noi_dung = models.TextField(null=True)
    ngay_dang = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.noi_dung