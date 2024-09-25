# Generated by Django 5.1.1 on 2024-09-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_tag_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddIndex(
            model_name='painting',
            index=models.Index(fields=['id', 'slug'], name='shop_painti_id_7d38a9_idx'),
        ),
        migrations.AddIndex(
            model_name='painting',
            index=models.Index(fields=['name'], name='shop_painti_name_f5efbf_idx'),
        ),
        migrations.AddIndex(
            model_name='painting',
            index=models.Index(fields=['-created'], name='shop_painti_created_613936_idx'),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['name'], name='shop_tag_name_971c74_idx'),
        ),
    ]
