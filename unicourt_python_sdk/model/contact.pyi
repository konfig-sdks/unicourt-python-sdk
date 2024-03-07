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


class Contact(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contact object data schema.
    """


    class MetaOapg:
        required = {
            "addressArray",
            "phoneNumberArray",
            "emailArray",
            "object",
        }
        
        class properties:
            
            
            class addressArray(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Address']:
                        return Address
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressArray':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class emailArray(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Email']:
                        return Email
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emailArray':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class phoneNumberArray(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Phone']:
                        return Phone
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phoneNumberArray':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "addressArray": addressArray,
                "emailArray": emailArray,
                "object": object,
                "phoneNumberArray": phoneNumberArray,
            }
    
    addressArray: MetaOapg.properties.addressArray
    phoneNumberArray: MetaOapg.properties.phoneNumberArray
    emailArray: MetaOapg.properties.emailArray
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressArray"]) -> MetaOapg.properties.addressArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailArray"]) -> MetaOapg.properties.emailArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumberArray"]) -> MetaOapg.properties.phoneNumberArray: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressArray", "emailArray", "object", "phoneNumberArray", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressArray"]) -> MetaOapg.properties.addressArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailArray"]) -> MetaOapg.properties.emailArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumberArray"]) -> MetaOapg.properties.phoneNumberArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressArray", "emailArray", "object", "phoneNumberArray", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addressArray: typing.Union[MetaOapg.properties.addressArray, list, tuple, None, ],
        phoneNumberArray: typing.Union[MetaOapg.properties.phoneNumberArray, list, tuple, None, ],
        emailArray: typing.Union[MetaOapg.properties.emailArray, list, tuple, None, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contact':
        return super().__new__(
            cls,
            *args,
            addressArray=addressArray,
            phoneNumberArray=phoneNumberArray,
            emailArray=emailArray,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.address import Address
from unicourt_python_sdk.model.email import Email
from unicourt_python_sdk.model.phone import Phone
