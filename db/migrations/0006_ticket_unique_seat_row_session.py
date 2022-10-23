# Generated by Django 4.0.2 on 2022-10-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_ticket'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ticket',
            constraint=models.UniqueConstraint(fields=('seat', 'row', 'movie_session'), name='unique_seat_row_session'),
        ),
    ]