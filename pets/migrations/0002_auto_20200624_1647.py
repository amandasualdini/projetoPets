# Generated by Django 3.0.7 on 2020-06-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petachado',
            name='Cor',
        ),
        migrations.AlterField(
            model_name='petachado',
            name='Nome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pets.petPerdido'),
        ),
    ]