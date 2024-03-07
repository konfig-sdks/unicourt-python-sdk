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


class SOSAssociatedNormOrganization(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "fromDate",
            "normOrganizationAPI",
            "relationshipType",
            "normOrganizationId",
            "toDate",
            "name",
            "object",
        }
        
        class properties:
            
            
            class fromDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 500
            
            
            class normOrganizationAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normOrganizationAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class normOrganizationId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normOrganizationId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 29
            
            
            class relationshipType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 6
                    enum_value_to_name = {
                        "Parent": "PARENT",
                        "Child": "CHILD",
                    }
                
                @schemas.classproperty
                def PARENT(cls):
                    return cls("Parent")
                
                @schemas.classproperty
                def CHILD(cls):
                    return cls("Child")
            
            
            class toDate(
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
                ) -> 'toDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "fromDate": fromDate,
                "name": name,
                "normOrganizationAPI": normOrganizationAPI,
                "normOrganizationId": normOrganizationId,
                "object": object,
                "relationshipType": relationshipType,
                "toDate": toDate,
            }
    
    fromDate: MetaOapg.properties.fromDate
    normOrganizationAPI: MetaOapg.properties.normOrganizationAPI
    relationshipType: MetaOapg.properties.relationshipType
    normOrganizationId: MetaOapg.properties.normOrganizationId
    toDate: MetaOapg.properties.toDate
    name: MetaOapg.properties.name
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromDate"]) -> MetaOapg.properties.fromDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normOrganizationAPI"]) -> MetaOapg.properties.normOrganizationAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normOrganizationId"]) -> MetaOapg.properties.normOrganizationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationshipType"]) -> MetaOapg.properties.relationshipType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toDate"]) -> MetaOapg.properties.toDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fromDate", "name", "normOrganizationAPI", "normOrganizationId", "object", "relationshipType", "toDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromDate"]) -> MetaOapg.properties.fromDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normOrganizationAPI"]) -> MetaOapg.properties.normOrganizationAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normOrganizationId"]) -> MetaOapg.properties.normOrganizationId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationshipType"]) -> MetaOapg.properties.relationshipType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toDate"]) -> MetaOapg.properties.toDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fromDate", "name", "normOrganizationAPI", "normOrganizationId", "object", "relationshipType", "toDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fromDate: typing.Union[MetaOapg.properties.fromDate, str, datetime, ],
        normOrganizationAPI: typing.Union[MetaOapg.properties.normOrganizationAPI, None, str, ],
        relationshipType: typing.Union[MetaOapg.properties.relationshipType, str, ],
        normOrganizationId: typing.Union[MetaOapg.properties.normOrganizationId, None, str, ],
        toDate: typing.Union[MetaOapg.properties.toDate, None, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SOSAssociatedNormOrganization':
        return super().__new__(
            cls,
            *args,
            fromDate=fromDate,
            normOrganizationAPI=normOrganizationAPI,
            relationshipType=relationshipType,
            normOrganizationId=normOrganizationId,
            toDate=toDate,
            name=name,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )