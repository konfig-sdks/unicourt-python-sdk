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


class NormJudgePublicDataNameHistoryArray(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Name changes of the Judge. Change in the official name. Other names go to Alias array.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['NormJudgePublicDataNameHistoryArrayItem']:
            return NormJudgePublicDataNameHistoryArrayItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['NormJudgePublicDataNameHistoryArrayItem'], typing.List['NormJudgePublicDataNameHistoryArrayItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'NormJudgePublicDataNameHistoryArray':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'NormJudgePublicDataNameHistoryArrayItem':
        return super().__getitem__(i)

from unicourt_python_sdk.model.norm_judge_public_data_name_history_array_item import NormJudgePublicDataNameHistoryArrayItem