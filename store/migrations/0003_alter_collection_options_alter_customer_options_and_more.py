# Generated by Django 4.1.3 on 2022-12-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20221216_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['title']},
        ),
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_last_na_2e448d_idx',
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
