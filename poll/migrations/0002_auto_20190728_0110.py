# Generated by Django 2.2.3 on 2019-07-27 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='qusetion_text',
            new_name='question_text',
        ),
    ]
