from django import forms
from .models import Nhan_xet

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.film = kwargs.pop('film', None)
        self.noi_dung = kwargs.pop('noi_dung', None)
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = '4'

    def save(self, commit=True):
        nhan_xet = super().save(commit=False)
        nhan_xet.user = self.user
        nhan_xet.phim = self.film
        nhan_xet.noi_dung = self.noi_dung
        nhan_xet.save()

    class Meta:
        model = Nhan_xet
        fields = ['noi_dung']