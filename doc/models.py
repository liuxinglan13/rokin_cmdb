from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe


# Create your models here.
# 文档
class Doc(models.Model):
    # 标题
    doc_subject = models.CharField(max_length=255, verbose_name="文档标题")
    # 正文
    doc_body = models.TextField(max_length=2550, verbose_name="文档正文")
    # 创建时间
    doc_ctime = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间', blank=True)
    # 最后更新时间
    doc_utime = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间', blank=True)

    def __str__(self):
        return self.doc_subject

    class  Meta:
        # 后台中显示的名称
        verbose_name="文档管理"
        # 去掉s 没有的话 在后台中会显示  资产管理s
        verbose_name_plural = '文档管理'

        # 这个函数 用来生成 url

    def get_absolute_url(self):
        return reverse('doc:doc_update', kwargs={'pk': self.pk})

