# Generated by Django 2.1.7 on 2019-03-14 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20190314_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Name')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Display order')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('required', models.BooleanField(verbose_name='Required')),
                ('type', models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer')], default='text', max_length=200, verbose_name='Type')),
                ('choices', models.TextField(blank=True, null=True, verbose_name='Choices')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='survey.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'ordering': ('survey', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('interview_uuid', models.CharField(max_length=36, verbose_name='Interview unique identifier')),
            ],
            options={
                'verbose_name': 'Set of answers to surveys',
                'verbose_name_plural': 'Sets of answers to surveys',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('is_published', models.BooleanField(verbose_name='Users can see it and answer it')),
                ('need_logged_user', models.BooleanField(verbose_name='Only authenticated users can see it and answer it')),
                ('display_by_question', models.BooleanField(verbose_name='Display by question')),
                ('template', models.CharField(blank=True, max_length=255, null=True, verbose_name='Template')),
            ],
            options={
                'verbose_name': 'survey',
                'verbose_name_plural': 'surveys',
            },
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='survey.Survey', verbose_name='Survey'),
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.Survey', verbose_name='Survey'),
        ),
        migrations.AddField(
            model_name='category',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='survey.Survey', verbose_name='Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.Question', verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.Response', verbose_name='Response'),
        ),
    ]