# Generated by Django 2.2.10 on 2020-03-02 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGroup', models.CharField(max_length=42, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('isadmin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ending_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name_projet', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=500)),
                ('group_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Group')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Group')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_task', models.CharField(max_length=128)),
                ('discription_task', models.TextField(max_length=500)),
                ('task_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('id_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Projet')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='idProfile',
            field=models.ForeignKey(db_column='idemployee', on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
