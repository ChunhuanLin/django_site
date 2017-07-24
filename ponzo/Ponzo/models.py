# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

# Ponzo Illusion test cases
#
# - Figure_name
# - 人眼与观察平面的距离(x)
# - 人眼的高度(z)
# - 两条水平线之间的间距(d)
# - 两条水平线的长度比(rate_l)
# - 测试组别

class IllusionCase(models.Model):
    eye_x = models.FloatField()
    eye_z = models.FloatField()
    b_dist = models.FloatField()
    b_ratio = models.FloatField()
    ratio = models.FloatField()
    fig_name = models.CharField(max_length=256)
    group = models.IntegerField()

    def __str__(self):
        str_expr = "{id} {eye_x} {eye_z} {b_dist} {b_ratio} {ratio} {fig_name} {group}"
        return str_expr.format(**self.__dict__)


# Information of subjects
# - User_id
# - 性别: 不同性别对的场依存性与场独立性不同
# - 年龄阶段: 不同年龄段的经验是否有影响？
# - 视力: 保证测试的有效性
# - 学习领域: 理性思维与感性思维对认知的影响

GENDER_CHOICES = (("M", _("男")), ("F", _("女")))

AREA_STUDY = (
    ("WK", _("文史类")),
    ("LG", _("理工类")),
    ("YY", _("医药学类")),
    ("FX", _("法学类")),
    ("YS", _("艺术类")),
    ("OT", _("其他")))

class Subject(models.Model):
    gender = models.CharField(choices=GENDER_CHOICES, max_length=32)
    age = models.IntegerField()
    vision = models.FloatField()
    area = models.CharField(max_length=256, choices=AREA_STUDY)
    mail = models.EmailField(max_length=256)

    def __str__(self):
        str_expr = "{id}: {gender} {age} {vision:g} {area} {mail}"
        return str_expr.format(id=self.id, gender=self.get_gender_display(),
                               age=self.age, vision=self.vision, area=self.get_area_display(),mail=self.mail)


class Answer(models.Model):
    question = models.ForeignKey(IllusionCase)
    subject = models.ForeignKey(Subject)
    ratio = models.FloatField()

    def __str__(self):
        str_expr = "{id} {question} {subject} {ratio}"
        return str_expr.format(id=self.id,
                               question=self.question,
                               subject=self.subject,
                               ratio=self.ratio)
