# Generated by Django 4.2.7 on 2023-12-12 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_name', models.CharField(max_length=100)),
                ('urun_description', models.CharField(max_length=250)),
                ('urun_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('urun_image', models.CharField(max_length=500)),
                ('urun_slug', models.SlugField(blank=True, unique=True)),
                ('urun_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.kategori')),
            ],
        ),
    ]
