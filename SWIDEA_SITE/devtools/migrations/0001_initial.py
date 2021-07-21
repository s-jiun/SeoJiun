# Generated by Django 3.2.5 on 2021-07-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(help_text='개발툴의 이름을 입력하세요', max_length=50)),
                ('type', models.CharField(help_text='개발툴의 종류를 입력하세요', max_length=100)),
                ('tool_desc', models.TextField(blank=True, help_text='개발툴에 대한 설명을 적어주세요')),
            ],
        ),
    ]
