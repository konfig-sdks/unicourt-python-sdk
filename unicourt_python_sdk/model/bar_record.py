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


class BarRecord(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    This contains the Attorney details that is obtained from the State Bar where the attorney is registered.
    """


    class MetaOapg:
        required = {
            "lastFetchDate",
            "barSourceData",
            "barNumber",
            "lastFetchDateWithUpdates",
            "contact",
            "barSourceType",
            "stateCode",
            "firstFetchDate",
            "inactivationDate",
            "admittedDate",
            "object",
            "status",
        }
        
        class properties:
            
            
            class admittedDate(
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
                ) -> 'admittedDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class barNumber(
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
                ) -> 'barNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def barSourceData() -> typing.Type['BarSourceData']:
                return BarSourceData
            
            
            class barSourceType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 70
        
            @staticmethod
            def contact() -> typing.Type['Contact']:
                return Contact
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
            
            
            class inactivationDate(
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
                ) -> 'inactivationDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
            
            
            class lastFetchDateWithUpdates(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 9
            
            
            class stateCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 15
                    enum_value_to_name = {
                        "Active": "ACTIVE",
                        "Inactive": "INACTIVE",
                        "Not Classified": "NOT_CLASSIFIED",
                        "Unknown": "UNKNOWN",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("Active")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("Inactive")
                
                @schemas.classproperty
                def NOT_CLASSIFIED(cls):
                    return cls("Not Classified")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("Unknown")
            __annotations__ = {
                "admittedDate": admittedDate,
                "barNumber": barNumber,
                "barSourceData": barSourceData,
                "barSourceType": barSourceType,
                "contact": contact,
                "firstFetchDate": firstFetchDate,
                "inactivationDate": inactivationDate,
                "lastFetchDate": lastFetchDate,
                "lastFetchDateWithUpdates": lastFetchDateWithUpdates,
                "object": object,
                "stateCode": stateCode,
                "status": status,
            }
    
    lastFetchDate: MetaOapg.properties.lastFetchDate
    barSourceData: 'BarSourceData'
    barNumber: MetaOapg.properties.barNumber
    lastFetchDateWithUpdates: MetaOapg.properties.lastFetchDateWithUpdates
    contact: 'Contact'
    barSourceType: MetaOapg.properties.barSourceType
    stateCode: MetaOapg.properties.stateCode
    firstFetchDate: MetaOapg.properties.firstFetchDate
    inactivationDate: MetaOapg.properties.inactivationDate
    admittedDate: MetaOapg.properties.admittedDate
    object: MetaOapg.properties.object
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admittedDate"]) -> MetaOapg.properties.admittedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["barNumber"]) -> MetaOapg.properties.barNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["barSourceData"]) -> 'BarSourceData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["barSourceType"]) -> MetaOapg.properties.barSourceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact"]) -> 'Contact': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inactivationDate"]) -> MetaOapg.properties.inactivationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDateWithUpdates"]) -> MetaOapg.properties.lastFetchDateWithUpdates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateCode"]) -> MetaOapg.properties.stateCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["admittedDate", "barNumber", "barSourceData", "barSourceType", "contact", "firstFetchDate", "inactivationDate", "lastFetchDate", "lastFetchDateWithUpdates", "object", "stateCode", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admittedDate"]) -> MetaOapg.properties.admittedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["barNumber"]) -> MetaOapg.properties.barNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["barSourceData"]) -> 'BarSourceData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["barSourceType"]) -> MetaOapg.properties.barSourceType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> 'Contact': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inactivationDate"]) -> MetaOapg.properties.inactivationDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDateWithUpdates"]) -> MetaOapg.properties.lastFetchDateWithUpdates: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateCode"]) -> MetaOapg.properties.stateCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["admittedDate", "barNumber", "barSourceData", "barSourceType", "contact", "firstFetchDate", "inactivationDate", "lastFetchDate", "lastFetchDateWithUpdates", "object", "stateCode", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, str, datetime, ],
        barSourceData: 'BarSourceData',
        barNumber: typing.Union[MetaOapg.properties.barNumber, None, str, ],
        lastFetchDateWithUpdates: typing.Union[MetaOapg.properties.lastFetchDateWithUpdates, str, datetime, ],
        contact: 'Contact',
        barSourceType: typing.Union[MetaOapg.properties.barSourceType, str, ],
        stateCode: typing.Union[MetaOapg.properties.stateCode, str, ],
        firstFetchDate: typing.Union[MetaOapg.properties.firstFetchDate, str, datetime, ],
        inactivationDate: typing.Union[MetaOapg.properties.inactivationDate, None, str, datetime, ],
        admittedDate: typing.Union[MetaOapg.properties.admittedDate, None, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BarRecord':
        return super().__new__(
            cls,
            *args,
            lastFetchDate=lastFetchDate,
            barSourceData=barSourceData,
            barNumber=barNumber,
            lastFetchDateWithUpdates=lastFetchDateWithUpdates,
            contact=contact,
            barSourceType=barSourceType,
            stateCode=stateCode,
            firstFetchDate=firstFetchDate,
            inactivationDate=inactivationDate,
            admittedDate=admittedDate,
            object=object,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.bar_source_data import BarSourceData
from unicourt_python_sdk.model.contact import Contact
