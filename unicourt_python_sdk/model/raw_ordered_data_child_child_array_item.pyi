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


class RawOrderedDataChildChildArrayItem(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contact object Data Schema.
    """


    class MetaOapg:
        required = {
            "ord",
            "val",
            "childArray",
            "lbl",
        }
        
        class properties:
        
            @staticmethod
            def childArray() -> typing.Type['RawOrderedDataChildChildArrayItemChildArray']:
                return RawOrderedDataChildChildArrayItemChildArray
            
            
            class lbl(
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
                ) -> 'lbl':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            ord = schemas.IntSchema
            
            
            class val(
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
                ) -> 'val':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "childArray": childArray,
                "lbl": lbl,
                "ord": ord,
                "val": val,
            }

    
    ord: MetaOapg.properties.ord
    val: MetaOapg.properties.val
    childArray: 'RawOrderedDataChildChildArrayItemChildArray'
    lbl: MetaOapg.properties.lbl
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["childArray"]) -> 'RawOrderedDataChildChildArrayItemChildArray': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lbl"]) -> MetaOapg.properties.lbl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ord"]) -> MetaOapg.properties.ord: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["val"]) -> MetaOapg.properties.val: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["childArray", "lbl", "ord", "val", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["childArray"]) -> 'RawOrderedDataChildChildArrayItemChildArray': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lbl"]) -> MetaOapg.properties.lbl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ord"]) -> MetaOapg.properties.ord: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["val"]) -> MetaOapg.properties.val: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["childArray", "lbl", "ord", "val", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RawOrderedDataChildChildArrayItem':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.raw_ordered_data_child_child_array_item_child_array import RawOrderedDataChildChildArrayItemChildArray
