# Generated by Django 2.1.3 on 2018-12-24 13:49

import checkins.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


def add_polymorphic_ctype_for_identifier(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')

    for model_name in ['PersonIdentifier', 'DebateIdentifier', 'VenueIdentifier']:
        model = apps.get_model('checkins', model_name)
        new_ct = ContentType.objects.get_for_model(model)
        model.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('checkins', '0002_auto_20180420_2044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='identifier',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='identifier',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_checkins.identifier_set+', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='barcode',
            field=models.CharField(default=checkins.models.generate_identifier, max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', message='The barcode must contain exactly six digits.')], verbose_name='barcode'),
        ),
        migrations.RunPython(
            add_polymorphic_ctype_for_identifier,
            migrations.RunPython.noop
        ),
    ]
