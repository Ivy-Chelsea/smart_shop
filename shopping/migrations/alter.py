from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.TextField(default='https://th.bing.com/th/id/R.eef165ce3d85779436c21fac35fb52bf?rik=ye5wclB7Tdn11w&riu=http%3a%2f%2fwww.pngmart.com%2ffiles%2f14%2fColorful-Shopping-Bag-Transparent-PNG.png&ehk=SY8Ni2y8vUMhDfyQr4GEhsTBHLL0CPYyea3hwjCI3hY%3d&risl=&pid=ImgRaw&r=0'),
        ),
    ]
