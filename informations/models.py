from django.db import models
from imagekit.models import ProcessedImageField as ProcessedImg
from pilkit.processors import ResizeToFill


# 新闻
class News(models.Model):
    img = ProcessedImg(upload_to='newsImg',default = 'newsImg/zhbit.png',processors=[ResizeToFill(370,180)])
    title = models.CharField(max_length=20)
    created_date = models.DateField("创建日期", auto_now_add=True)
    content = models.TextField(default='null')
    is_show = models.BooleanField()

    class Meta:
        db_table = 'News'
    def __str__(self):
        return self.title

# 合作学校
class CoSchool(models.Model):
    img = ProcessedImg(upload_to='schoolImg', default='newsImg/zhbit.png', processors=[ResizeToFill(1000, 610)])
    name = models.CharField(max_length=20)
    content = models.TextField(default='null')
    is_show = models.BooleanField(default=True)

    class Meta:
        db_table = 'Co_school'

    def __str__(self):
        return self.name

# 中外项目
class StudyPlan(models.Model):
    img = ProcessedImg(upload_to='schoolImg', default='newsImg/zhbit.png', processors=[ResizeToFill(1170, 550)])
    name = models.CharField(max_length=20)
    content = models.TextField(default='null')
    is_show = models.BooleanField(default=True)

    class Meta:
        db_table = 'Co_school'

    def __str__(self):
        return self.name
