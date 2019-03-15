# Generated by Django 2.1.7 on 2019-03-13 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_user_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('text', models.CharField(max_length=200, verbose_name='question')),
                ('has_importance', models.BooleanField(default=False, verbose_name='has importance')),
                ('type', models.CharField(choices=[('yesno', 'yes or no'), ('grade', 'grade'), ('text', 'text'), ('checkbox', 'checkbox')], max_length=20, verbose_name='type')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('new_page', models.BooleanField(default=False, verbose_name='starts new page')),
            ],
            options={
                'verbose_name': 'question group',
                'verbose_name_plural': 'question groups',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('code', models.CharField(default='D3JIEPSy3GzlyKFb98fC', max_length=20, unique=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'survey',
                'verbose_name_plural': 'surveys',
            },
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='iZsh3AMufwXpqd2UUI0g', max_length=20, verbose_name='code')),
                ('status', models.PositiveIntegerField(choices=[(0, 'initial state'), (5, 'invited'), (10, 'started'), (15, 'finished'), (20, 'completed')], default=0, verbose_name='status')),
                ('answers', models.TextField(blank=True, verbose_name='answers')),
                ('visitor_company', models.CharField(blank=True, max_length=100, verbose_name='company')),
                ('visitor_name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('visitor_contact', models.CharField(max_length=100, verbose_name='contact')),
                ('visitor_counter', models.PositiveIntegerField(default=0, verbose_name='visitor counter')),
                ('conductor_company', models.CharField(blank=True, max_length=100, verbose_name='company')),
                ('conductor_name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('conductor_contact', models.CharField(blank=True, max_length=100, verbose_name='contact')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.Survey', verbose_name='survey')),
            ],
            options={
                'verbose_name': 'survey answer',
                'verbose_name_plural': 'survey answers',
            },
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='survey.Survey', verbose_name='survey'),
        ),
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.QuestionGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='surveyanswer',
            unique_together={('survey', 'code')},
        ),
        migrations.AlterUniqueTogether(
            name='questiongroup',
            unique_together={('survey', 'ordering')},
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('group', 'ordering')},
        ),
    ]
