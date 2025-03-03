# Generated by Django 5.1.3 on 2024-11-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('smartphones', 'Smartphones'), ('laptops', 'Laptops'), ('tablets', 'Tablets'), ('accessories', 'Accessories')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
    ]
