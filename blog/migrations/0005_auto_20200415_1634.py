# Generated by Django 3.0.4 on 2020-04-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200327_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'blog'},
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image3',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]