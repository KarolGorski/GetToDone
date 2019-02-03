# Generated by Django 2.1.5 on 2019-02-03 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_multiplier', models.FloatField()),
            ],
            options={
                'verbose_name': 'Difficulty',
                'verbose_name_plural': 'Difficulties',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority_num', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Difficulty',
                'verbose_name_plural': 'Difficulties',
            },
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2019-02-03')),
                ('due_date', models.DateField(default='2019-02-03')),
                ('estimatedTime', models.CharField(max_length=10)),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todostack.Category')),
                ('difficulty', models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='todostack.Difficulty')),
                ('priority', models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='todostack.Priority')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
