from django.contrib import admin

from .models import Question

admin.site.register(Question)  # 向管理页面中加入数据字段对象
