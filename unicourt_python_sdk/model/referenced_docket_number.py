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


class ReferencedDocketNumber(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Object consisiting of each docket entry number and its corresponding API call.
    """


    class MetaOapg:
        required = {
            "docketEntriesAPI",
            "docketNumber",
            "object",
        }
        
        class properties:
            
            
            class docketEntriesAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'docketEntriesAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            docketNumber = schemas.IntSchema
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 22
                    min_length = 22
            __annotations__ = {
                "docketEntriesAPI": docketEntriesAPI,
                "docketNumber": docketNumber,
                "object": object,
            }

    
    docketEntriesAPI: MetaOapg.properties.docketEntriesAPI
    docketNumber: MetaOapg.properties.docketNumber
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["docketEntriesAPI"]) -> MetaOapg.properties.docketEntriesAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["docketNumber"]) -> MetaOapg.properties.docketNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["docketEntriesAPI", "docketNumber", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["docketEntriesAPI"]) -> MetaOapg.properties.docketEntriesAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["docketNumber"]) -> MetaOapg.properties.docketNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["docketEntriesAPI", "docketNumber", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReferencedDocketNumber':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
