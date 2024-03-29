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


class BarSourceDataAdministrativeActionsArray(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BarSourceDataAdministrativeActionsArrayItem']:
            return BarSourceDataAdministrativeActionsArrayItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['BarSourceDataAdministrativeActionsArrayItem'], typing.List['BarSourceDataAdministrativeActionsArrayItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BarSourceDataAdministrativeActionsArray':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BarSourceDataAdministrativeActionsArrayItem':
        return super().__getitem__(i)

from unicourt_python_sdk.model.bar_source_data_administrative_actions_array_item import BarSourceDataAdministrativeActionsArrayItem
