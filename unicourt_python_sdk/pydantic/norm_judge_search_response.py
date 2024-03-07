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
from pydantic import BaseModel, Field, RootModel

from unicourt_python_sdk.pydantic.norm_judge_search_result import NormJudgeSearchResult

class NormJudgeSearchResponse(BaseModel):
    # Link to next page.
    next_page_a_p_i: typing.Optional[str] = Field(alias='nextPageAPI')

    # Query been sent by client
    norm_judge_search_id: str = Field(alias='normJudgeSearchId')

    norm_judge_search_result_array: typing.List[NormJudgeSearchResult] = Field(alias='normJudgeSearchResultArray')

    object: str = Field(alias='object')

    page_number: int = Field(alias='pageNumber')

    # Link to previous page.
    previous_page_a_p_i: typing.Optional[str] = Field(alias='previousPageAPI')

    # Query been sent by client
    q: str = Field(alias='q')

    # The number of matches that were found in the index.
    total_count: int = Field(alias='totalCount')

    # Total pages for matches that were found in the index.
    total_pages: int = Field(alias='totalPages')
    class Config:
        arbitrary_types_allowed = True
