# Generated by Django 2.2.4 on 2019-08-07 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0004_auto_20190806_2223'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categorias', verbose_name='categorias')),
            ],
        ),
    ]