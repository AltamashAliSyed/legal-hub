# Generated by Django 4.2.6 on 2024-10-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rights', '0004_lawyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyer',
            name='email',
        ),
        migrations.AddField(
            model_name='lawyer',
            name='doc',
            field=models.ImageField(default='images/default_image.png', upload_to='lawyerdoc/'),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='img',
            field=models.ImageField(default='images/default_image.png', upload_to='lawyerpic/'),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
