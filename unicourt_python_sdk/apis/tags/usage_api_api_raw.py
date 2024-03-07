# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.billing_cycle_usage_billing_cycle.get import GetApiUsageByBillingCycleRaw
from unicourt_python_sdk.paths.daily_usage_date.get import GetApiUsageByDateRaw
from unicourt_python_sdk.paths.billing_cycles.get import ListPreviousBillingCyclesRaw


class UsageAPIApiRaw(
    GetApiUsageByBillingCycleRaw,
    GetApiUsageByDateRaw,
    ListPreviousBillingCyclesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass