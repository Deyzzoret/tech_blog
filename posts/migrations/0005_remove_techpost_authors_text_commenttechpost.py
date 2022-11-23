# Generated by Django 4.1 on 2022-11-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_techpost_authors_text_alter_techpost_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techpost',
            name='authors_text',
        ),
        migrations.CreateModel(
            name='CommentTechPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_comment', models.CharField(max_length=100)),
                ('date_comment', models.DateField()),
                ('content_comment', models.CharField(max_length=500)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.techpost')),
            ],
        ),
    ]