from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Phim)
admin.site.register(Dien_vien)
admin.site.register(Dao_dien)
admin.site.register(The_loai)
admin.site.register(Nhan_xet)