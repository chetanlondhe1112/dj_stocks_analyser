# Generated by Django 4.2.7 on 2023-12-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
        migrations.AlterField(
            model_name='equity_files',
            name='eps',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
