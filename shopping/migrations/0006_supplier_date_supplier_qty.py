from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_supplier_delivered_alter_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='supplier',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
