# Generated by Django 2.1.5 on 2019-02-01 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Espn', '0005_profile_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2200)),
            ],
        ),
        migrations.CreateModel(
            name='CommentField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type', models.CharField(choices=[('G', 'Game'), ('T', 'Team'), ('P', 'Player'), ('L', 'League'), ('N', 'News')], max_length=1)),
                ('commented_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Comment.Comment')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Espn.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comment.CommentField'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Espn.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Comment.Comment'),
        ),
    ]