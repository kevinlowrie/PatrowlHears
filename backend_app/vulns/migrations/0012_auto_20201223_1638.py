# Generated by Django 3.0.10 on 2020-12-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0011_auto_20201223_1635'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='vuln',
            index=models.Index(fields=['cveid'], name='vulns_cveid_c3cdba_idx'),
        ),
        migrations.AddIndex(
            model_name='vuln',
            index=models.Index(fields=['feedid'], name='vulns_feedid_511b40_idx'),
        ),
    ]