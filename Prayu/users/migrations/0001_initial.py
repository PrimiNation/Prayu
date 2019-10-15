# Generated by Django 2.2.4 on 2019-10-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Ayurveda', 'Ayurveda'), ('Vitamins & Supplements', 'Vitamins & Supplements'), ('Homeopathy', 'Homeopathy'), ('Protein Supplements', 'Protein Supplements'), ('Elderly Care', 'Elderly Care'), ('Sexual Wellness', 'Sexual Wellness'), ('Health Food & Drinks', 'Health Food & Drinks'), ('Healthcare Devices', 'Healthcare Devices'), ("Other's", "Other's")], max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=1000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='PriminationShop/images')),
            ],
        ),
    ]