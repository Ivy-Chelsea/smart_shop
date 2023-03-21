# Generated by Django 4.1.5 on 2023-01-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_supplier_delete_customer_delete_suppliers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='delivered',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
