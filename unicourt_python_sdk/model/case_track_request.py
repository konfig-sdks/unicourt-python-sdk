# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unicourt_python_sdk import schemas  # noqa: F401


class CaseTrackRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "caseTrackParams",
            "schedule",
        }
        
        class properties:
        
            @staticmethod
            def caseTrackParams() -> typing.Type['CaseUpdateRequest']:
                return CaseUpdateRequest
        
            @staticmethod
            def schedule() -> typing.Type['CaseTrackSchedule']:
                return CaseTrackSchedule
            __annotations__ = {
                "caseTrackParams": caseTrackParams,
                "schedule": schedule,
            }
    
    caseTrackParams: 'CaseUpdateRequest'
    schedule: 'CaseTrackSchedule'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseTrackParams"]) -> 'CaseUpdateRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'CaseTrackSchedule': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caseTrackParams", "schedule", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseTrackParams"]) -> 'CaseUpdateRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> 'CaseTrackSchedule': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caseTrackParams", "schedule", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        caseTrackParams: 'CaseUpdateRequest',
        schedule: 'CaseTrackSchedule',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseTrackRequest':
        return super().__new__(
            cls,
            *args,
            caseTrackParams=caseTrackParams,
            schedule=schedule,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_track_schedule import CaseTrackSchedule
from unicourt_python_sdk.model.case_update_request import CaseUpdateRequest
