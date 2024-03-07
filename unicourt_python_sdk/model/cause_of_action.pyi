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


class CauseOfAction(
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
            "createdDate",
            "causeOfActionGroupId",
            "name",
            "causeOfActionGroup",
            "causeOfActionId",
            "object",
        }
        
        class properties:
            
            
            class causeOfActionGroup(
                schemas.StrSchema
            ):
                pass
            
            
            class causeOfActionGroupId(
                schemas.StrSchema
            ):
                pass
            
            
            class causeOfActionId(
                schemas.StrSchema
            ):
                pass
            
            
            class createdDate(
                schemas.DateTimeSchema
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
                "causeOfActionGroup": causeOfActionGroup,
                "causeOfActionGroupId": causeOfActionGroupId,
                "causeOfActionId": causeOfActionId,
                "createdDate": createdDate,
                "name": name,
                "object": object,
            }

    
    createdDate: MetaOapg.properties.createdDate
    causeOfActionGroupId: MetaOapg.properties.causeOfActionGroupId
    name: MetaOapg.properties.name
    causeOfActionGroup: MetaOapg.properties.causeOfActionGroup
    causeOfActionId: MetaOapg.properties.causeOfActionId
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["causeOfActionGroup"]) -> MetaOapg.properties.causeOfActionGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["causeOfActionGroupId"]) -> MetaOapg.properties.causeOfActionGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["causeOfActionId"]) -> MetaOapg.properties.causeOfActionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["causeOfActionGroup", "causeOfActionGroupId", "causeOfActionId", "createdDate", "name", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["causeOfActionGroup"]) -> MetaOapg.properties.causeOfActionGroup: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["causeOfActionGroupId"]) -> MetaOapg.properties.causeOfActionGroupId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["causeOfActionId"]) -> MetaOapg.properties.causeOfActionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["causeOfActionGroup", "causeOfActionGroupId", "causeOfActionId", "createdDate", "name", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CauseOfAction':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )