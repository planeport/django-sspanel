# Generated by Django 3.0.2 on 2020-03-10 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0036_auto_20200307_1902"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relayrule",
            name="vmess_node",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="relay_rules",
                to="sspanel.VmessNode",
                verbose_name="Vmess节点",
            ),
        ),
        migrations.AlterField(
            model_name="userorder",
            name="qrcode_url",
            field=models.CharField(max_length=512, null=True, verbose_name="支付连接"),
        ),
    ]