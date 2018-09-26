from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
# Create your models here.

DEPARTMENT = (
    ('x', '行政部'),
    ('j', '技术部'),
    ('p', '产品部'),
    ('f', '财务'),
    ('b', 'BOSS'),
)
class Quest(models.Model):
    title =models.CharField('问题',max_length=256)
    reward =models.IntegerField('奖励',default=0)
    req_user =models.IntegerField('需求人数',default=0)
    date = models.DateField('日期',auto_now=True)
    content = models.TextField('内容',)
    keyword = models.CharField('关键字',max_length=2,choices=DEPARTMENT)
    flag = models.BooleanField('标志',default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'


class Img(models.Model):
    title = models.CharField('图片名',max_length=50)
    img = models.FileField('图片',upload_to='img')

    def img_data(self):
        print(self.img.url)
        return format_html(f'<img src="{self.img.url}" width="100px"/>')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
    img_data.short_description='图片'


class Treasure(models.Model):
    state_store=(
        (1,'货足'),
        (2,'没有货了')
    )
    title = models.CharField('宝物名字',max_length=256)
    item = models.CharField('道具',max_length=64)
    value = models.IntegerField('价值',default=0)
    store = models.IntegerField('库存',default=0)
    stat = models.IntegerField('库存状态',default=1,choices=state_store)
    flag = models.BooleanField('达成',default=False)
    tcreate_date = models.DateTimeField('创建日期',auto_now=True)
    img = models.ForeignKey(Img,on_delete=models.CASCADE,verbose_name='图片')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '宝物'
        verbose_name_plural = '宝物'

    def img_data(self):
        print(self.img.url)
        return format_html(f'<img src="{self.img.url}" width="100px"/>')

    img_data.short_description = '图片'


class Sign(models.Model):
    date = models.DateField('日期',auto_now=True)
    class Meta:
        verbose_name = '签到'
        verbose_name_plural = '签到'


class Log(models.Model):

    label = models.CharField('标签',max_length=256)
    catlog=models.CharField('分类',max_length=20)
    date=models.DateTimeField('生成时间',auto_now=True)
    pub_deptment=models.CharField('发布部门',max_length=2,choices=DEPARTMENT)

    def __str__(self):
        return self.label
    class Meta:
        verbose_name = '日志'
        verbose_name_plural = '日志'


class User(AbstractUser):
    work_number=models.IntegerField('工号',default=0)
    name = models.CharField('名字',max_length=20,blank=True)
    create_datetime=models.DateTimeField('创建时间',auto_now=True)
    currency=models.IntegerField('微币',default=0)
    total_currency=models.IntegerField('总量',default=0)
    quest=models.ManyToManyField(Quest,blank=True,verbose_name='任物')
    treasure=models.ManyToManyField(Treasure,blank=True,verbose_name='宝物')
    token = models.CharField('令牌',max_length=256,blank=True,default='')
    department=models.CharField('部门',max_length=2,blank=True,choices=DEPARTMENT)
    is_administer = models.BooleanField('管理员',default=False)
    sign=models.ForeignKey(Sign, on_delete=models.SET_NULL,blank=True,null=True,verbose_name='签到')
    img=models.ForeignKey(Img, on_delete=models.SET_NULL,blank=True,null=True,verbose_name='图片')
    log = models.ForeignKey(Log, on_delete=models.SET_NULL,blank=True,null=True,verbose_name='日志')

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'