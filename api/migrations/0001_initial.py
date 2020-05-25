# Generated by Django 2.2 on 2020-05-25 13:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneNumber', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('amountOutstanding', models.FloatField()),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('isRecurring', models.BooleanField()),
                ('frequencyOfReocurence', models.CharField(max_length=30)),
                ('VendorId', models.ForeignKey('api.Vendor', on_delete=models.CASCADE))
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='MessageStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneNumber', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100)),
                ('itemsOrdered', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('amountDue', models.FloatField()),
                ('amountPaid', models.FloatField()),
                ('amountOutstanding', models.FloatField()),
                ('orderStatus', models.IntegerField(choices=[(1, 'Pendind'), (2, 'Delivered'), (3, 'Cancelled')])),
                ('dateAndTimeOfOrder', models.DateTimeField(auto_now_add=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Menu')),
                ('vendorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Vendor')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('messageStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MessageStatus')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
                ('subjectUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Vendor')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='vendorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Vendor'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('itemsOrdered', models.ManyToManyField(to='api.Order')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('landmark', models.CharField(max_length=50)),
                ('itemsOrdered', models.ManyToManyField(to='api.Order')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'verbose_name_plural': 'Shipping Addresses',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
