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


class DocketEntrySecondaryDocuments(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Secondary Documents refers to documents that are attached to a docket entry. Secondary Documents could be specific to a courts or case type in courts. For isntance the below example is in PACER. PACER District Courts - Here the secondary document is one which is attached in the docket entry.
    """


    class MetaOapg:
        required = {
            "pageNumber",
            "nextPageAPI",
            "totalPages",
            "totalCount",
            "caseDocumentArray",
            "object",
        }
        
        class properties:
            
            
            class caseDocumentArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 100
                    
                    @staticmethod
                    def items() -> typing.Type['CaseDocument']:
                        return CaseDocument
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CaseDocument'], typing.List['CaseDocument']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'caseDocumentArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CaseDocument':
                    return super().__getitem__(i)
            
            
            class nextPageAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nextPageAPI':
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
                    min_length = 29
            pageNumber = schemas.IntSchema
            totalCount = schemas.IntSchema
            totalPages = schemas.IntSchema
            __annotations__ = {
                "caseDocumentArray": caseDocumentArray,
                "nextPageAPI": nextPageAPI,
                "object": object,
                "pageNumber": pageNumber,
                "totalCount": totalCount,
                "totalPages": totalPages,
            }

    
    pageNumber: MetaOapg.properties.pageNumber
    nextPageAPI: MetaOapg.properties.nextPageAPI
    totalPages: MetaOapg.properties.totalPages
    totalCount: MetaOapg.properties.totalCount
    caseDocumentArray: MetaOapg.properties.caseDocumentArray
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseDocumentArray"]) -> MetaOapg.properties.caseDocumentArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caseDocumentArray", "nextPageAPI", "object", "pageNumber", "totalCount", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseDocumentArray"]) -> MetaOapg.properties.caseDocumentArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caseDocumentArray", "nextPageAPI", "object", "pageNumber", "totalCount", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocketEntrySecondaryDocuments':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_document import CaseDocument
