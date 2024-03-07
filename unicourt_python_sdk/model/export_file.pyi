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


class ExportFile(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "expiryDate",
            "name",
            "fileUrl",
            "object",
        }
        
        class properties:
            
            
            class expiryDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class fileUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "expiryDate": expiryDate,
                "fileUrl": fileUrl,
                "name": name,
                "object": object,
            }

    
    expiryDate: MetaOapg.properties.expiryDate
    name: MetaOapg.properties.name
    fileUrl: MetaOapg.properties.fileUrl
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryDate"]) -> MetaOapg.properties.expiryDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileUrl"]) -> MetaOapg.properties.fileUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expiryDate", "fileUrl", "name", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryDate"]) -> MetaOapg.properties.expiryDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileUrl"]) -> MetaOapg.properties.fileUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expiryDate", "fileUrl", "name", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExportFile':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
