# Generated by Django 3.1.5 on 2021-02-05 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0016_product_times_viewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='times_viewed',
        ),
        migrations.CreateModel(
            name='ProductViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.product')),
            ],
        ),
    ]
