# Generated by Django 2.2 on 2020-06-21 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Microrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', db_index=True, max_length=200)),
                ('data_request', models.DateTimeField(auto_now_add=True, db_column='data_request')),
                ('data_accept', models.DateTimeField(blank=True, db_column='data_accept', null=True)),
                ('data_completed', models.DateTimeField(blank=True, db_column='data_completed', null=True)),
                ('delay', models.PositiveIntegerField(db_column='delay')),
                ('quantity', models.PositiveIntegerField(db_column='quantity')),
                ('status', models.CharField(choices=[('adopted', 'adopted'), ('processing', 'processing'), ('completed', 'completed'), ('error', 'error')], db_column='status', default='adopted', max_length=10)),
            ],
            options={
                'db_table': 'microrequest',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField(db_column='elapsed_time')),
                ('temperature', models.SmallIntegerField(db_column='temperature')),
                ('illumination', models.SmallIntegerField(db_column='illumination')),
                ('microrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='microrequest_id', to='data_viewer.Microrequest')),
            ],
            options={
                'db_table': 'entry',
            },
        ),
    ]
