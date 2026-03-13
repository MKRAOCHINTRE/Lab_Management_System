from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0013_evaluation_viva_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelupload',
            name='file',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
