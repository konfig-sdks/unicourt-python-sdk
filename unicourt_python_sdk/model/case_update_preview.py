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


class CaseUpdatePreview(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "exception",
            "pacerOptions",
            "caseId",
            "caseAPI",
            "requestedDate",
            "object",
            "status",
        }
        
        class properties:
            
            
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
        
            @staticmethod
            def exception() -> typing.Type['Exception']:
                return Exception
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 17
                    min_length = 17
        
            @staticmethod
            def pacerOptions() -> typing.Type['CaseUpdatePacerOptionsResponse']:
                return CaseUpdatePacerOptionsResponse
            
            
            class requestedDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 11
                    min_length = 7
                    enum_value_to_name = {
                        "COMPLETE": "COMPLETE",
                        "FAILURE": "FAILURE",
                        "IN_PROGRESS": "IN_PROGRESS",
                    }
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("COMPLETE")
                
                @schemas.classproperty
                def FAILURE(cls):
                    return cls("FAILURE")
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("IN_PROGRESS")
            __annotations__ = {
                "caseAPI": caseAPI,
                "caseId": caseId,
                "exception": exception,
                "object": object,
                "pacerOptions": pacerOptions,
                "requestedDate": requestedDate,
                "status": status,
            }
    
    exception: 'Exception'
    pacerOptions: 'CaseUpdatePacerOptionsResponse'
    caseId: MetaOapg.properties.caseId
    caseAPI: MetaOapg.properties.caseAPI
    requestedDate: MetaOapg.properties.requestedDate
    object: MetaOapg.properties.object
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseAPI"]) -> MetaOapg.properties.caseAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseId"]) -> MetaOapg.properties.caseId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exception"]) -> 'Exception': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pacerOptions"]) -> 'CaseUpdatePacerOptionsResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestedDate"]) -> MetaOapg.properties.requestedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caseAPI", "caseId", "exception", "object", "pacerOptions", "requestedDate", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseAPI"]) -> MetaOapg.properties.caseAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseId"]) -> MetaOapg.properties.caseId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exception"]) -> 'Exception': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pacerOptions"]) -> 'CaseUpdatePacerOptionsResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestedDate"]) -> MetaOapg.properties.requestedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caseAPI", "caseId", "exception", "object", "pacerOptions", "requestedDate", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        exception: 'Exception',
        pacerOptions: 'CaseUpdatePacerOptionsResponse',
        caseId: typing.Union[MetaOapg.properties.caseId, str, ],
        caseAPI: typing.Union[MetaOapg.properties.caseAPI, str, ],
        requestedDate: typing.Union[MetaOapg.properties.requestedDate, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseUpdatePreview':
        return super().__new__(
            cls,
            *args,
            exception=exception,
            pacerOptions=pacerOptions,
            caseId=caseId,
            caseAPI=caseAPI,
            requestedDate=requestedDate,
            object=object,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from unicourt_python_sdk.model.exception import Exception
