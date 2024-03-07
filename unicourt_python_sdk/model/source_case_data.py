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


class SourceCaseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Source data in the court website.
    """


    class MetaOapg:
        required = {
            "sourceCourt",
            "sourcePageData",
            "natureOfSuitArray",
            "sourceCaseType",
            "sourceCauseOfActionArray",
            "sourceCaseStatus",
            "sourceChargeArray",
            "object",
        }
        
        class properties:
            
            
            class natureOfSuitArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NatureOfSuit']:
                        return NatureOfSuit
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NatureOfSuit'], typing.List['NatureOfSuit']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'natureOfSuitArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NatureOfSuit':
                    return super().__getitem__(i)
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 14
                    min_length = 14
            
            
            class sourceCaseStatus(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
            
            
            class sourceCaseType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
            
            
            class sourceCauseOfActionArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SourceCauseOfAction']:
                        return SourceCauseOfAction
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SourceCauseOfAction'], typing.List['SourceCauseOfAction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourceCauseOfActionArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SourceCauseOfAction':
                    return super().__getitem__(i)
            
            
            class sourceChargeArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SourceCharge']:
                        return SourceCharge
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SourceCharge'], typing.List['SourceCharge']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourceChargeArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SourceCharge':
                    return super().__getitem__(i)
            
            
            class sourceCourt(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
            
            
            class sourcePageData(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SourcePageData']:
                        return SourcePageData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SourcePageData'], typing.List['SourcePageData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourcePageData':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SourcePageData':
                    return super().__getitem__(i)
            __annotations__ = {
                "natureOfSuitArray": natureOfSuitArray,
                "object": object,
                "sourceCaseStatus": sourceCaseStatus,
                "sourceCaseType": sourceCaseType,
                "sourceCauseOfActionArray": sourceCauseOfActionArray,
                "sourceChargeArray": sourceChargeArray,
                "sourceCourt": sourceCourt,
                "sourcePageData": sourcePageData,
            }
    
    sourceCourt: MetaOapg.properties.sourceCourt
    sourcePageData: MetaOapg.properties.sourcePageData
    natureOfSuitArray: MetaOapg.properties.natureOfSuitArray
    sourceCaseType: MetaOapg.properties.sourceCaseType
    sourceCauseOfActionArray: MetaOapg.properties.sourceCauseOfActionArray
    sourceCaseStatus: MetaOapg.properties.sourceCaseStatus
    sourceChargeArray: MetaOapg.properties.sourceChargeArray
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["natureOfSuitArray"]) -> MetaOapg.properties.natureOfSuitArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceCaseStatus"]) -> MetaOapg.properties.sourceCaseStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceCaseType"]) -> MetaOapg.properties.sourceCaseType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceCauseOfActionArray"]) -> MetaOapg.properties.sourceCauseOfActionArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceChargeArray"]) -> MetaOapg.properties.sourceChargeArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceCourt"]) -> MetaOapg.properties.sourceCourt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourcePageData"]) -> MetaOapg.properties.sourcePageData: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["natureOfSuitArray", "object", "sourceCaseStatus", "sourceCaseType", "sourceCauseOfActionArray", "sourceChargeArray", "sourceCourt", "sourcePageData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["natureOfSuitArray"]) -> MetaOapg.properties.natureOfSuitArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceCaseStatus"]) -> MetaOapg.properties.sourceCaseStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceCaseType"]) -> MetaOapg.properties.sourceCaseType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceCauseOfActionArray"]) -> MetaOapg.properties.sourceCauseOfActionArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceChargeArray"]) -> MetaOapg.properties.sourceChargeArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceCourt"]) -> MetaOapg.properties.sourceCourt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourcePageData"]) -> MetaOapg.properties.sourcePageData: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["natureOfSuitArray", "object", "sourceCaseStatus", "sourceCaseType", "sourceCauseOfActionArray", "sourceChargeArray", "sourceCourt", "sourcePageData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sourceCourt: typing.Union[MetaOapg.properties.sourceCourt, str, ],
        sourcePageData: typing.Union[MetaOapg.properties.sourcePageData, list, tuple, ],
        natureOfSuitArray: typing.Union[MetaOapg.properties.natureOfSuitArray, list, tuple, ],
        sourceCaseType: typing.Union[MetaOapg.properties.sourceCaseType, str, ],
        sourceCauseOfActionArray: typing.Union[MetaOapg.properties.sourceCauseOfActionArray, list, tuple, ],
        sourceCaseStatus: typing.Union[MetaOapg.properties.sourceCaseStatus, str, ],
        sourceChargeArray: typing.Union[MetaOapg.properties.sourceChargeArray, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceCaseData':
        return super().__new__(
            cls,
            *args,
            sourceCourt=sourceCourt,
            sourcePageData=sourcePageData,
            natureOfSuitArray=natureOfSuitArray,
            sourceCaseType=sourceCaseType,
            sourceCauseOfActionArray=sourceCauseOfActionArray,
            sourceCaseStatus=sourceCaseStatus,
            sourceChargeArray=sourceChargeArray,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.nature_of_suit import NatureOfSuit
from unicourt_python_sdk.model.source_cause_of_action import SourceCauseOfAction
from unicourt_python_sdk.model.source_charge import SourceCharge
from unicourt_python_sdk.model.source_page_data import SourcePageData
