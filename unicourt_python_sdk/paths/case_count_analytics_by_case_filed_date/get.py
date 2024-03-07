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

from unicourt_python_sdk.model.case_count_analytics_by_case_filed_date_response import CaseCountAnalyticsByCaseFiledDateResponse as CaseCountAnalyticsByCaseFiledDateResponseSchema
from unicourt_python_sdk.model.exception import Exception as ExceptionSchema

from unicourt_python_sdk.type.case_count_analytics_by_case_filed_date_response import CaseCountAnalyticsByCaseFiledDateResponse
from unicourt_python_sdk.type.exception import Exception

from ...api_client import Dictionary
from unicourt_python_sdk.pydantic.exception import Exception as ExceptionPydantic
from unicourt_python_sdk.pydantic.case_count_analytics_by_case_filed_date_response import CaseCountAnalyticsByCaseFiledDateResponse as CaseCountAnalyticsByCaseFiledDateResponsePydantic

from . import path

# Query params


class QSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 2048


class PageNumberSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_minimum = 1


class GroupBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "Yearly": "YEARLY",
            "Quarterly": "QUARTERLY",
            "Monthly": "MONTHLY",
            "Weekly": "WEEKLY",
        }
    
    @schemas.classproperty
    def YEARLY(cls):
        return cls("Yearly")
    
    @schemas.classproperty
    def QUARTERLY(cls):
        return cls("Quarterly")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("Monthly")
    
    @schemas.classproperty
    def WEEKLY(cls):
        return cls("Weekly")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'pageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'groupBy': typing.Union[GroupBySchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'q': typing.Union[QSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_page_number = api_client.QueryParameter(
    name="pageNumber",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    required=True,
    explode=True,
)
request_query_group_by = api_client.QueryParameter(
    name="groupBy",
    style=api_client.ParameterStyle.FORM,
    schema=GroupBySchema,
    required=True,
    explode=True,
)
_auth = [
    'bearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = CaseCountAnalyticsByCaseFiledDateResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CaseCountAnalyticsByCaseFiledDateResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CaseCountAnalyticsByCaseFiledDateResponse


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
SchemaFor404ResponseBodyApplicationJson = ExceptionSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Exception


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Exception


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_case_count_analytics_by_case_filed_date_mapped_args(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if q is not None:
            _query_params["q"] = q
        if page_number is not None:
            _query_params["pageNumber"] = page_number
        if group_by is not None:
            _query_params["groupBy"] = group_by
        args.query = _query_params
        return args

    async def _aget_case_count_analytics_by_case_filed_date_oapg(
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
        Case Count Analytics by Case Filed Date.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_page_number,
            request_query_group_by,
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
            path_template='/caseCountAnalyticsByCaseFiledDate',
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


    def _get_case_count_analytics_by_case_filed_date_oapg(
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
        Case Count Analytics by Case Filed Date.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_page_number,
            request_query_group_by,
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
            path_template='/caseCountAnalyticsByCaseFiledDate',
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


class GetCaseCountAnalyticsByCaseFiledDateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_case_count_analytics_by_case_filed_date(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_case_count_analytics_by_case_filed_date_mapped_args(
            page_number=page_number,
            group_by=group_by,
            q=q,
        )
        return await self._aget_case_count_analytics_by_case_filed_date_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_case_count_analytics_by_case_filed_date(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_case_count_analytics_by_case_filed_date_mapped_args(
            page_number=page_number,
            group_by=group_by,
            q=q,
        )
        return self._get_case_count_analytics_by_case_filed_date_oapg(
            query_params=args.query,
        )

class GetCaseCountAnalyticsByCaseFiledDate(BaseApi):

    async def aget_case_count_analytics_by_case_filed_date(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CaseCountAnalyticsByCaseFiledDateResponsePydantic:
        raw_response = await self.raw.aget_case_count_analytics_by_case_filed_date(
            page_number=page_number,
            group_by=group_by,
            q=q,
            **kwargs,
        )
        if validate:
            return CaseCountAnalyticsByCaseFiledDateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CaseCountAnalyticsByCaseFiledDateResponsePydantic, raw_response.body)
    
    
    def get_case_count_analytics_by_case_filed_date(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CaseCountAnalyticsByCaseFiledDateResponsePydantic:
        raw_response = self.raw.get_case_count_analytics_by_case_filed_date(
            page_number=page_number,
            group_by=group_by,
            q=q,
        )
        if validate:
            return CaseCountAnalyticsByCaseFiledDateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CaseCountAnalyticsByCaseFiledDateResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_case_count_analytics_by_case_filed_date_mapped_args(
            page_number=page_number,
            group_by=group_by,
            q=q,
        )
        return await self._aget_case_count_analytics_by_case_filed_date_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        page_number: int,
        group_by: str,
        q: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_case_count_analytics_by_case_filed_date_mapped_args(
            page_number=page_number,
            group_by=group_by,
            q=q,
        )
        return self._get_case_count_analytics_by_case_filed_date_oapg(
            query_params=args.query,
        )
