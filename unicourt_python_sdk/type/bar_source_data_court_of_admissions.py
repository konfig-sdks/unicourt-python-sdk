# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from unicourt_python_sdk.type.bar_source_data_court_of_admissions_court_state_array import BarSourceDataCourtOfAdmissionsCourtStateArray
from unicourt_python_sdk.type.bar_source_data_court_of_admissions_federal_array import BarSourceDataCourtOfAdmissionsFederalArray
from unicourt_python_sdk.type.bar_source_data_court_of_admissions_other_courts_array import BarSourceDataCourtOfAdmissionsOtherCourtsArray

class RequiredBarSourceDataCourtOfAdmissions(TypedDict):
    courtStateArray: BarSourceDataCourtOfAdmissionsCourtStateArray

    federalArray: BarSourceDataCourtOfAdmissionsFederalArray

    otherCourtsArray: BarSourceDataCourtOfAdmissionsOtherCourtsArray

class OptionalBarSourceDataCourtOfAdmissions(TypedDict, total=False):
    pass

class BarSourceDataCourtOfAdmissions(RequiredBarSourceDataCourtOfAdmissions, OptionalBarSourceDataCourtOfAdmissions):
    pass
