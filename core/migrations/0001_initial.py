# Generated by Django 4.2.6 on 2023-10-23 20:24

import core.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('COORDENADOR', 'Coordenador'), ('SUPERVISOR', 'Supervisor'), ('AVALIADOR', 'Avaliador')], default='Avaliador', max_length=25)),
                ('image_url', models.ImageField(blank=True, default='media/admin_image/generic_profile.png', null=True, upload_to=core.models.upload_image_pessoa)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField(default=datetime.date.today)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('registroProfissional', models.CharField(blank=True, max_length=30, null=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]