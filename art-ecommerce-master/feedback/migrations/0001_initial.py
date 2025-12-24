# Generated migration for Feedback model

from django.conf import settings
from django.db import migrations, models
from django.core.validators import MinValueValidator, MaxValueValidator
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '⭐ Poor'), (2, '⭐⭐ Fair'), (3, '⭐⭐⭐ Good'), (4, '⭐⭐⭐⭐ Very Good'), (5, '⭐⭐⭐⭐⭐ Excellent')], default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer Feedback',
                'verbose_name_plural': 'Customer Feedbacks',
                'ordering': ['-created_at'],
            },
        ),
    ]
