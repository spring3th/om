from django.db import models
from django.contrib.auth.models import User

class CreateUpdateTime(models.Model):
    created = models.DateTimeField(auto_now_add=True,verbose_name=u"创建日期")
    updated = models.DateTimeField(auto_now=True,verbose_name=u"更新日期")
    class Meta:
        abstract = True

class Muser(CreateUpdateTime):
    user = models.OneToOneField(User)
    permission = models.IntegerField()
    user_name = models.CharField(max_length=30,verbose_name=u"姓名")
    user_phone = models.CharField(max_length=30,verbose_name=u"电话")
    user_email = models.EmailField(blank=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "会员"
        verbose_name_plural ="会员"
