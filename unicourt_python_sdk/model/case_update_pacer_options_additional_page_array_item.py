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


class CaseUpdatePacerOptionsAdditionalPageArrayItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class fetchIfOlderThanDays(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            
            
            class page(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 15
                    min_length = 11
                    enum_value_to_name = {
                        "associatedCases": "ASSOCIATED_CASES",
                        "caseSummary": "CASE_SUMMARY",
                        "listOfCreditors": "LIST_OF_CREDITORS",
                    }
                
                @schemas.classproperty
                def ASSOCIATED_CASES(cls):
                    return cls("associatedCases")
                
                @schemas.classproperty
                def CASE_SUMMARY(cls):
                    return cls("caseSummary")
                
                @schemas.classproperty
                def LIST_OF_CREDITORS(cls):
                    return cls("listOfCreditors")
            __annotations__ = {
                "fetchIfOlderThanDays": fetchIfOlderThanDays,
                "page": page,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fetchIfOlderThanDays"]) -> MetaOapg.properties.fetchIfOlderThanDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fetchIfOlderThanDays", "page", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fetchIfOlderThanDays"]) -> typing.Union[MetaOapg.properties.fetchIfOlderThanDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fetchIfOlderThanDays", "page", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fetchIfOlderThanDays: typing.Union[MetaOapg.properties.fetchIfOlderThanDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseUpdatePacerOptionsAdditionalPageArrayItem':
        return super().__new__(
            cls,
            *args,
            fetchIfOlderThanDays=fetchIfOlderThanDays,
            page=page,
            _configuration=_configuration,
            **kwargs,
        )