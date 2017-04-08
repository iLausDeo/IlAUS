import jsonfield, json

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ILAUS_GENDER_CHOICE = (
    ('male', u'男'),
    ('female', u'女'),
    ('na', u'未知'),
)

ILAUS_CATEGORY_CHOICE = (
    ('stu', u'学生'),
    ('ind', u'个人'),
    ('org', u'机构'),
    ('adm', u'管理员'),
    ('unk', u'未知'),
)
ILAUS_INCOMING_SOURCE_CHOICE = (
    ('site', u'网站注册'),
    ('wechat', u'微信注册'),
    ('admin', u'管理员'),
)


class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    gender = models.CharField(max_length=10, choices=ILAUS_GENDER_CHOICE, null=True, blank=True)
    category = models.CharField(max_length=8, choices=ILAUS_CATEGORY_CHOICE)
    source = models.CharField(max_length=8, choices=ILAUS_INCOMING_SOURCE_CHOICE)
    # 昵称姓名
    user_name = models.CharField(max_length=100, default='', blank=True) 
    nick_name = models.CharField(max_length=100, default='', blank=True)
    org_name = models.CharField(max_length=100, default='', blank=True)
    # 手机
    mobile_phone = models.CharField(max_length=16, blank=True)
    phone_country = models.CharField(max_length=100, blank=True)
    phone_country_code = models.CharField(max_length=100, blank=True)

    dob = models.DateField(verbose_name='date of birth', null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True, default="chinese")
    description = models.TextField(max_length=1000, default='', blank=True)

    photo_paths = jsonfield.JSONField(default=[])
    profile_paths = jsonfield.JSONField(default=[])
    # 地址
    street_number = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True, default="CN")
    currency = models.CharField(max_length=20, null=True, blank=True, default="RMB")

    latitude = models.DecimalField(max_digits=16, decimal_places=11, null=True, blank=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=11, null=True, blank=True)
    time_zone_id = models.CharField(max_length=200, null=True, blank=True)
    login_ip = models.GenericIPAddressField(verbose_name='login IP address', null=True, blank=True)
    login_duration = models.DurationField(verbose_name='last login duration', null=True, blank=True)
    signup_platform = models.CharField(max_length=128, null=True)

    created_at = models.DateTimeField(default=timezone.now, null=True)
    credit = models.DecimalField(max_digits=16, decimal_places=11, default=0)

    @property
    def get_gender(self):
        return  dict(ILAUS_GENDER_CHOICE).get(self.gender)

    class Meta:
        db_table = 'user_info'












