# Generated by Django 3.1.7 on 2021-05-03 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer_order_total', models.FloatField(blank=True, default=12.3, null=True)),
                ('employee_id', models.CharField(default=12.3, max_length=50)),
                ('registered_payroll', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('price', models.FloatField()),
                ('instructions', models.CharField(default='Pickup and Delivery Available', max_length=250)),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('labels', models.CharField(blank=True, choices=[('BestSeller', 'BestSeller'), ('New', 'New'), ('Spicy🔥', 'Spicy🔥'), ('Veggies', 'Veggies')], max_length=25)),
                ('label_colour', models.CharField(blank=True, choices=[('danger', 'danger'), ('success', 'success'), ('primary', 'primary'), ('info', 'info')], max_length=15)),
                ('slug', models.SlugField(default='slug')),
                ('meal_menu', models.CharField(blank=True, choices=[('Lunch', 'Lunch'), ('Breakfast', 'Breakfast'), ('Dinner', 'Dinner')], max_length=25)),
                ('quantity_available', models.IntegerField(default=1)),
                ('subcription_avail', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Food Menu',
                'verbose_name_plural': 'Food Menus',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rslug', models.SlugField()),
                ('review', models.TextField()),
                ('posted_on', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_balance', models.FloatField(blank=True, default=134.34, null=True)),
                ('created_time', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=200, null=True)),
                ('registered', models.BooleanField(default=False)),
                ('employee_id', models.CharField(max_length=200, null=True)),
                ('birth_date', models.DateTimeField(null=True)),
                ('customer_acc', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customer')),
            ],
            options={
                'verbose_name': 'Payroll',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('ordered_date', models.DateField()),
                ('payment_method', models.CharField(choices=[('Payroll', 'Payroll'), ('Credit', 'Credit')], default='Credit', max_length=20)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Active', max_length=20)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('delivery_mode', models.CharField(choices=[('Delivered', 'Delivered'), ('Pickup', 'Pickup')], max_length=20)),
                ('isPaid', models.BooleanField(default=False)),
                ('paidAt', models.DateTimeField(blank=True, null=True)),
                ('isDelivered', models.BooleanField(default=False)),
                ('subscription_order', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customer')),
                ('delivery_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.location')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item')),
            ],
            options={
                'verbose_name': 'Food Order Item',
                'verbose_name_plural': 'Food Order Items',
            },
        ),
        migrations.CreateModel(
            name='MealSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_available', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=56)),
                ('time_ordered', models.TimeField(null=True)),
                ('delivery_mode', models.CharField(choices=[('Delivered', 'Delivered'), ('PickUp', 'PickUp')], max_length=30)),
                ('payment_method', models.CharField(choices=[('Payroll', 'Payroll'), ('Credit', 'Credit')], default='Credit', max_length=30)),
                ('subscription_status', models.BooleanField(default=False)),
                ('number_days', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
                ('delivery_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.location')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item')),
            ],
            options={
                'verbose_name': 'Meal Subscription',
                'verbose_name_plural': 'Meal Subscriptions',
            },
        ),
    ]
