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
from unicourt_python_sdk.model.attorneys import Attorneys as AttorneysSchema

from unicourt_python_sdk.type.exception import Exception
from unicourt_python_sdk.type.attorneys import Attorneys

from ...api_client import Dictionary
from unicourt_python_sdk.pydantic.attorneys import Attorneys as AttorneysPydantic
from unicourt_python_sdk.pydantic.exception import Exception as ExceptionPydantic

from . import path

# Query params
IsVisibleSchema = schemas.BoolSchema
PageNumberSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'isVisible': typing.Union[IsVisibleSchema, bool, ],
        'pageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_is_visible = api_client.QueryParameter(
    name="isVisible",
    style=api_client.ParameterStyle.FORM,
    schema=IsVisibleSchema,
    explode=True,
)
request_query_page_number = api_client.QueryParameter(
    name="pageNumber",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    explode=True,
)
# Path params


class CaseIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 18
        min_length = 18
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'caseId': typing.Union[CaseIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_case_id = api_client.PathParameter(
    name="caseId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CaseIdSchema,
    required=True,
)
_auth = [
    'bearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = AttorneysSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Attorneys


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Attorneys


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
SchemaFor451ResponseBodyApplicationJson = ExceptionSchema


@dataclass
class ApiResponseFor451(api_client.ApiResponse):
    body: Exception


@dataclass
class ApiResponseFor451Async(api_client.AsyncApiResponse):
    body: Exception


_response_for_451 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor451,
    response_cls_async=ApiResponseFor451Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor451ResponseBodyApplicationJson),
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
    '451': _response_for_451,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_attorneys_by_case_id_mapped_args(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if is_visible is not None:
            _query_params["isVisible"] = is_visible
        if page_number is not None:
            _query_params["pageNumber"] = page_number
        if case_id is not None:
            _path_params["caseId"] = case_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_attorneys_by_case_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Gets Attorneys for a requested Case ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_case_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_is_visible,
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
            path_template='/case/{caseId}/attorneys',
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


    def _get_attorneys_by_case_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Gets Attorneys for a requested Case ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_case_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_is_visible,
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
            path_template='/case/{caseId}/attorneys',
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


class GetAttorneysByCaseIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_attorneys_by_case_id(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_attorneys_by_case_id_mapped_args(
            case_id=case_id,
            is_visible=is_visible,
            page_number=page_number,
        )
        return await self._aget_attorneys_by_case_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_attorneys_by_case_id(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_attorneys_by_case_id_mapped_args(
            case_id=case_id,
            is_visible=is_visible,
            page_number=page_number,
        )
        return self._get_attorneys_by_case_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAttorneysByCaseId(BaseApi):

    async def aget_attorneys_by_case_id(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> AttorneysPydantic:
        raw_response = await self.raw.aget_attorneys_by_case_id(
            case_id=case_id,
            is_visible=is_visible,
            page_number=page_number,
            **kwargs,
        )
        if validate:
            return AttorneysPydantic(**raw_response.body)
        return api_client.construct_model_instance(AttorneysPydantic, raw_response.body)
    
    
    def get_attorneys_by_case_id(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        validate: bool = False,
    ) -> AttorneysPydantic:
        raw_response = self.raw.get_attorneys_by_case_id(
            case_id=case_id,
            is_visible=is_visible,
            page_number=page_number,
        )
        if validate:
            return AttorneysPydantic(**raw_response.body)
        return api_client.construct_model_instance(AttorneysPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_attorneys_by_case_id_mapped_args(
            case_id=case_id,
            is_visible=is_visible,
            page_number=page_number,
        )
        return await self._aget_attorneys_by_case_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        case_id: str,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_attorneys_by_case_id_mapped_args(
            case_id=case_id,
            is_visible=is_visible,
            page_number=page_number,
        )
        return self._get_attorneys_by_case_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

