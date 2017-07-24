# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.forms import ModelForm

from Ponzo.models import Subject

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['gender', 'age', 'vision', 'area', 'mail']
        labels = {'gender': _("性别"),
                  'age': _("年龄"),
                  'vision': _("视力(校正后)"),
                  'area': _("学习领域"),
                  'mail': _("邮箱")}

class TestForm(forms.Form):
    ratio = forms.FloatField(label="", widget=forms.NumberInput(
        attrs={'type':'range', 'step': '0.01', 'min': 0.5, 'max': 1.5}))
