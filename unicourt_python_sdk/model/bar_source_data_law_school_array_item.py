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


class BarSourceDataLawSchoolArrayItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "lawSchoolGraduatedDate",
            "lawSchool",
        }
        
        class properties:
            
            
            class lawSchool(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 250
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lawSchool':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class lawSchoolGraduatedDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lawSchoolGraduatedDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "lawSchool": lawSchool,
                "lawSchoolGraduatedDate": lawSchoolGraduatedDate,
            }
    
    lawSchoolGraduatedDate: MetaOapg.properties.lawSchoolGraduatedDate
    lawSchool: MetaOapg.properties.lawSchool
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lawSchool"]) -> MetaOapg.properties.lawSchool: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lawSchoolGraduatedDate"]) -> MetaOapg.properties.lawSchoolGraduatedDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lawSchool", "lawSchoolGraduatedDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lawSchool"]) -> MetaOapg.properties.lawSchool: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lawSchoolGraduatedDate"]) -> MetaOapg.properties.lawSchoolGraduatedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lawSchool", "lawSchoolGraduatedDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lawSchoolGraduatedDate: typing.Union[MetaOapg.properties.lawSchoolGraduatedDate, None, str, datetime, ],
        lawSchool: typing.Union[MetaOapg.properties.lawSchool, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BarSourceDataLawSchoolArrayItem':
        return super().__new__(
            cls,
            *args,
            lawSchoolGraduatedDate=lawSchoolGraduatedDate,
            lawSchool=lawSchool,
            _configuration=_configuration,
            **kwargs,
        )