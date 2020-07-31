# Generated by Django 2.2.12 on 2020-06-10 23:21

import django.core.validators
from django.db import migrations, models

from polaris.models import Transaction


class Migration(migrations.Migration):

    dependencies = [
        ("polaris", "0015_asset_symbol"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="send_fee_fixed",
            field=models.DecimalField(
                blank=True, decimal_places=7, max_digits=30, null=True
            ),
        ),
        migrations.AddField(
            model_name="asset",
            name="send_fee_percent",
            field=models.DecimalField(
                blank=True,
                decimal_places=7,
                max_digits=30,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.AddField(
            model_name="asset",
            name="send_max_amount",
            field=models.DecimalField(
                blank=True, decimal_places=7, default=999999999999999999, max_digits=30
            ),
        ),
        migrations.AddField(
            model_name="asset",
            name="send_min_amount",
            field=models.DecimalField(
                blank=True, decimal_places=7, default=0, max_digits=30
            ),
        ),
        migrations.AddField(
            model_name="asset",
            name="sep31_enabled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="transaction",
            name="send_memo",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="transaction",
            name="send_memo_type",
            field=models.CharField(
                choices=Transaction.MEMO_TYPES,
                default=Transaction.MEMO_TYPES.text,
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="send_anchor_account",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="kind",
            field=models.CharField(
                choices=[
                    ("deposit", "deposit"),
                    ("withdrawal", "withdrawal"),
                    ("send", "send"),
                ],
                default="deposit",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="protocol",
            field=models.CharField(
                choices=[("sep6", "sep6"), ("sep24", "sep24"), ("sep31", "sep31")],
                max_length=5,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending_anchor", "pending_anchor"),
                    ("pending_trust", "pending_trust"),
                    ("pending_user", "pending_user"),
                    ("pending_user_transfer_start", "pending_user_transfer_start"),
                    ("incomplete", "incomplete"),
                    ("no_market", "no_market"),
                    ("too_small", "too_small"),
                    ("too_large", "too_large"),
                    ("pending_sender", "pending_sender"),
                    ("pending_receiver", "pending_receiver"),
                    ("pending_info_update", "pending_info_update"),
                    ("completed", "completed"),
                    ("error", "error"),
                    ("pending_external", "pending_external"),
                    ("pending_stellar", "pending_stellar"),
                ],
                default="pending_external",
                max_length=30,
            ),
        ),
        migrations.RenameField(
            model_name="transaction",
            old_name="external_extra_text",
            new_name="required_info_message",
        ),
        migrations.RenameField(
            model_name="transaction",
            old_name="external_extra",
            new_name="required_info_update",
        ),
        migrations.AlterField(
            model_name="transaction",
            name="status_eta",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]