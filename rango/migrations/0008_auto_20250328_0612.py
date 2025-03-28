from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_character_start_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Achievement',
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_unlocked', models.DateTimeField(auto_now_add=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Character')),
            ],
        ),
        # Add new fields to the Character model.
        migrations.AddField(
            model_name='character',
            name='total_kills',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='boss_kills',
            field=models.IntegerField(default=0),
        ),
    ]
