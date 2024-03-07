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


class Court(
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
            "container",
            "courtServiceStatusAPI",
            "courtSystemId",
            "additionalLevels",
            "containerType",
            "type",
            "nameAka",
            "jurisdictionGeoForCourtAPI",
            "createdDate",
            "system",
            "courtLocationsForCourtAPI",
            "name",
            "appealCourtsForCourtAPI",
            "courtTypeId",
            "courtId",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def additionalLevels() -> typing.Type['AdditionalLevels']:
                return AdditionalLevels
            
            
            class appealCourtsForCourtAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'appealCourtsForCourtAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class container(
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
                ) -> 'container':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class containerType(
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
                ) -> 'containerType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class courtId(
                schemas.StrSchema
            ):
                pass
            
            
            class courtLocationsForCourtAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'courtLocationsForCourtAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class courtServiceStatusAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'courtServiceStatusAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class courtSystemId(
                schemas.StrSchema
            ):
                pass
            
            
            class courtTypeId(
                schemas.StrSchema
            ):
                pass
            
            
            class createdDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class jurisdictionGeoForCourtAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'jurisdictionGeoForCourtAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class nameAka(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class system(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "additionalLevels": additionalLevels,
                "appealCourtsForCourtAPI": appealCourtsForCourtAPI,
                "container": container,
                "containerType": containerType,
                "courtId": courtId,
                "courtLocationsForCourtAPI": courtLocationsForCourtAPI,
                "courtServiceStatusAPI": courtServiceStatusAPI,
                "courtSystemId": courtSystemId,
                "courtTypeId": courtTypeId,
                "createdDate": createdDate,
                "jurisdictionGeoForCourtAPI": jurisdictionGeoForCourtAPI,
                "name": name,
                "nameAka": nameAka,
                "object": object,
                "system": system,
                "type": type,
            }

    
    container: MetaOapg.properties.container
    courtServiceStatusAPI: MetaOapg.properties.courtServiceStatusAPI
    courtSystemId: MetaOapg.properties.courtSystemId
    additionalLevels: 'AdditionalLevels'
    containerType: MetaOapg.properties.containerType
    type: MetaOapg.properties.type
    nameAka: MetaOapg.properties.nameAka
    jurisdictionGeoForCourtAPI: MetaOapg.properties.jurisdictionGeoForCourtAPI
    createdDate: MetaOapg.properties.createdDate
    system: MetaOapg.properties.system
    courtLocationsForCourtAPI: MetaOapg.properties.courtLocationsForCourtAPI
    name: MetaOapg.properties.name
    appealCourtsForCourtAPI: MetaOapg.properties.appealCourtsForCourtAPI
    courtTypeId: MetaOapg.properties.courtTypeId
    courtId: MetaOapg.properties.courtId
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalLevels"]) -> 'AdditionalLevels': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appealCourtsForCourtAPI"]) -> MetaOapg.properties.appealCourtsForCourtAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["container"]) -> MetaOapg.properties.container: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containerType"]) -> MetaOapg.properties.containerType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courtId"]) -> MetaOapg.properties.courtId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courtLocationsForCourtAPI"]) -> MetaOapg.properties.courtLocationsForCourtAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courtServiceStatusAPI"]) -> MetaOapg.properties.courtServiceStatusAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courtSystemId"]) -> MetaOapg.properties.courtSystemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courtTypeId"]) -> MetaOapg.properties.courtTypeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jurisdictionGeoForCourtAPI"]) -> MetaOapg.properties.jurisdictionGeoForCourtAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameAka"]) -> MetaOapg.properties.nameAka: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["additionalLevels", "appealCourtsForCourtAPI", "container", "containerType", "courtId", "courtLocationsForCourtAPI", "courtServiceStatusAPI", "courtSystemId", "courtTypeId", "createdDate", "jurisdictionGeoForCourtAPI", "name", "nameAka", "object", "system", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalLevels"]) -> 'AdditionalLevels': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appealCourtsForCourtAPI"]) -> MetaOapg.properties.appealCourtsForCourtAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["container"]) -> MetaOapg.properties.container: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containerType"]) -> MetaOapg.properties.containerType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courtId"]) -> MetaOapg.properties.courtId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courtLocationsForCourtAPI"]) -> MetaOapg.properties.courtLocationsForCourtAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courtServiceStatusAPI"]) -> MetaOapg.properties.courtServiceStatusAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courtSystemId"]) -> MetaOapg.properties.courtSystemId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courtTypeId"]) -> MetaOapg.properties.courtTypeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jurisdictionGeoForCourtAPI"]) -> MetaOapg.properties.jurisdictionGeoForCourtAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameAka"]) -> MetaOapg.properties.nameAka: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["additionalLevels", "appealCourtsForCourtAPI", "container", "containerType", "courtId", "courtLocationsForCourtAPI", "courtServiceStatusAPI", "courtSystemId", "courtTypeId", "createdDate", "jurisdictionGeoForCourtAPI", "name", "nameAka", "object", "system", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Court':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.additional_levels import AdditionalLevels
