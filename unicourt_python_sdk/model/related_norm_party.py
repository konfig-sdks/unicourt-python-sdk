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


class RelatedNormParty(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "relationshipType",
            "normPartyId",
            "object",
        }
        
        class properties:
            
            
            class normPartyId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 16
            
            
            class relationshipType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
                    enum_value_to_name = {
                        "Parent": "PARENT",
                        "Child": "CHILD",
                        "Same_Corporate_Group": "SAME_CORPORATE_GROUP",
                    }
                
                @schemas.classproperty
                def PARENT(cls):
                    return cls("Parent")
                
                @schemas.classproperty
                def CHILD(cls):
                    return cls("Child")
                
                @schemas.classproperty
                def SAME_CORPORATE_GROUP(cls):
                    return cls("Same_Corporate_Group")
            __annotations__ = {
                "normPartyId": normPartyId,
                "object": object,
                "relationshipType": relationshipType,
            }
    
    relationshipType: MetaOapg.properties.relationshipType
    normPartyId: MetaOapg.properties.normPartyId
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normPartyId"]) -> MetaOapg.properties.normPartyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationshipType"]) -> MetaOapg.properties.relationshipType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["normPartyId", "object", "relationshipType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normPartyId"]) -> MetaOapg.properties.normPartyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationshipType"]) -> MetaOapg.properties.relationshipType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["normPartyId", "object", "relationshipType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        relationshipType: typing.Union[MetaOapg.properties.relationshipType, str, ],
        normPartyId: typing.Union[MetaOapg.properties.normPartyId, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RelatedNormParty':
        return super().__new__(
            cls,
            *args,
            relationshipType=relationshipType,
            normPartyId=normPartyId,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
