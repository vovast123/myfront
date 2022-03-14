# Generated by Django 4.0.3 on 2022-03-03 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('rare', models.CharField(choices=[('CM', 'Common'), ('UC', 'Uncommon'), ('RR', 'Rare'), ('MK', 'Mythical'), ('LG', 'Legendary'), ('IM', 'Immortal'), ('AC', 'Arcana'), ('AN', 'Ancient'), ('DT', 'Dota plus')], max_length=100, verbose_name='Редкость')),
                ('text', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Ценна')),
                ('hero', models.CharField(max_length=155, verbose_name='Герой')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='time')),
            ],
            options={
                'verbose_name': 'скин',
                'verbose_name_plural': 'скины',
            },
        ),
    ]