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


class BarSourceDataFeesOptionsArrayItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "slidingScaleFees",
            "flatFees",
            "hourlyRate",
            "paymentPlans",
            "contingencyFees",
        }
        
        class properties:
            
            
            class contingencyFees(
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
                ) -> 'contingencyFees':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class flatFees(
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
                ) -> 'flatFees':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class hourlyRate(
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
                ) -> 'hourlyRate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class paymentPlans(
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
                ) -> 'paymentPlans':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class slidingScaleFees(
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
                ) -> 'slidingScaleFees':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "contingencyFees": contingencyFees,
                "flatFees": flatFees,
                "hourlyRate": hourlyRate,
                "paymentPlans": paymentPlans,
                "slidingScaleFees": slidingScaleFees,
            }
    
    slidingScaleFees: MetaOapg.properties.slidingScaleFees
    flatFees: MetaOapg.properties.flatFees
    hourlyRate: MetaOapg.properties.hourlyRate
    paymentPlans: MetaOapg.properties.paymentPlans
    contingencyFees: MetaOapg.properties.contingencyFees
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contingencyFees"]) -> MetaOapg.properties.contingencyFees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flatFees"]) -> MetaOapg.properties.flatFees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlyRate"]) -> MetaOapg.properties.hourlyRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentPlans"]) -> MetaOapg.properties.paymentPlans: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slidingScaleFees"]) -> MetaOapg.properties.slidingScaleFees: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contingencyFees", "flatFees", "hourlyRate", "paymentPlans", "slidingScaleFees", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contingencyFees"]) -> MetaOapg.properties.contingencyFees: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flatFees"]) -> MetaOapg.properties.flatFees: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlyRate"]) -> MetaOapg.properties.hourlyRate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentPlans"]) -> MetaOapg.properties.paymentPlans: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slidingScaleFees"]) -> MetaOapg.properties.slidingScaleFees: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contingencyFees", "flatFees", "hourlyRate", "paymentPlans", "slidingScaleFees", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        slidingScaleFees: typing.Union[MetaOapg.properties.slidingScaleFees, None, str, ],
        flatFees: typing.Union[MetaOapg.properties.flatFees, None, str, ],
        hourlyRate: typing.Union[MetaOapg.properties.hourlyRate, None, str, ],
        paymentPlans: typing.Union[MetaOapg.properties.paymentPlans, None, str, ],
        contingencyFees: typing.Union[MetaOapg.properties.contingencyFees, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BarSourceDataFeesOptionsArrayItem':
        return super().__new__(
            cls,
            *args,
            slidingScaleFees=slidingScaleFees,
            flatFees=flatFees,
            hourlyRate=hourlyRate,
            paymentPlans=paymentPlans,
            contingencyFees=contingencyFees,
            _configuration=_configuration,
            **kwargs,
        )
