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

from unicourt_python_sdk.model.pacer_import_case import PACERImportCase as PACERImportCaseSchema
from unicourt_python_sdk.model.exception import Exception as ExceptionSchema

from unicourt_python_sdk.type.pacer_import_case import PACERImportCase
from unicourt_python_sdk.type.exception import Exception

from ...api_client import Dictionary
from unicourt_python_sdk.pydantic.exception import Exception as ExceptionPydantic
from unicourt_python_sdk.pydantic.pacer_import_case import PACERImportCase as PACERImportCasePydantic

from . import path

# Query params


class PacerUserIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 20
        min_length = 6


class PacerClientCodeSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 32
        min_length = 1


class CaseNumberSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 50
        min_length = 3


class CourtIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 18
        min_length = 18
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'pacerUserId': typing.Union[PacerUserIdSchema, str, ],
        'pacerClientCode': typing.Union[PacerClientCodeSchema, str, ],
        'caseNumber': typing.Union[CaseNumberSchema, str, ],
        'courtId': typing.Union[CourtIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_pacer_user_id = api_client.QueryParameter(
    name="pacerUserId",
    style=api_client.ParameterStyle.FORM,
    schema=PacerUserIdSchema,
    required=True,
    explode=True,
)
request_query_pacer_client_code = api_client.QueryParameter(
    name="pacerClientCode",
    style=api_client.ParameterStyle.FORM,
    schema=PacerClientCodeSchema,
    required=True,
    explode=True,
)
request_query_case_number = api_client.QueryParameter(
    name="caseNumber",
    style=api_client.ParameterStyle.FORM,
    schema=CaseNumberSchema,
    required=True,
    explode=True,
)
request_query_court_id = api_client.QueryParameter(
    name="courtId",
    style=api_client.ParameterStyle.FORM,
    schema=CourtIdSchema,
    required=True,
    explode=True,
)
_auth = [
    'bearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = PACERImportCaseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PACERImportCase


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PACERImportCase


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _import_pacer_case_by_court_using_case_number_get_mapped_args(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if pacer_user_id is not None:
            _query_params["pacerUserId"] = pacer_user_id
        if pacer_client_code is not None:
            _query_params["pacerClientCode"] = pacer_client_code
        if case_number is not None:
            _query_params["caseNumber"] = case_number
        if court_id is not None:
            _query_params["courtId"] = court_id
        args.query = _query_params
        return args

    async def _aimport_pacer_case_by_court_using_case_number_get_oapg(
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
        Find PACER Case for a requested Case Number and Court.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pacer_user_id,
            request_query_pacer_client_code,
            request_query_case_number,
            request_query_court_id,
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
            path_template='/pacer/importCaseByCourtUsingCaseNumber',
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


    def _import_pacer_case_by_court_using_case_number_get_oapg(
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
        Find PACER Case for a requested Case Number and Court.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pacer_user_id,
            request_query_pacer_client_code,
            request_query_case_number,
            request_query_court_id,
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
            path_template='/pacer/importCaseByCourtUsingCaseNumber',
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


class ImportPacerCaseByCourtUsingCaseNumberGetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aimport_pacer_case_by_court_using_case_number_get(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._import_pacer_case_by_court_using_case_number_get_mapped_args(
            pacer_user_id=pacer_user_id,
            pacer_client_code=pacer_client_code,
            case_number=case_number,
            court_id=court_id,
        )
        return await self._aimport_pacer_case_by_court_using_case_number_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def import_pacer_case_by_court_using_case_number_get(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._import_pacer_case_by_court_using_case_number_get_mapped_args(
            pacer_user_id=pacer_user_id,
            pacer_client_code=pacer_client_code,
            case_number=case_number,
            court_id=court_id,
        )
        return self._import_pacer_case_by_court_using_case_number_get_oapg(
            query_params=args.query,
        )

class ImportPacerCaseByCourtUsingCaseNumberGet(BaseApi):

    async def aimport_pacer_case_by_court_using_case_number_get(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
        validate: bool = False,
        **kwargs,
    ) -> PACERImportCasePydantic:
        raw_response = await self.raw.aimport_pacer_case_by_court_using_case_number_get(
            pacer_user_id=pacer_user_id,
            pacer_client_code=pacer_client_code,
            case_number=case_number,
            court_id=court_id,
            **kwargs,
        )
        if validate:
            return PACERImportCasePydantic(**raw_response.body)
        return api_client.construct_model_instance(PACERImportCasePydantic, raw_response.body)
    
    
    def import_pacer_case_by_court_using_case_number_get(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
        validate: bool = False,
    ) -> PACERImportCasePydantic:
        raw_response = self.raw.import_pacer_case_by_court_using_case_number_get(
            pacer_user_id=pacer_user_id,
            pacer_client_code=pacer_client_code,
            case_number=case_number,
            court_id=court_id,
        )
        if validate:
            return PACERImportCasePydantic(**raw_response.body)
        return api_client.construct_model_instance(PACERImportCasePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._import_pacer_case_by_court_using_case_number_get_mapped_args(
            pacer_user_id=pacer_user_id,
            pacer_client_code=pacer_client_code,
            case_number=case_number,
            court_id=court_id,
        )
        return await self._aimport_pacer_case_by_court_using_case_number_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._import_pacer_case_by_court_using_case_number_get_mapped_args(
            pacer_user_id=pacer_user_id,
            pacer_client_code=pacer_client_code,
            case_number=case_number,
            court_id=court_id,
        )
        return self._import_pacer_case_by_court_using_case_number_get_oapg(
            query_params=args.query,
        )
