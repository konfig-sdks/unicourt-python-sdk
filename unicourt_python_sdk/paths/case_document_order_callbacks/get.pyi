# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from unicourt_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from unicourt_python_sdk.api_response import AsyncGeneratorResponse
from unicourt_python_sdk import api_client, exceptions
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

from unicourt_python_sdk.model.exception import Exception as ExceptionSchema
from unicourt_python_sdk.model.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse as CaseDocumentOrderCallbackListResponseSchema

from unicourt_python_sdk.type.exception import Exception
from unicourt_python_sdk.type.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse

from ...api_client import Dictionary
from unicourt_python_sdk.pydantic.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse as CaseDocumentOrderCallbackListResponsePydantic
from unicourt_python_sdk.pydantic.exception import Exception as ExceptionPydantic

# Query params


class DateSchema(
    schemas.DateTimeSchema
):
    pass


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def IN_PROGRESS(cls):
        return cls("IN_PROGRESS")
    
    @schemas.classproperty
    def COMPLETE(cls):
        return cls("COMPLETE")
    
    @schemas.classproperty
    def FAILURE(cls):
        return cls("FAILURE")


class PageNumberSchema(
    schemas.IntSchema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'date': typing.Union[DateSchema, str, datetime, ],
        'status': typing.Union[StatusSchema, str, ],
        'pageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_page_number = api_client.QueryParameter(
    name="pageNumber",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = CaseDocumentOrderCallbackListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CaseDocumentOrderCallbackListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CaseDocumentOrderCallbackListResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ExceptionSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Exception


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Exception


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ExceptionSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: Exception


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: Exception


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_document_order_callbacks_mapped_args(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if date is not None:
            _query_params["date"] = date
        if status is not None:
            _query_params["status"] = status
        if page_number is not None:
            _query_params["pageNumber"] = page_number
        args.query = _query_params
        return args

    async def _alist_document_order_callbacks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Case Document Order Callback list for a requested Date.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_date,
            request_query_status,
            request_query_page_number,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/caseDocumentOrder/callbacks',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_document_order_callbacks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Case Document Order Callback list for a requested Date.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_date,
            request_query_status,
            request_query_page_number,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/caseDocumentOrder/callbacks',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListDocumentOrderCallbacksRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_document_order_callbacks(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_document_order_callbacks_mapped_args(
            date=date,
            status=status,
            page_number=page_number,
        )
        return await self._alist_document_order_callbacks_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_document_order_callbacks(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_document_order_callbacks_mapped_args(
            date=date,
            status=status,
            page_number=page_number,
        )
        return self._list_document_order_callbacks_oapg(
            query_params=args.query,
        )

class ListDocumentOrderCallbacks(BaseApi):

    async def alist_document_order_callbacks(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> CaseDocumentOrderCallbackListResponsePydantic:
        raw_response = await self.raw.alist_document_order_callbacks(
            date=date,
            status=status,
            page_number=page_number,
            **kwargs,
        )
        if validate:
            return CaseDocumentOrderCallbackListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CaseDocumentOrderCallbackListResponsePydantic, raw_response.body)
    
    
    def list_document_order_callbacks(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        validate: bool = False,
    ) -> CaseDocumentOrderCallbackListResponsePydantic:
        raw_response = self.raw.list_document_order_callbacks(
            date=date,
            status=status,
            page_number=page_number,
        )
        if validate:
            return CaseDocumentOrderCallbackListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CaseDocumentOrderCallbackListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_document_order_callbacks_mapped_args(
            date=date,
            status=status,
            page_number=page_number,
        )
        return await self._alist_document_order_callbacks_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_document_order_callbacks_mapped_args(
            date=date,
            status=status,
            page_number=page_number,
        )
        return self._list_document_order_callbacks_oapg(
            query_params=args.query,
        )

