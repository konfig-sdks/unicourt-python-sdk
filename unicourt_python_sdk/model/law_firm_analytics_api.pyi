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


class LawFirmAnalyticsAPI(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "associatedNormPartiesAPI",
            "associatedNormJudgeAPI",
            "caseCountAnalyticsByOpposingNormLawFirmAPI",
            "caseCountAnalyticsByOpposingNormAttorneyAPI",
            "associatedNormAttorneyAPI",
            "caseCountAnalyticsByOpposingNormPartyAPI",
            "normLawFirmAPI",
            "object",
        }
        
        class properties:
            
            
            class associatedNormAttorneyAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class associatedNormJudgeAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class associatedNormPartiesAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class caseCountAnalyticsByOpposingNormAttorneyAPI(
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
                ) -> 'caseCountAnalyticsByOpposingNormAttorneyAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class caseCountAnalyticsByOpposingNormLawFirmAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class caseCountAnalyticsByOpposingNormPartyAPI(
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
                ) -> 'caseCountAnalyticsByOpposingNormPartyAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class normLawFirmAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "associatedNormAttorneyAPI": associatedNormAttorneyAPI,
                "associatedNormJudgeAPI": associatedNormJudgeAPI,
                "associatedNormPartiesAPI": associatedNormPartiesAPI,
                "caseCountAnalyticsByOpposingNormAttorneyAPI": caseCountAnalyticsByOpposingNormAttorneyAPI,
                "caseCountAnalyticsByOpposingNormLawFirmAPI": caseCountAnalyticsByOpposingNormLawFirmAPI,
                "caseCountAnalyticsByOpposingNormPartyAPI": caseCountAnalyticsByOpposingNormPartyAPI,
                "normLawFirmAPI": normLawFirmAPI,
                "object": object,
            }
    
    associatedNormPartiesAPI: MetaOapg.properties.associatedNormPartiesAPI
    associatedNormJudgeAPI: MetaOapg.properties.associatedNormJudgeAPI
    caseCountAnalyticsByOpposingNormLawFirmAPI: MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI
    caseCountAnalyticsByOpposingNormAttorneyAPI: MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI
    associatedNormAttorneyAPI: MetaOapg.properties.associatedNormAttorneyAPI
    caseCountAnalyticsByOpposingNormPartyAPI: MetaOapg.properties.caseCountAnalyticsByOpposingNormPartyAPI
    normLawFirmAPI: MetaOapg.properties.normLawFirmAPI
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormAttorneyAPI"]) -> MetaOapg.properties.associatedNormAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormJudgeAPI"]) -> MetaOapg.properties.associatedNormJudgeAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormAttorneyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormLawFirmAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormPartyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormPartyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmAPI"]) -> MetaOapg.properties.normLawFirmAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["associatedNormAttorneyAPI", "associatedNormJudgeAPI", "associatedNormPartiesAPI", "caseCountAnalyticsByOpposingNormAttorneyAPI", "caseCountAnalyticsByOpposingNormLawFirmAPI", "caseCountAnalyticsByOpposingNormPartyAPI", "normLawFirmAPI", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormAttorneyAPI"]) -> MetaOapg.properties.associatedNormAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormJudgeAPI"]) -> MetaOapg.properties.associatedNormJudgeAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormAttorneyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormLawFirmAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormPartyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormPartyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmAPI"]) -> MetaOapg.properties.normLawFirmAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["associatedNormAttorneyAPI", "associatedNormJudgeAPI", "associatedNormPartiesAPI", "caseCountAnalyticsByOpposingNormAttorneyAPI", "caseCountAnalyticsByOpposingNormLawFirmAPI", "caseCountAnalyticsByOpposingNormPartyAPI", "normLawFirmAPI", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        associatedNormPartiesAPI: typing.Union[MetaOapg.properties.associatedNormPartiesAPI, str, ],
        associatedNormJudgeAPI: typing.Union[MetaOapg.properties.associatedNormJudgeAPI, str, ],
        caseCountAnalyticsByOpposingNormLawFirmAPI: typing.Union[MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI, str, ],
        caseCountAnalyticsByOpposingNormAttorneyAPI: typing.Union[MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI, None, str, ],
        associatedNormAttorneyAPI: typing.Union[MetaOapg.properties.associatedNormAttorneyAPI, str, ],
        caseCountAnalyticsByOpposingNormPartyAPI: typing.Union[MetaOapg.properties.caseCountAnalyticsByOpposingNormPartyAPI, None, str, ],
        normLawFirmAPI: typing.Union[MetaOapg.properties.normLawFirmAPI, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LawFirmAnalyticsAPI':
        return super().__new__(
            cls,
            *args,
            associatedNormPartiesAPI=associatedNormPartiesAPI,
            associatedNormJudgeAPI=associatedNormJudgeAPI,
            caseCountAnalyticsByOpposingNormLawFirmAPI=caseCountAnalyticsByOpposingNormLawFirmAPI,
            caseCountAnalyticsByOpposingNormAttorneyAPI=caseCountAnalyticsByOpposingNormAttorneyAPI,
            associatedNormAttorneyAPI=associatedNormAttorneyAPI,
            caseCountAnalyticsByOpposingNormPartyAPI=caseCountAnalyticsByOpposingNormPartyAPI,
            normLawFirmAPI=normLawFirmAPI,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
