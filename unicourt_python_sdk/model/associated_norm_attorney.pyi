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


class AssociatedNormAttorney(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "firstName",
            "lastName",
            "caseSearchAPI",
            "normAttorneyId",
            "name",
            "caseTimeline",
            "middleName",
            "stateBarDataArray",
            "caseCount",
            "normAttorneyAPI",
            "object",
        }
        
        class properties:
            caseCount = schemas.IntSchema
            
            
            class caseSearchAPI(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def caseTimeline() -> typing.Type['CaseTimeline']:
                return CaseTimeline
            
            
            class firstName(
                schemas.StrSchema
            ):
                pass
            
            
            class lastName(
                schemas.StrSchema
            ):
                pass
            
            
            class middleName(
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
                ) -> 'middleName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class normAttorneyAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class normAttorneyId(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class stateBarDataArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BarRecordPreview']:
                        return BarRecordPreview
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BarRecordPreview'], typing.List['BarRecordPreview']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stateBarDataArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BarRecordPreview':
                    return super().__getitem__(i)
            __annotations__ = {
                "caseCount": caseCount,
                "caseSearchAPI": caseSearchAPI,
                "caseTimeline": caseTimeline,
                "firstName": firstName,
                "lastName": lastName,
                "middleName": middleName,
                "name": name,
                "normAttorneyAPI": normAttorneyAPI,
                "normAttorneyId": normAttorneyId,
                "object": object,
                "stateBarDataArray": stateBarDataArray,
            }
    
    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    caseSearchAPI: MetaOapg.properties.caseSearchAPI
    normAttorneyId: MetaOapg.properties.normAttorneyId
    name: MetaOapg.properties.name
    caseTimeline: 'CaseTimeline'
    middleName: MetaOapg.properties.middleName
    stateBarDataArray: MetaOapg.properties.stateBarDataArray
    caseCount: MetaOapg.properties.caseCount
    normAttorneyAPI: MetaOapg.properties.normAttorneyAPI
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseTimeline"]) -> 'CaseTimeline': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneyAPI"]) -> MetaOapg.properties.normAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneyId"]) -> MetaOapg.properties.normAttorneyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateBarDataArray"]) -> MetaOapg.properties.stateBarDataArray: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caseCount", "caseSearchAPI", "caseTimeline", "firstName", "lastName", "middleName", "name", "normAttorneyAPI", "normAttorneyId", "object", "stateBarDataArray", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseTimeline"]) -> 'CaseTimeline': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneyAPI"]) -> MetaOapg.properties.normAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneyId"]) -> MetaOapg.properties.normAttorneyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateBarDataArray"]) -> MetaOapg.properties.stateBarDataArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caseCount", "caseSearchAPI", "caseTimeline", "firstName", "lastName", "middleName", "name", "normAttorneyAPI", "normAttorneyId", "object", "stateBarDataArray", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        caseSearchAPI: typing.Union[MetaOapg.properties.caseSearchAPI, str, ],
        normAttorneyId: typing.Union[MetaOapg.properties.normAttorneyId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        caseTimeline: 'CaseTimeline',
        middleName: typing.Union[MetaOapg.properties.middleName, None, str, ],
        stateBarDataArray: typing.Union[MetaOapg.properties.stateBarDataArray, list, tuple, ],
        caseCount: typing.Union[MetaOapg.properties.caseCount, decimal.Decimal, int, ],
        normAttorneyAPI: typing.Union[MetaOapg.properties.normAttorneyAPI, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssociatedNormAttorney':
        return super().__new__(
            cls,
            *args,
            firstName=firstName,
            lastName=lastName,
            caseSearchAPI=caseSearchAPI,
            normAttorneyId=normAttorneyId,
            name=name,
            caseTimeline=caseTimeline,
            middleName=middleName,
            stateBarDataArray=stateBarDataArray,
            caseCount=caseCount,
            normAttorneyAPI=normAttorneyAPI,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.bar_record_preview import BarRecordPreview
from unicourt_python_sdk.model.case_timeline import CaseTimeline
