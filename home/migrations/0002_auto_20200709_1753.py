# Generated by Django 3.0.5 on 2020-07-09 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='price',
            new_name='prix',
        ),
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
    ]
