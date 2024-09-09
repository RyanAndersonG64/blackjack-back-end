# Generated by Django 5.0.6 on 2024-08-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackjack_app', '0004_alter_profile_hand'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='suit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='value',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(to='blackjack_app.card'),
        ),
    ]
