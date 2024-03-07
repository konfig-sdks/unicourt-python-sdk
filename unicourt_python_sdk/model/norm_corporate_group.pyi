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


class NormCorporateGroup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "normCorporateGroupName",
            "normCorporateGroupId",
            "object",
        }
        
        class properties:
            
            
            class normCorporateGroupId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normCorporateGroupId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class normCorporateGroupName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normCorporateGroupName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "normCorporateGroupId": normCorporateGroupId,
                "normCorporateGroupName": normCorporateGroupName,
                "object": object,
            }
    
    normCorporateGroupName: MetaOapg.properties.normCorporateGroupName
    normCorporateGroupId: MetaOapg.properties.normCorporateGroupId
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normCorporateGroupId"]) -> MetaOapg.properties.normCorporateGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normCorporateGroupName"]) -> MetaOapg.properties.normCorporateGroupName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["normCorporateGroupId", "normCorporateGroupName", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normCorporateGroupId"]) -> MetaOapg.properties.normCorporateGroupId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normCorporateGroupName"]) -> MetaOapg.properties.normCorporateGroupName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["normCorporateGroupId", "normCorporateGroupName", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        normCorporateGroupName: typing.Union[MetaOapg.properties.normCorporateGroupName, None, str, ],
        normCorporateGroupId: typing.Union[MetaOapg.properties.normCorporateGroupId, None, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NormCorporateGroup':
        return super().__new__(
            cls,
            *args,
            normCorporateGroupName=normCorporateGroupName,
            normCorporateGroupId=normCorporateGroupId,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
