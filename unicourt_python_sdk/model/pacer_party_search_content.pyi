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


class PACERPartySearchContent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "pclFirstName",
            "pclPartyRole",
            "pclCaseId",
            "pclCourtId",
            "pclPartyType",
            "pclCaseOffice",
            "pclCaseNumberFull",
            "pclCaseNumber",
            "pclCaseType",
            "pclCaseYear",
            "pclLastName",
            "pclCourtCase",
            "pclJurisdictionType",
            "pclMiddleName",
            "pclCaseTitle",
            "pclGeneration",
            "pclDateFiled",
            "object",
        }
        
        class properties:
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            pclCaseId = schemas.IntSchema
            pclCaseNumber = schemas.IntSchema
            
            
            class pclCaseNumberFull(
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
                ) -> 'pclCaseNumberFull':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclCaseOffice(
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
                ) -> 'pclCaseOffice':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclCaseTitle(
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
                ) -> 'pclCaseTitle':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclCaseType(
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
                ) -> 'pclCaseType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            pclCaseYear = schemas.IntSchema
        
            @staticmethod
            def pclCourtCase() -> typing.Type['PACERCaseSearchContent']:
                return PACERCaseSearchContent
            
            
            class pclCourtId(
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
                ) -> 'pclCourtId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclDateFiled(
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
                ) -> 'pclDateFiled':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclFirstName(
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
                ) -> 'pclFirstName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclGeneration(
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
                ) -> 'pclGeneration':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclJurisdictionType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def APPELLATE(cls):
                    return cls("Appellate")
                
                @schemas.classproperty
                def BANKRUPTCY(cls):
                    return cls("Bankruptcy")
                
                @schemas.classproperty
                def CRIMINAL(cls):
                    return cls("Criminal")
                
                @schemas.classproperty
                def CIVIL(cls):
                    return cls("Civil")
                
                @schemas.classproperty
                def MULTIDISTRICT_LITIGATION(cls):
                    return cls("Multi-district Litigation")
            
            
            class pclLastName(
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
                ) -> 'pclLastName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclMiddleName(
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
                ) -> 'pclMiddleName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclPartyRole(
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
                ) -> 'pclPartyRole':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pclPartyType(
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
                ) -> 'pclPartyType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "object": object,
                "pclCaseId": pclCaseId,
                "pclCaseNumber": pclCaseNumber,
                "pclCaseNumberFull": pclCaseNumberFull,
                "pclCaseOffice": pclCaseOffice,
                "pclCaseTitle": pclCaseTitle,
                "pclCaseType": pclCaseType,
                "pclCaseYear": pclCaseYear,
                "pclCourtCase": pclCourtCase,
                "pclCourtId": pclCourtId,
                "pclDateFiled": pclDateFiled,
                "pclFirstName": pclFirstName,
                "pclGeneration": pclGeneration,
                "pclJurisdictionType": pclJurisdictionType,
                "pclLastName": pclLastName,
                "pclMiddleName": pclMiddleName,
                "pclPartyRole": pclPartyRole,
                "pclPartyType": pclPartyType,
            }
    
    pclFirstName: MetaOapg.properties.pclFirstName
    pclPartyRole: MetaOapg.properties.pclPartyRole
    pclCaseId: MetaOapg.properties.pclCaseId
    pclCourtId: MetaOapg.properties.pclCourtId
    pclPartyType: MetaOapg.properties.pclPartyType
    pclCaseOffice: MetaOapg.properties.pclCaseOffice
    pclCaseNumberFull: MetaOapg.properties.pclCaseNumberFull
    pclCaseNumber: MetaOapg.properties.pclCaseNumber
    pclCaseType: MetaOapg.properties.pclCaseType
    pclCaseYear: MetaOapg.properties.pclCaseYear
    pclLastName: MetaOapg.properties.pclLastName
    pclCourtCase: 'PACERCaseSearchContent'
    pclJurisdictionType: MetaOapg.properties.pclJurisdictionType
    pclMiddleName: MetaOapg.properties.pclMiddleName
    pclCaseTitle: MetaOapg.properties.pclCaseTitle
    pclGeneration: MetaOapg.properties.pclGeneration
    pclDateFiled: MetaOapg.properties.pclDateFiled
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseId"]) -> MetaOapg.properties.pclCaseId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseNumber"]) -> MetaOapg.properties.pclCaseNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseNumberFull"]) -> MetaOapg.properties.pclCaseNumberFull: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseOffice"]) -> MetaOapg.properties.pclCaseOffice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseTitle"]) -> MetaOapg.properties.pclCaseTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseType"]) -> MetaOapg.properties.pclCaseType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCaseYear"]) -> MetaOapg.properties.pclCaseYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCourtCase"]) -> 'PACERCaseSearchContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclCourtId"]) -> MetaOapg.properties.pclCourtId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclDateFiled"]) -> MetaOapg.properties.pclDateFiled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclFirstName"]) -> MetaOapg.properties.pclFirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclGeneration"]) -> MetaOapg.properties.pclGeneration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclJurisdictionType"]) -> MetaOapg.properties.pclJurisdictionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclLastName"]) -> MetaOapg.properties.pclLastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclMiddleName"]) -> MetaOapg.properties.pclMiddleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclPartyRole"]) -> MetaOapg.properties.pclPartyRole: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pclPartyType"]) -> MetaOapg.properties.pclPartyType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "pclCaseId", "pclCaseNumber", "pclCaseNumberFull", "pclCaseOffice", "pclCaseTitle", "pclCaseType", "pclCaseYear", "pclCourtCase", "pclCourtId", "pclDateFiled", "pclFirstName", "pclGeneration", "pclJurisdictionType", "pclLastName", "pclMiddleName", "pclPartyRole", "pclPartyType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseId"]) -> MetaOapg.properties.pclCaseId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseNumber"]) -> MetaOapg.properties.pclCaseNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseNumberFull"]) -> MetaOapg.properties.pclCaseNumberFull: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseOffice"]) -> MetaOapg.properties.pclCaseOffice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseTitle"]) -> MetaOapg.properties.pclCaseTitle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseType"]) -> MetaOapg.properties.pclCaseType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCaseYear"]) -> MetaOapg.properties.pclCaseYear: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCourtCase"]) -> 'PACERCaseSearchContent': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclCourtId"]) -> MetaOapg.properties.pclCourtId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclDateFiled"]) -> MetaOapg.properties.pclDateFiled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclFirstName"]) -> MetaOapg.properties.pclFirstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclGeneration"]) -> MetaOapg.properties.pclGeneration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclJurisdictionType"]) -> MetaOapg.properties.pclJurisdictionType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclLastName"]) -> MetaOapg.properties.pclLastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclMiddleName"]) -> MetaOapg.properties.pclMiddleName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclPartyRole"]) -> MetaOapg.properties.pclPartyRole: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pclPartyType"]) -> MetaOapg.properties.pclPartyType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "pclCaseId", "pclCaseNumber", "pclCaseNumberFull", "pclCaseOffice", "pclCaseTitle", "pclCaseType", "pclCaseYear", "pclCourtCase", "pclCourtId", "pclDateFiled", "pclFirstName", "pclGeneration", "pclJurisdictionType", "pclLastName", "pclMiddleName", "pclPartyRole", "pclPartyType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pclFirstName: typing.Union[MetaOapg.properties.pclFirstName, None, str, ],
        pclPartyRole: typing.Union[MetaOapg.properties.pclPartyRole, None, str, ],
        pclCaseId: typing.Union[MetaOapg.properties.pclCaseId, decimal.Decimal, int, ],
        pclCourtId: typing.Union[MetaOapg.properties.pclCourtId, None, str, ],
        pclPartyType: typing.Union[MetaOapg.properties.pclPartyType, None, str, ],
        pclCaseOffice: typing.Union[MetaOapg.properties.pclCaseOffice, None, str, ],
        pclCaseNumberFull: typing.Union[MetaOapg.properties.pclCaseNumberFull, None, str, ],
        pclCaseNumber: typing.Union[MetaOapg.properties.pclCaseNumber, decimal.Decimal, int, ],
        pclCaseType: typing.Union[MetaOapg.properties.pclCaseType, None, str, ],
        pclCaseYear: typing.Union[MetaOapg.properties.pclCaseYear, decimal.Decimal, int, ],
        pclLastName: typing.Union[MetaOapg.properties.pclLastName, None, str, ],
        pclCourtCase: 'PACERCaseSearchContent',
        pclJurisdictionType: typing.Union[MetaOapg.properties.pclJurisdictionType, str, ],
        pclMiddleName: typing.Union[MetaOapg.properties.pclMiddleName, None, str, ],
        pclCaseTitle: typing.Union[MetaOapg.properties.pclCaseTitle, None, str, ],
        pclGeneration: typing.Union[MetaOapg.properties.pclGeneration, None, str, ],
        pclDateFiled: typing.Union[MetaOapg.properties.pclDateFiled, None, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PACERPartySearchContent':
        return super().__new__(
            cls,
            *args,
            pclFirstName=pclFirstName,
            pclPartyRole=pclPartyRole,
            pclCaseId=pclCaseId,
            pclCourtId=pclCourtId,
            pclPartyType=pclPartyType,
            pclCaseOffice=pclCaseOffice,
            pclCaseNumberFull=pclCaseNumberFull,
            pclCaseNumber=pclCaseNumber,
            pclCaseType=pclCaseType,
            pclCaseYear=pclCaseYear,
            pclLastName=pclLastName,
            pclCourtCase=pclCourtCase,
            pclJurisdictionType=pclJurisdictionType,
            pclMiddleName=pclMiddleName,
            pclCaseTitle=pclCaseTitle,
            pclGeneration=pclGeneration,
            pclDateFiled=pclDateFiled,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.pacer_case_search_content import PACERCaseSearchContent
