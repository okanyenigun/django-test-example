# Generated by Django 4.1.4 on 2022-12-11 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.game')),
            ],
        ),
    ]
