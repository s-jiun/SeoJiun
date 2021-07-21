from django.db import models

# Create your models here.

class DevTool(models.Model):
    tool_name = models.CharField(max_length=50, help_text="개발툴의 이름을 입력하세요")
    type = models.CharField(max_length=100, help_text="개발툴의 종류를 입력하세요")
    tool_desc = models.TextField(blank=True, help_text="개발툴에 대한 설명을 적어주세요")