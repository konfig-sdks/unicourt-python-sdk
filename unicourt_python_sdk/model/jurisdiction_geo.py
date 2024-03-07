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


class JurisdictionGeo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "country",
            "createdDate",
            "city",
            "county",
            "fipsCode",
            "jurisdictionGeoId",
            "state",
            "courtsForJurisdictionGeoAPI",
            "zipCodeArray",
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
                    max_length = 255
                    min_length = 1
            
            
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
            
            
            class country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
            
            
            class county(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'county':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class courtsForJurisdictionGeoAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
                    min_length = 1
            
            
            class createdDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
            class fipsCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
            
            
            class jurisdictionGeoId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 15
                    min_length = 15
            
            
            class state(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
        
            @staticmethod
            def zipCodeArray() -> typing.Type['JurisdictionGeoZipCodeArray']:
                return JurisdictionGeoZipCodeArray
            __annotations__ = {
                "city": city,
                "country": country,
                "county": county,
                "courtsForJurisdictionGeoAPI": courtsForJurisdictionGeoAPI,
                "createdDate": createdDate,
                "fipsCode": fipsCode,
                "jurisdictionGeoId": jurisdictionGeoId,
                "object": object,
                "state": state,
                "zipCodeArray": zipCodeArray,
            }
    
    country: MetaOapg.properties.country
    createdDate: MetaOapg.properties.createdDate
    city: MetaOapg.properties.city
    county: MetaOapg.properties.county
    fipsCode: MetaOapg.properties.fipsCode
    jurisdictionGeoId: MetaOapg.properties.jurisdictionGeoId
    state: MetaOapg.properties.state
    courtsForJurisdictionGeoAPI: MetaOapg.properties.courtsForJurisdictionGeoAPI
    zipCodeArray: 'JurisdictionGeoZipCodeArray'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["county"]) -> MetaOapg.properties.county: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courtsForJurisdictionGeoAPI"]) -> MetaOapg.properties.courtsForJurisdictionGeoAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fipsCode"]) -> MetaOapg.properties.fipsCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jurisdictionGeoId"]) -> MetaOapg.properties.jurisdictionGeoId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipCodeArray"]) -> 'JurisdictionGeoZipCodeArray': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["city", "country", "county", "courtsForJurisdictionGeoAPI", "createdDate", "fipsCode", "jurisdictionGeoId", "object", "state", "zipCodeArray", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["county"]) -> MetaOapg.properties.county: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courtsForJurisdictionGeoAPI"]) -> MetaOapg.properties.courtsForJurisdictionGeoAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fipsCode"]) -> MetaOapg.properties.fipsCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jurisdictionGeoId"]) -> MetaOapg.properties.jurisdictionGeoId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipCodeArray"]) -> 'JurisdictionGeoZipCodeArray': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["city", "country", "county", "courtsForJurisdictionGeoAPI", "createdDate", "fipsCode", "jurisdictionGeoId", "object", "state", "zipCodeArray", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        createdDate: typing.Union[MetaOapg.properties.createdDate, str, datetime, ],
        city: typing.Union[MetaOapg.properties.city, None, str, ],
        county: typing.Union[MetaOapg.properties.county, None, str, ],
        fipsCode: typing.Union[MetaOapg.properties.fipsCode, str, ],
        jurisdictionGeoId: typing.Union[MetaOapg.properties.jurisdictionGeoId, str, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        courtsForJurisdictionGeoAPI: typing.Union[MetaOapg.properties.courtsForJurisdictionGeoAPI, str, ],
        zipCodeArray: 'JurisdictionGeoZipCodeArray',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JurisdictionGeo':
        return super().__new__(
            cls,
            *args,
            country=country,
            createdDate=createdDate,
            city=city,
            county=county,
            fipsCode=fipsCode,
            jurisdictionGeoId=jurisdictionGeoId,
            state=state,
            courtsForJurisdictionGeoAPI=courtsForJurisdictionGeoAPI,
            zipCodeArray=zipCodeArray,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.jurisdiction_geo_zip_code_array import JurisdictionGeoZipCodeArray
