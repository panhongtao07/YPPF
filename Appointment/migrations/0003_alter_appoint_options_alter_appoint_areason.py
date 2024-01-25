# Generated by Django 5.0.1 on 2024-01-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Appointment", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appoint",
            options={
                "ordering": ["Aid"],
                "permissions": [
                    ("create_appointment", "创建预约"),
                    ("cancel_appointment", "取消预约"),
                ],
                "verbose_name": "预约信息",
                "verbose_name_plural": "预约信息",
            },
        ),
        migrations.AlterField(
            model_name="appoint",
            name="Areason",
            field=models.IntegerField(
                choices=[(0, "没有违约"), (1, "迟到"), (2, "人数不足"), (3, "其它原因")],
                default=0,
                verbose_name="违约原因",
            ),
        ),
    ]