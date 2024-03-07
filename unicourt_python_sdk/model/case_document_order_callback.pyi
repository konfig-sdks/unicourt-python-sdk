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


class CaseDocumentOrderCallback(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "exception",
            "caseDocumentOrderCallbackAPI",
            "file",
            "caseDocument",
            "caseDocumentOrderCallbackId",
            "caseDocumentId",
            "callbackGeneratedDate",
            "object",
            "status",
        }
        
        class properties:
            
            
            class callbackGeneratedDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'callbackGeneratedDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def caseDocument() -> typing.Type['CaseDocument']:
                return CaseDocument
            
            
            class caseDocumentId(
                schemas.StrSchema
            ):
                pass
            
            
            class caseDocumentOrderCallbackAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class caseDocumentOrderCallbackId(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def exception() -> typing.Type['Exception']:
                return Exception
        
            @staticmethod
            def file() -> typing.Type['ExportFile']:
                return ExportFile
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("COMPLETE")
                
                @schemas.classproperty
                def FAILURE(cls):
                    return cls("FAILURE")
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("IN_PROGRESS")
            __annotations__ = {
                "callbackGeneratedDate": callbackGeneratedDate,
                "caseDocument": caseDocument,
                "caseDocumentId": caseDocumentId,
                "caseDocumentOrderCallbackAPI": caseDocumentOrderCallbackAPI,
                "caseDocumentOrderCallbackId": caseDocumentOrderCallbackId,
                "exception": exception,
                "file": file,
                "object": object,
                "status": status,
            }
    
    exception: 'Exception'
    caseDocumentOrderCallbackAPI: MetaOapg.properties.caseDocumentOrderCallbackAPI
    file: 'ExportFile'
    caseDocument: 'CaseDocument'
    caseDocumentOrderCallbackId: MetaOapg.properties.caseDocumentOrderCallbackId
    caseDocumentId: MetaOapg.properties.caseDocumentId
    callbackGeneratedDate: MetaOapg.properties.callbackGeneratedDate
    object: MetaOapg.properties.object
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callbackGeneratedDate"]) -> MetaOapg.properties.callbackGeneratedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseDocument"]) -> 'CaseDocument': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseDocumentId"]) -> MetaOapg.properties.caseDocumentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseDocumentOrderCallbackAPI"]) -> MetaOapg.properties.caseDocumentOrderCallbackAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseDocumentOrderCallbackId"]) -> MetaOapg.properties.caseDocumentOrderCallbackId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exception"]) -> 'Exception': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'ExportFile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["callbackGeneratedDate", "caseDocument", "caseDocumentId", "caseDocumentOrderCallbackAPI", "caseDocumentOrderCallbackId", "exception", "file", "object", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callbackGeneratedDate"]) -> MetaOapg.properties.callbackGeneratedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseDocument"]) -> 'CaseDocument': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseDocumentId"]) -> MetaOapg.properties.caseDocumentId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseDocumentOrderCallbackAPI"]) -> MetaOapg.properties.caseDocumentOrderCallbackAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseDocumentOrderCallbackId"]) -> MetaOapg.properties.caseDocumentOrderCallbackId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exception"]) -> 'Exception': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> 'ExportFile': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["callbackGeneratedDate", "caseDocument", "caseDocumentId", "caseDocumentOrderCallbackAPI", "caseDocumentOrderCallbackId", "exception", "file", "object", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        exception: 'Exception',
        caseDocumentOrderCallbackAPI: typing.Union[MetaOapg.properties.caseDocumentOrderCallbackAPI, str, ],
        file: 'ExportFile',
        caseDocument: 'CaseDocument',
        caseDocumentOrderCallbackId: typing.Union[MetaOapg.properties.caseDocumentOrderCallbackId, str, ],
        caseDocumentId: typing.Union[MetaOapg.properties.caseDocumentId, str, ],
        callbackGeneratedDate: typing.Union[MetaOapg.properties.callbackGeneratedDate, None, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseDocumentOrderCallback':
        return super().__new__(
            cls,
            *args,
            exception=exception,
            caseDocumentOrderCallbackAPI=caseDocumentOrderCallbackAPI,
            file=file,
            caseDocument=caseDocument,
            caseDocumentOrderCallbackId=caseDocumentOrderCallbackId,
            caseDocumentId=caseDocumentId,
            callbackGeneratedDate=callbackGeneratedDate,
            object=object,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_document import CaseDocument
from unicourt_python_sdk.model.exception import Exception
from unicourt_python_sdk.model.export_file import ExportFile
