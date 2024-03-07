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


class PossibleNormLawFirmSourceDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "linkedNormAttorneyIdArray",
            "source",
        }
        
        class properties:
        
            @staticmethod
            def linkedNormAttorneyIdArray() -> typing.Type['PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray']:
                return PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray
            
            
            class source(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Case_Attorney_Linked_In_Other_Cases": "LINKED_IN_OTHER_CASES",
                        "Case_Attorney_Field_Contains_Law_Firm": "FIELD_CONTAINS_LAW_FIRM",
                    }
                
                @schemas.classproperty
                def LINKED_IN_OTHER_CASES(cls):
                    return cls("Case_Attorney_Linked_In_Other_Cases")
                
                @schemas.classproperty
                def FIELD_CONTAINS_LAW_FIRM(cls):
                    return cls("Case_Attorney_Field_Contains_Law_Firm")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "linkedNormAttorneyIdArray": linkedNormAttorneyIdArray,
                "source": source,
            }
    
    linkedNormAttorneyIdArray: 'PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray'
    source: MetaOapg.properties.source
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkedNormAttorneyIdArray"]) -> 'PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["linkedNormAttorneyIdArray", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkedNormAttorneyIdArray"]) -> 'PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["linkedNormAttorneyIdArray", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        linkedNormAttorneyIdArray: 'PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray',
        source: typing.Union[MetaOapg.properties.source, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PossibleNormLawFirmSourceDetails':
        return super().__new__(
            cls,
            *args,
            linkedNormAttorneyIdArray=linkedNormAttorneyIdArray,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.possible_norm_law_firm_source_details_linked_norm_attorney_id_array import PossibleNormLawFirmSourceDetailsLinkedNormAttorneyIdArray