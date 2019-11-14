# Generated by Django 2.2.4 on 2019-11-12 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20191111_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='dprofile',
            name='about_you',
            field=models.TextField(default='Write About Yourself...', max_length=30000),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='full_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='mci_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='phone_no',
            field=models.IntegerField(default=0, max_length=12),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='qualification',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='reg_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='specialities_opt',
            field=models.CharField(choices=[('Gynecologist', 'Gynecologist'), ('General Physician', 'General Physician'), ('Orthopedician', 'Orthopedician'), ('Dietitian', 'Dietitian'), ('Pediatrician', 'Pediatrician'), ('Dermatologist', 'Dermatologist'), ('Psychiatrist', 'Psychiatrist'), ('Andrologist', 'Andrologist'), ('Urologist', 'Urologist'), ('General Surgeon', 'General Surgeon'), ('Dentist', 'Dentist'), ('Pulmonologist', 'Pulmonologist'), ('Oncologist', 'Oncologist'), ('Nephrologist', 'Nephrologist'), ('Sports Medicine', 'Sports Medicine'), ('Psychotherapist', 'Psychotherapist'), ('Diabetologist', 'Diabetologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Endocrinologist', 'Endocrinologist'), ('Fertility Specialist', 'Fertility Specialist'), ('Neurosurgeon', 'Neurosurgeon'), ('Neurologist', 'Neurologist'), ('Cosmetologist', 'Cosmetologist')], default='please define your Specialist', max_length=50),
        ),
        migrations.AddField(
            model_name='dprofile',
            name='yr_expr',
            field=models.IntegerField(default=0),
        ),
    ]
