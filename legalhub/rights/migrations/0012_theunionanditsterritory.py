# Generated by Django 4.2.6 on 2025-03-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rights', '0011_alter_reply_lawyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheUnionandItsTerritory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=400)),
                ('Description', models.CharField(max_length=50002)),
                ('img1', models.ImageField(default='images/default_image.png', upload_to='images/')),
                ('ex1', models.CharField(blank=True, max_length=500, null=True)),
                ('img2', models.ImageField(default='images/default_image.png', upload_to='images/')),
                ('ex2', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
