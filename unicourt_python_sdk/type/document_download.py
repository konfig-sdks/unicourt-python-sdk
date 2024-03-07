# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredDocumentDownload(TypedDict):
    # API call to download the document again if the above fileUrl is expired.
    caseDocumentDownloadAPI: str

    # Requested Document ID.
    caseDocumentId: str

    # Expiry date-time for the fileUrl provided in this object.
    expiryDate: str

    # Link to download the file.
    fileUrl: str

    # Name of the object.
    object: str

class OptionalDocumentDownload(TypedDict, total=False):
    pass

class DocumentDownload(RequiredDocumentDownload, OptionalDocumentDownload):
    pass