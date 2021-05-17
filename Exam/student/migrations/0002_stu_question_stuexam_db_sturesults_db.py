

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20201201_1604'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_Question',
            fields=[
                ('question_db_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='questions.question_db')),
                ('choice', models.CharField(default='E', max_length=3)),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('questions.question_db',),
        ),
        migrations.CreateModel(
            name='StuExam_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examname', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('completed', models.IntegerField(default=0)),
                ('qpaper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.question_paper')),
                ('questions', models.ManyToManyField(to='student.Stu_Question')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StuResults_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exams', models.ManyToManyField(to='student.StuExam_DB')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
