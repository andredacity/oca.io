# Generated by Django 3.2.3 on 2021-05-19 04:10

from django.db import migrations, models
import django_editorjs.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('body', django_editorjs.fields.EditorJsField()),
            ],
        ),
    ]
