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


class CourtServiceStatusCaseClassIdArray(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    All the Case class ids associated to the service status
    """


    class MetaOapg:
        
        
        class items(
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
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                )


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CourtServiceStatusCaseClassIdArray':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )