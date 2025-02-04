# Generated by Django 2.2 on 2020-07-25 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChainAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price_from', models.DateField()),
                ('price_to', models.DateField()),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price_from', models.DateField()),
                ('price_to', models.DateField()),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='HandleBarWithBrake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price_from', models.DateField()),
                ('price_to', models.DateField()),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Seating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price_from', models.DateField()),
                ('price_to', models.DateField()),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price_from', models.DateField()),
                ('price_to', models.DateField()),
                ('spoke_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('rim_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('tube_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('tyre_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('tyre_type', models.CharField(choices=[('Tube Less', 'Tube Less'), ('Tube', 'Tube')], max_length=10)),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheel_unit', models.PositiveIntegerField(default=2)),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('chain_assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycle.ChainAssembly')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycle.Frame')),
                ('handlebar_with_brake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycle.HandleBarWithBrake')),
                ('seating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycle.Seating')),
                ('wheel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycle.Wheel')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
