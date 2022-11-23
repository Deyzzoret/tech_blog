# Generated by Django 4.1 on 2022-11-23 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='techpost',
            name='authors_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='techpost',
            name='authors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='techposts', to='posts.author'),
        ),
    ]
