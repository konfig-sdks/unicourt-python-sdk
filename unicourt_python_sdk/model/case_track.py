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


class CaseTrack(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "lastFetchDate",
            "schedule",
            "pacerOptions",
            "lastFetchDateWithUpdates",
            "caseId",
            "caseAPI",
            "lastTrackedDetails",
            "case",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def case() -> typing.Type['Case']:
                return Case
            
            
            class caseAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
                    min_length = 1
            
            
            class caseId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class lastFetchDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastFetchDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class lastFetchDateWithUpdates(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastFetchDateWithUpdates':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def lastTrackedDetails() -> typing.Type['LastTrackedDetails']:
                return LastTrackedDetails
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 9
                    min_length = 9
        
            @staticmethod
            def pacerOptions() -> typing.Type['CaseUpdatePacerOptionsResponse']:
                return CaseUpdatePacerOptionsResponse
        
            @staticmethod
            def schedule() -> typing.Type['Schedule']:
                return Schedule
            __annotations__ = {
                "case": case,
                "caseAPI": caseAPI,
                "caseId": caseId,
                "lastFetchDate": lastFetchDate,
                "lastFetchDateWithUpdates": lastFetchDateWithUpdates,
                "lastTrackedDetails": lastTrackedDetails,
                "object": object,
                "pacerOptions": pacerOptions,
                "schedule": schedule,
            }
    
    lastFetchDate: MetaOapg.properties.lastFetchDate
    schedule: 'Schedule'
    pacerOptions: 'CaseUpdatePacerOptionsResponse'
    lastFetchDateWithUpdates: MetaOapg.properties.lastFetchDateWithUpdates
    caseId: MetaOapg.properties.caseId
    caseAPI: MetaOapg.properties.caseAPI
    lastTrackedDetails: 'LastTrackedDetails'
    case: 'Case'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["case"]) -> 'Case': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseAPI"]) -> MetaOapg.properties.caseAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseId"]) -> MetaOapg.properties.caseId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDateWithUpdates"]) -> MetaOapg.properties.lastFetchDateWithUpdates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastTrackedDetails"]) -> 'LastTrackedDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pacerOptions"]) -> 'CaseUpdatePacerOptionsResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'Schedule': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["case", "caseAPI", "caseId", "lastFetchDate", "lastFetchDateWithUpdates", "lastTrackedDetails", "object", "pacerOptions", "schedule", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["case"]) -> 'Case': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseAPI"]) -> MetaOapg.properties.caseAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseId"]) -> MetaOapg.properties.caseId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDateWithUpdates"]) -> MetaOapg.properties.lastFetchDateWithUpdates: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastTrackedDetails"]) -> 'LastTrackedDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pacerOptions"]) -> 'CaseUpdatePacerOptionsResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> 'Schedule': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["case", "caseAPI", "caseId", "lastFetchDate", "lastFetchDateWithUpdates", "lastTrackedDetails", "object", "pacerOptions", "schedule", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, None, str, datetime, ],
        schedule: 'Schedule',
        pacerOptions: 'CaseUpdatePacerOptionsResponse',
        lastFetchDateWithUpdates: typing.Union[MetaOapg.properties.lastFetchDateWithUpdates, None, str, datetime, ],
        caseId: typing.Union[MetaOapg.properties.caseId, str, ],
        caseAPI: typing.Union[MetaOapg.properties.caseAPI, str, ],
        lastTrackedDetails: 'LastTrackedDetails',
        case: 'Case',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseTrack':
        return super().__new__(
            cls,
            *args,
            lastFetchDate=lastFetchDate,
            schedule=schedule,
            pacerOptions=pacerOptions,
            lastFetchDateWithUpdates=lastFetchDateWithUpdates,
            caseId=caseId,
            caseAPI=caseAPI,
            lastTrackedDetails=lastTrackedDetails,
            case=case,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case import Case
from unicourt_python_sdk.model.case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from unicourt_python_sdk.model.last_tracked_details import LastTrackedDetails
from unicourt_python_sdk.model.schedule import Schedule
