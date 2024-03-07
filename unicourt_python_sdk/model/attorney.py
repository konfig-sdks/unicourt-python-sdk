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


class Attorney(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sourceAttorneyType",
            "attorneyId",
            "lastName",
            "nameSuffix",
            "possibleNormLawFirmArray",
            "attorneyLawFirmArray",
            "isVisible",
            "partyRoleGroupIdArray",
            "partyRoleIdArray",
            "firstName",
            "lastFetchDate",
            "possibleNormAttorneyArray",
            "barNumber",
            "namePrefix",
            "contact",
            "name",
            "attorneyType",
            "middleName",
            "firstFetchDate",
            "partyAttorneyAssociations",
            "object",
        }
        
        class properties:
            
            
            class attorneyId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class attorneyLawFirmArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 25
                    
                    @staticmethod
                    def items() -> typing.Type['AttorneyLawFirm']:
                        return AttorneyLawFirm
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AttorneyLawFirm'], typing.List['AttorneyLawFirm']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attorneyLawFirmArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AttorneyLawFirm':
                    return super().__getitem__(i)
        
            @staticmethod
            def attorneyType() -> typing.Type['AttorneyType']:
                return AttorneyType
            
            
            class barNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 250
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'barNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def contact() -> typing.Type['Contact']:
                return Contact
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
            class firstName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 250
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'firstName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            isVisible = schemas.BoolSchema
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
            class lastName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class middleName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'middleName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
                    min_length = 1
            
            
            class namePrefix(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 10
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'namePrefix':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class nameSuffix(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 10
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nameSuffix':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 8
                    min_length = 8
        
            @staticmethod
            def partyAttorneyAssociations() -> typing.Type['PartyAttorneyAssociations']:
                return PartyAttorneyAssociations
        
            @staticmethod
            def partyRoleGroupIdArray() -> typing.Type['AttorneyPartyRoleGroupIdArray']:
                return AttorneyPartyRoleGroupIdArray
        
            @staticmethod
            def partyRoleIdArray() -> typing.Type['AttorneyPartyRoleIdArray']:
                return AttorneyPartyRoleIdArray
            
            
            class possibleNormAttorneyArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PossibleNormAttorney']:
                        return PossibleNormAttorney
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PossibleNormAttorney'], typing.List['PossibleNormAttorney']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'possibleNormAttorneyArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PossibleNormAttorney':
                    return super().__getitem__(i)
            
            
            class possibleNormLawFirmArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PossibleNormLawFirm']:
                        return PossibleNormLawFirm
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PossibleNormLawFirm'], typing.List['PossibleNormLawFirm']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'possibleNormLawFirmArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PossibleNormLawFirm':
                    return super().__getitem__(i)
            
            
            class sourceAttorneyType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
            __annotations__ = {
                "attorneyId": attorneyId,
                "attorneyLawFirmArray": attorneyLawFirmArray,
                "attorneyType": attorneyType,
                "barNumber": barNumber,
                "contact": contact,
                "firstFetchDate": firstFetchDate,
                "firstName": firstName,
                "isVisible": isVisible,
                "lastFetchDate": lastFetchDate,
                "lastName": lastName,
                "middleName": middleName,
                "name": name,
                "namePrefix": namePrefix,
                "nameSuffix": nameSuffix,
                "object": object,
                "partyAttorneyAssociations": partyAttorneyAssociations,
                "partyRoleGroupIdArray": partyRoleGroupIdArray,
                "partyRoleIdArray": partyRoleIdArray,
                "possibleNormAttorneyArray": possibleNormAttorneyArray,
                "possibleNormLawFirmArray": possibleNormLawFirmArray,
                "sourceAttorneyType": sourceAttorneyType,
            }

    
    sourceAttorneyType: MetaOapg.properties.sourceAttorneyType
    attorneyId: MetaOapg.properties.attorneyId
    lastName: MetaOapg.properties.lastName
    nameSuffix: MetaOapg.properties.nameSuffix
    possibleNormLawFirmArray: MetaOapg.properties.possibleNormLawFirmArray
    attorneyLawFirmArray: MetaOapg.properties.attorneyLawFirmArray
    isVisible: MetaOapg.properties.isVisible
    partyRoleGroupIdArray: 'AttorneyPartyRoleGroupIdArray'
    partyRoleIdArray: 'AttorneyPartyRoleIdArray'
    firstName: MetaOapg.properties.firstName
    lastFetchDate: MetaOapg.properties.lastFetchDate
    possibleNormAttorneyArray: MetaOapg.properties.possibleNormAttorneyArray
    barNumber: MetaOapg.properties.barNumber
    namePrefix: MetaOapg.properties.namePrefix
    contact: 'Contact'
    name: MetaOapg.properties.name
    attorneyType: 'AttorneyType'
    middleName: MetaOapg.properties.middleName
    firstFetchDate: MetaOapg.properties.firstFetchDate
    partyAttorneyAssociations: 'PartyAttorneyAssociations'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attorneyId"]) -> MetaOapg.properties.attorneyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attorneyLawFirmArray"]) -> MetaOapg.properties.attorneyLawFirmArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attorneyType"]) -> 'AttorneyType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["barNumber"]) -> MetaOapg.properties.barNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact"]) -> 'Contact': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["namePrefix"]) -> MetaOapg.properties.namePrefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameSuffix"]) -> MetaOapg.properties.nameSuffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partyAttorneyAssociations"]) -> 'PartyAttorneyAssociations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partyRoleGroupIdArray"]) -> 'AttorneyPartyRoleGroupIdArray': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partyRoleIdArray"]) -> 'AttorneyPartyRoleIdArray': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possibleNormAttorneyArray"]) -> MetaOapg.properties.possibleNormAttorneyArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possibleNormLawFirmArray"]) -> MetaOapg.properties.possibleNormLawFirmArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceAttorneyType"]) -> MetaOapg.properties.sourceAttorneyType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attorneyId", "attorneyLawFirmArray", "attorneyType", "barNumber", "contact", "firstFetchDate", "firstName", "isVisible", "lastFetchDate", "lastName", "middleName", "name", "namePrefix", "nameSuffix", "object", "partyAttorneyAssociations", "partyRoleGroupIdArray", "partyRoleIdArray", "possibleNormAttorneyArray", "possibleNormLawFirmArray", "sourceAttorneyType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attorneyId"]) -> MetaOapg.properties.attorneyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attorneyLawFirmArray"]) -> MetaOapg.properties.attorneyLawFirmArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attorneyType"]) -> 'AttorneyType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["barNumber"]) -> MetaOapg.properties.barNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> 'Contact': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["namePrefix"]) -> MetaOapg.properties.namePrefix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameSuffix"]) -> MetaOapg.properties.nameSuffix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partyAttorneyAssociations"]) -> 'PartyAttorneyAssociations': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partyRoleGroupIdArray"]) -> 'AttorneyPartyRoleGroupIdArray': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partyRoleIdArray"]) -> 'AttorneyPartyRoleIdArray': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possibleNormAttorneyArray"]) -> MetaOapg.properties.possibleNormAttorneyArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possibleNormLawFirmArray"]) -> MetaOapg.properties.possibleNormLawFirmArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceAttorneyType"]) -> MetaOapg.properties.sourceAttorneyType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attorneyId", "attorneyLawFirmArray", "attorneyType", "barNumber", "contact", "firstFetchDate", "firstName", "isVisible", "lastFetchDate", "lastName", "middleName", "name", "namePrefix", "nameSuffix", "object", "partyAttorneyAssociations", "partyRoleGroupIdArray", "partyRoleIdArray", "possibleNormAttorneyArray", "possibleNormLawFirmArray", "sourceAttorneyType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Attorney':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.attorney_law_firm import AttorneyLawFirm
from unicourt_python_sdk.model.attorney_party_role_group_id_array import AttorneyPartyRoleGroupIdArray
from unicourt_python_sdk.model.attorney_party_role_id_array import AttorneyPartyRoleIdArray
from unicourt_python_sdk.model.attorney_type import AttorneyType
from unicourt_python_sdk.model.contact import Contact
from unicourt_python_sdk.model.party_attorney_associations import PartyAttorneyAssociations
from unicourt_python_sdk.model.possible_norm_attorney import PossibleNormAttorney
from unicourt_python_sdk.model.possible_norm_law_firm import PossibleNormLawFirm