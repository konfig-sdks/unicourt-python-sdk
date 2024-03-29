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


class Address(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Address object Data Schema
    """


    class MetaOapg:
        required = {
            "zip",
            "city",
            "latitude",
            "streetAddress1",
            "streetAddress2",
            "zip4",
            "isVisible",
            "lastFetchDate",
            "stateName",
            "countryCode",
            "stateCode",
            "countryName",
            "firstFetchDate",
            "longitude",
            "object",
        }
        
        class properties:
            
            
            class city(
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
                ) -> 'city':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class countryCode(
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
                ) -> 'countryCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class countryName(
                schemas.StrSchema
            ):
                pass
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
                pass
            isVisible = schemas.BoolSchema
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class latitude(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'latitude':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class longitude(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'longitude':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class stateCode(
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
                ) -> 'stateCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class stateName(
                schemas.StrSchema
            ):
                pass
            
            
            class streetAddress1(
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
                ) -> 'streetAddress1':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class streetAddress2(
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
                ) -> 'streetAddress2':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class zip(
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
                ) -> 'zip':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class zip4(
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
                ) -> 'zip4':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "city": city,
                "countryCode": countryCode,
                "countryName": countryName,
                "firstFetchDate": firstFetchDate,
                "isVisible": isVisible,
                "lastFetchDate": lastFetchDate,
                "latitude": latitude,
                "longitude": longitude,
                "object": object,
                "stateCode": stateCode,
                "stateName": stateName,
                "streetAddress1": streetAddress1,
                "streetAddress2": streetAddress2,
                "zip": zip,
                "zip4": zip4,
            }
    
    zip: MetaOapg.properties.zip
    city: MetaOapg.properties.city
    latitude: MetaOapg.properties.latitude
    streetAddress1: MetaOapg.properties.streetAddress1
    streetAddress2: MetaOapg.properties.streetAddress2
    zip4: MetaOapg.properties.zip4
    isVisible: MetaOapg.properties.isVisible
    lastFetchDate: MetaOapg.properties.lastFetchDate
    stateName: MetaOapg.properties.stateName
    countryCode: MetaOapg.properties.countryCode
    stateCode: MetaOapg.properties.stateCode
    countryName: MetaOapg.properties.countryName
    firstFetchDate: MetaOapg.properties.firstFetchDate
    longitude: MetaOapg.properties.longitude
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateCode"]) -> MetaOapg.properties.stateCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateName"]) -> MetaOapg.properties.stateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetAddress1"]) -> MetaOapg.properties.streetAddress1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetAddress2"]) -> MetaOapg.properties.streetAddress2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip4"]) -> MetaOapg.properties.zip4: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["city", "countryCode", "countryName", "firstFetchDate", "isVisible", "lastFetchDate", "latitude", "longitude", "object", "stateCode", "stateName", "streetAddress1", "streetAddress2", "zip", "zip4", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateCode"]) -> MetaOapg.properties.stateCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateName"]) -> MetaOapg.properties.stateName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetAddress1"]) -> MetaOapg.properties.streetAddress1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetAddress2"]) -> MetaOapg.properties.streetAddress2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip4"]) -> MetaOapg.properties.zip4: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["city", "countryCode", "countryName", "firstFetchDate", "isVisible", "lastFetchDate", "latitude", "longitude", "object", "stateCode", "stateName", "streetAddress1", "streetAddress2", "zip", "zip4", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        zip: typing.Union[MetaOapg.properties.zip, None, str, ],
        city: typing.Union[MetaOapg.properties.city, None, str, ],
        latitude: typing.Union[MetaOapg.properties.latitude, None, decimal.Decimal, int, float, ],
        streetAddress1: typing.Union[MetaOapg.properties.streetAddress1, None, str, ],
        streetAddress2: typing.Union[MetaOapg.properties.streetAddress2, None, str, ],
        zip4: typing.Union[MetaOapg.properties.zip4, None, str, ],
        isVisible: typing.Union[MetaOapg.properties.isVisible, bool, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, str, datetime, ],
        stateName: typing.Union[MetaOapg.properties.stateName, str, ],
        countryCode: typing.Union[MetaOapg.properties.countryCode, None, str, ],
        stateCode: typing.Union[MetaOapg.properties.stateCode, None, str, ],
        countryName: typing.Union[MetaOapg.properties.countryName, str, ],
        firstFetchDate: typing.Union[MetaOapg.properties.firstFetchDate, str, datetime, ],
        longitude: typing.Union[MetaOapg.properties.longitude, None, decimal.Decimal, int, float, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Address':
        return super().__new__(
            cls,
            *args,
            zip=zip,
            city=city,
            latitude=latitude,
            streetAddress1=streetAddress1,
            streetAddress2=streetAddress2,
            zip4=zip4,
            isVisible=isVisible,
            lastFetchDate=lastFetchDate,
            stateName=stateName,
            countryCode=countryCode,
            stateCode=stateCode,
            countryName=countryName,
            firstFetchDate=firstFetchDate,
            longitude=longitude,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
