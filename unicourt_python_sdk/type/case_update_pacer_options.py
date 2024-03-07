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

from unicourt_python_sdk.type.case_update_pacer_options_additional_page_array import CaseUpdatePacerOptionsAdditionalPageArray

class RequiredCaseUpdatePacerOptions(TypedDict):
    # **Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.**
    pacerUserId: str

class OptionalCaseUpdatePacerOptions(TypedDict, total=False):
    additionalPageArray: CaseUpdatePacerOptionsAdditionalPageArray

    # **Currently this option is only applicable for Federal PACER cases. You can limit how often parties and attorneys for a PACER case are fetched to reduce your PACER fees. If you are tracking cases daily or hourly you could easily end up with a large PACER bill.**  **Use Case: Cases are typically updated to check for new docket entry filings. However every update to PACER case costs money. Participants for a case change less often than docket entry filings. So fetching participants for every update might result in unnecessary PACER costs; especially on cases which have a lot of parties and attorneys. So instead of getting charged the minimum cost of $0.10 for an update which might have had few docket entries, you could end up spending $3 for every update because there were a lot of parties for that case that were also fetched.**  **With this option you can choose when to fetch parties for case based on when was it last fetched.** You can limit how often this participants are fetched in a PACER case to keep your PACER costs under control.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that participants are fetched from PACER for this case update irrespective of when the participants were last fetched. 2.  Specifying a value of 30 ensures that participants are fetched from PACER for this case update only if the last fetch was older than 30 days. 
    fetchParticipantsIfOlderThanDays: int

    # PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.
    pacerClientCode: typing.Optional[str]

    # This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.  Only one of the two values is allowed: -   fetchNewDocketEntries:     >   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested. -   fetchAllDocketEntries:     >   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available. 
    refreshType: typing.Optional[str]

class CaseUpdatePacerOptions(RequiredCaseUpdatePacerOptions, OptionalCaseUpdatePacerOptions):
    pass
