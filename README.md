<div align="left">

[![Visit Unicourt](./header.png)](https://unicourt.com)

# Unicourt<a id="unicourt"></a>

<button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`unicourt.attorney_analytics_api.get_associated_law_firms`](#unicourtattorney_analytics_apiget_associated_law_firms)
- [Terms and Connectors](#terms-and-connectors)
- [Example Query](#example-query)
  * [`unicourt.attorney_analytics_api.get_judges_associated_with_attorney`](#unicourtattorney_analytics_apiget_judges_associated_with_attorney)
- [Terms and Connectors](#terms-and-connectors-1)
- [Example Query](#example-query-1)
  * [`unicourt.attorney_analytics_api.get_norm_attorney_by_id`](#unicourtattorney_analytics_apiget_norm_attorney_by_id)
  * [`unicourt.attorney_analytics_api.get_norm_attorney_search_results`](#unicourtattorney_analytics_apiget_norm_attorney_search_results)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormAttorneySearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normattorneysearchqueryobject)
  * [`unicourt.attorney_analytics_api.list_associated_norm_parties`](#unicourtattorney_analytics_apilist_associated_norm_parties)
- [Terms and Connectors](#terms-and-connectors-2)
- [Example Query](#example-query-2)
  * [`unicourt.attorney_analytics_api.search_attorney_info`](#unicourtattorney_analytics_apisearch_attorney_info)
  * [This endpoint retrieves information, including the normAttorneyId, on all attorneys in our normalized attorney database which match the request parameters. All query parameters supported by this API can be found in the schema section below.](#this-endpoint-retrieves-information-including-the-normattorneyid-on-all-attorneys-in-our-normalized-attorney-database-which-match-the-request-parameters-all-query-parameters-supported-by-this-api-can-be-found-in-the-schema-section-below)
  * [`unicourt.authentication_api.generate_new_token`](#unicourtauthentication_apigenerate_new_token)
  * [`unicourt.authentication_api.get_all_token_ids`](#unicourtauthentication_apiget_all_token_ids)
  * [`unicourt.authentication_api.invalidate_access_token`](#unicourtauthentication_apiinvalidate_access_token)
  * [`unicourt.authentication_api.invalidate_all_tokens`](#unicourtauthentication_apiinvalidate_all_tokens)
  * [`unicourt.callback_api.list_callbacks_with_count`](#unicourtcallback_apilist_callbacks_with_count)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_case_class`](#unicourtcase_analytics_apiget_case_count_analytics_by_case_class)
- [Terms and Connectors](#terms-and-connectors-3)
- [Example Query](#example-query-3)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_case_filed_date`](#unicourtcase_analytics_apiget_case_count_analytics_by_case_filed_date)
- [Terms and Connectors](#terms-and-connectors-4)
- [Example Query](#example-query-4)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_case_type_group`](#unicourtcase_analytics_apiget_case_count_analytics_by_case_type_group)
- [Terms and Connectors](#terms-and-connectors-5)
- [Example Query](#example-query-5)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_court`](#unicourtcase_analytics_apiget_case_count_analytics_by_court)
- [Terms and Connectors](#terms-and-connectors-6)
- [Example Query](#example-query-6)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_court_location`](#unicourtcase_analytics_apiget_case_count_analytics_by_court_location)
- [Terms and Connectors](#terms-and-connectors-7)
- [Example Query](#example-query-7)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_court_system`](#unicourtcase_analytics_apiget_case_count_analytics_by_court_system)
- [Terms and Connectors](#terms-and-connectors-8)
- [Example Query](#example-query-8)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_court_type`](#unicourtcase_analytics_apiget_case_count_analytics_by_court_type)
- [Terms and Connectors](#terms-and-connectors-9)
- [Example Query](#example-query-9)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_jurisdiction_geo`](#unicourtcase_analytics_apiget_case_count_analytics_by_jurisdiction_geo)
- [Terms and Connectors](#terms-and-connectors-10)
- [Example Query](#example-query-10)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_norm_attorney`](#unicourtcase_analytics_apiget_case_count_analytics_by_norm_attorney)
- [Terms and Connectors](#terms-and-connectors-11)
- [Example Query](#example-query-11)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_norm_judge`](#unicourtcase_analytics_apiget_case_count_analytics_by_norm_judge)
- [Terms and Connectors](#terms-and-connectors-12)
- [Example Query](#example-query-12)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_norm_law_firm`](#unicourtcase_analytics_apiget_case_count_analytics_by_norm_law_firm)
- [Terms and Connectors](#terms-and-connectors-13)
- [Example Query](#example-query-13)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_norm_party`](#unicourtcase_analytics_apiget_case_count_analytics_by_norm_party)
- [Terms and Connectors](#terms-and-connectors-14)
- [Example Query](#example-query-14)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_attorney_for_norm_attorney`](#unicourtcase_analytics_apiget_case_count_analytics_by_opposing_norm_attorney_for_norm_attorney)
- [Terms and Connectors](#terms-and-connectors-15)
- [Example Query](#example-query-15)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm`](#unicourtcase_analytics_apiget_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm)
- [Terms and Connectors](#terms-and-connectors-16)
- [Example Query](#example-query-16)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_party_for_a_norm_party`](#unicourtcase_analytics_apiget_case_count_analytics_by_opposing_norm_party_for_a_norm_party)
- [Terms and Connectors](#terms-and-connectors-17)
- [Example Query](#example-query-17)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_party_role`](#unicourtcase_analytics_apiget_case_count_analytics_by_party_role)
- [Terms and Connectors](#terms-and-connectors-18)
- [Example Query](#example-query-18)
  * [`unicourt.case_analytics_api.get_case_count_analytics_by_party_role_group`](#unicourtcase_analytics_apiget_case_count_analytics_by_party_role_group)
- [Terms and Connectors](#terms-and-connectors-19)
- [Example Query](#example-query-19)
  * [`unicourt.case_analytics_api.get_case_count_by_area_of_law`](#unicourtcase_analytics_apiget_case_count_by_area_of_law)
- [Terms and Connectors](#terms-and-connectors-20)
- [Example Query](#example-query-20)
  * [`unicourt.case_analytics_api.get_case_count_by_case_type`](#unicourtcase_analytics_apiget_case_count_by_case_type)
- [Terms and Connectors](#terms-and-connectors-21)
- [Example Query](#example-query-21)
  * [`unicourt.case_docket_api.get_associated_attorney_details`](#unicourtcase_docket_apiget_associated_attorney_details)
  * [`unicourt.case_docket_api.get_associated_parties`](#unicourtcase_docket_apiget_associated_parties)
  * [`unicourt.case_docket_api.get_attorney_details`](#unicourtcase_docket_apiget_attorney_details)
  * [`unicourt.case_docket_api.get_attorneys_by_case_id`](#unicourtcase_docket_apiget_attorneys_by_case_id)
  * [`unicourt.case_docket_api.get_case_info`](#unicourtcase_docket_apiget_case_info)
  * [`unicourt.case_docket_api.get_case_parties`](#unicourtcase_docket_apiget_case_parties)
  * [`unicourt.case_docket_api.get_docket_entries`](#unicourtcase_docket_apiget_docket_entries)
  * [`unicourt.case_docket_api.get_hearings_for_case`](#unicourtcase_docket_apiget_hearings_for_case)
  * [`unicourt.case_docket_api.get_judge_details`](#unicourtcase_docket_apiget_judge_details)
  * [`unicourt.case_docket_api.get_judges_for_case`](#unicourtcase_docket_apiget_judges_for_case)
  * [`unicourt.case_docket_api.get_party_details`](#unicourtcase_docket_apiget_party_details)
  * [`unicourt.case_docket_api.get_primary_documents`](#unicourtcase_docket_apiget_primary_documents)
  * [`unicourt.case_docket_api.get_related_cases`](#unicourtcase_docket_apiget_related_cases)
  * [`unicourt.case_docket_api.get_secondary_documents_for_docket_entries`](#unicourtcase_docket_apiget_secondary_documents_for_docket_entries)
  * [`unicourt.case_documents_api.add_document_order`](#unicourtcase_documents_apiadd_document_order)
  * [`unicourt.case_documents_api.get_callback_by_id`](#unicourtcase_documents_apiget_callback_by_id)
  * [`unicourt.case_documents_api.get_document_details_by_document_id`](#unicourtcase_documents_apiget_document_details_by_document_id)
  * [`unicourt.case_documents_api.get_documents_for_case`](#unicourtcase_documents_apiget_documents_for_case)
  * [`unicourt.case_documents_api.get_downloadable_url_for_document`](#unicourtcase_documents_apiget_downloadable_url_for_document)
  * [`unicourt.case_documents_api.list_document_order_callbacks`](#unicourtcase_documents_apilist_document_order_callbacks)
  * [`unicourt.case_export_api.get_callback_by_id`](#unicourtcase_export_apiget_callback_by_id)
  * [`unicourt.case_export_api.get_callback_list_for_requested_date`](#unicourtcase_export_apiget_callback_list_for_requested_date)
  * [`unicourt.case_export_api.get_case_export_by_case_id`](#unicourtcase_export_apiget_case_export_by_case_id)
  * [`unicourt.case_search_api.get_search_results_by_case_search_id`](#unicourtcase_search_apiget_search_results_by_case_search_id)
  * [`unicourt.case_search_api.search_by_keyword_expressions`](#unicourtcase_search_apisearch_by_keyword_expressions)
- [Allowed Connectors in Keyword Expressions](#allowed-connectors-in-keyword-expressions)
- [Fields and Connectors Searching](#fields-and-connectors-searching)
- [](#)
- [Party Sub Filter Examples](#party-sub-filter-examples)
  * [All query parameters supported for this API can be found in below schema section. Schema --> CaseSearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema-----casesearchqueryobject)
  * [`unicourt.case_tracking_api.add_case_track`](#unicourtcase_tracking_apiadd_case_track)
  * [`unicourt.case_tracking_api.get_case_track`](#unicourtcase_tracking_apiget_case_track)
  * [`unicourt.case_tracking_api.get_case_track_list`](#unicourtcase_tracking_apiget_case_track_list)
  * [`unicourt.case_tracking_api.remove_case_track_by_id`](#unicourtcase_tracking_apiremove_case_track_by_id)
  * [`unicourt.case_update_api.add_case_update_for_case_id`](#unicourtcase_update_apiadd_case_update_for_case_id)
  * [`unicourt.case_update_api.get_case_updates`](#unicourtcase_update_apiget_case_updates)
  * [`unicourt.case_update_api.get_case_updates_by_case_id`](#unicourtcase_update_apiget_case_updates_by_case_id)
  * [`unicourt.court_availability_api.get_court_coverage_by_court_id`](#unicourtcourt_availability_apiget_court_coverage_by_court_id)
  * [`unicourt.court_standards_api.associated_court_for_jurisdiction_geo`](#unicourtcourt_standards_apiassociated_court_for_jurisdiction_geo)
  * [`unicourt.court_standards_api.get_additional_charge_info`](#unicourtcourt_standards_apiget_additional_charge_info)
- [Logical Operators](#logical-operators)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargeadditionaldataqueryobject)
  * [`unicourt.court_standards_api.get_appeal_courts_for_court`](#unicourtcourt_standards_apiget_appeal_courts_for_court)
  * [`unicourt.court_standards_api.get_area_of_law`](#unicourtcourt_standards_apiget_area_of_law)
  * [`unicourt.court_standards_api.get_attorney_rep_type`](#unicourtcourt_standards_apiget_attorney_rep_type)
- [Logical Operators](#logical-operators-1)
  * [All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----attorneyrepresentationtypequeryobject)
  * [`unicourt.court_standards_api.get_attorney_rep_type_0`](#unicourtcourt_standards_apiget_attorney_rep_type_0)
  * [`unicourt.court_standards_api.get_attorney_type_object`](#unicourtcourt_standards_apiget_attorney_type_object)
  * [`unicourt.court_standards_api.get_attorney_type_using_keyword_expression`](#unicourtcourt_standards_apiget_attorney_type_using_keyword_expression)
- [Logical Operators](#logical-operators-2)
  * [All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----attorneytypequeryobject)
  * [`unicourt.court_standards_api.get_case_class_by_id`](#unicourtcourt_standards_apiget_case_class_by_id)
  * [`unicourt.court_standards_api.get_case_class_by_keyword`](#unicourtcourt_standards_apiget_case_class_by_keyword)
- [Logical Operators](#logical-operators-3)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----caseclassqueryobject)
  * [`unicourt.court_standards_api.get_case_relationship_type_by_id`](#unicourtcourt_standards_apiget_case_relationship_type_by_id)
  * [`unicourt.court_standards_api.get_case_relationship_types`](#unicourtcourt_standards_apiget_case_relationship_types)
- [Logical Operators](#logical-operators-4)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----caserelationshiptypequeryobject)
  * [`unicourt.court_standards_api.get_case_status_by_id`](#unicourtcourt_standards_apiget_case_status_by_id)
  * [`unicourt.court_standards_api.get_case_status_by_keyword`](#unicourtcourt_standards_apiget_case_status_by_keyword)
- [Logical Operators](#logical-operators-5)
  * [All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casestatusqueryobject)
  * [`unicourt.court_standards_api.get_case_status_group`](#unicourtcourt_standards_apiget_case_status_group)
  * [`unicourt.court_standards_api.get_case_status_group_using_keyword_expression`](#unicourtcourt_standards_apiget_case_status_group_using_keyword_expression)
- [Logical Operators](#logical-operators-6)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casestatusgroupqueryobject)
  * [`unicourt.court_standards_api.get_case_type`](#unicourtcourt_standards_apiget_case_type)
  * [`unicourt.court_standards_api.get_case_type_group`](#unicourtcourt_standards_apiget_case_type_group)
  * [`unicourt.court_standards_api.get_case_types_by_keyword`](#unicourtcourt_standards_apiget_case_types_by_keyword)
- [Logical Operators](#logical-operators-7)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casetypequeryobject)
  * [`unicourt.court_standards_api.get_cause_of_action`](#unicourtcourt_standards_apiget_cause_of_action)
  * [`unicourt.court_standards_api.get_cause_of_action_additional_data`](#unicourtcourt_standards_apiget_cause_of_action_additional_data)
- [Logical Operators](#logical-operators-8)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----causeofactionadditionaldataqueryobject)
  * [`unicourt.court_standards_api.get_cause_of_action_additional_data_0`](#unicourtcourt_standards_apiget_cause_of_action_additional_data_0)
  * [`unicourt.court_standards_api.get_cause_of_action_by_keyword`](#unicourtcourt_standards_apiget_cause_of_action_by_keyword)
- [Logical Operators](#logical-operators-9)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----causeofactionqueryobject)
  * [`unicourt.court_standards_api.get_cause_of_action_group`](#unicourtcourt_standards_apiget_cause_of_action_group)
- [Logical Operators](#logical-operators-10)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----causeofactiongroupqueryobject)
  * [`unicourt.court_standards_api.get_cause_of_action_group_0`](#unicourtcourt_standards_apiget_cause_of_action_group_0)
  * [`unicourt.court_standards_api.get_charge_additional_data`](#unicourtcourt_standards_apiget_charge_additional_data)
  * [`unicourt.court_standards_api.get_charge_by_id`](#unicourtcourt_standards_apiget_charge_by_id)
  * [`unicourt.court_standards_api.get_charge_degree_by_id`](#unicourtcourt_standards_apiget_charge_degree_by_id)
  * [`unicourt.court_standards_api.get_charge_degree_using_keyword_expression`](#unicourtcourt_standards_apiget_charge_degree_using_keyword_expression)
- [Logical Operators](#logical-operators-11)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargedegreequeryobject)
  * [`unicourt.court_standards_api.get_charge_group`](#unicourtcourt_standards_apiget_charge_group)
  * [`unicourt.court_standards_api.get_charge_groups_by_keyword`](#unicourtcourt_standards_apiget_charge_groups_by_keyword)
- [Logical Operators](#logical-operators-12)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargegroupqueryobject)
  * [`unicourt.court_standards_api.get_charge_severity`](#unicourtcourt_standards_apiget_charge_severity)
  * [`unicourt.court_standards_api.get_charge_severity_by_keyword`](#unicourtcourt_standards_apiget_charge_severity_by_keyword)
- [Logical Operators](#logical-operators-13)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargeseverityqueryobject)
  * [`unicourt.court_standards_api.get_charges_using_keyword`](#unicourtcourt_standards_apiget_charges_using_keyword)
- [Logical Operators](#logical-operators-14)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargequeryobject)
  * [`unicourt.court_standards_api.get_court_location`](#unicourtcourt_standards_apiget_court_location)
- [Logical Operators](#logical-operators-15)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtlocationqueryobject)
  * [`unicourt.court_standards_api.get_court_location_object`](#unicourtcourt_standards_apiget_court_location_object)
  * [`unicourt.court_standards_api.get_court_locations`](#unicourtcourt_standards_apiget_court_locations)
  * [`unicourt.court_standards_api.get_court_object`](#unicourtcourt_standards_apiget_court_object)
  * [`unicourt.court_standards_api.get_court_service_status`](#unicourtcourt_standards_apiget_court_service_status)
- [Logical Operators](#logical-operators-16)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtservicestatusqueryobject)
  * [`unicourt.court_standards_api.get_court_service_status_by_id`](#unicourtcourt_standards_apiget_court_service_status_by_id)
  * [`unicourt.court_standards_api.get_court_system`](#unicourtcourt_standards_apiget_court_system)
  * [`unicourt.court_standards_api.get_court_type_object`](#unicourtcourt_standards_apiget_court_type_object)
  * [`unicourt.court_standards_api.get_court_types`](#unicourtcourt_standards_apiget_court_types)
- [Logical Operators](#logical-operators-17)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courttypequeryobject)
  * [`unicourt.court_standards_api.get_courts`](#unicourtcourt_standards_apiget_courts)
- [Logical Operators](#logical-operators-18)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtqueryobject)
  * [`unicourt.court_standards_api.get_courts_by_location`](#unicourtcourt_standards_apiget_courts_by_location)
  * [`unicourt.court_standards_api.get_judge_type_object`](#unicourtcourt_standards_apiget_judge_type_object)
- [Logical Operators](#logical-operators-19)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----judgetypequeryobject)
  * [`unicourt.court_standards_api.get_judge_type_object_by_id`](#unicourtcourt_standards_apiget_judge_type_object_by_id)
  * [`unicourt.court_standards_api.get_jurisdiction_geo`](#unicourtcourt_standards_apiget_jurisdiction_geo)
  * [`unicourt.court_standards_api.get_jurisdiction_geo_for_court`](#unicourtcourt_standards_apiget_jurisdiction_geo_for_court)
- [Logical Operators](#logical-operators-20)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----jurisdictiongeoqueryobject)
  * [`unicourt.court_standards_api.get_jurisdiction_geo_objects_for_court`](#unicourtcourt_standards_apiget_jurisdiction_geo_objects_for_court)
  * [`unicourt.court_standards_api.get_party_role`](#unicourtcourt_standards_apiget_party_role)
  * [`unicourt.court_standards_api.get_party_role_group`](#unicourtcourt_standards_apiget_party_role_group)
  * [`unicourt.court_standards_api.get_party_role_groups`](#unicourtcourt_standards_apiget_party_role_groups)
- [Logical Operators](#logical-operators-21)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----partyrolegroupqueryobject)
  * [`unicourt.court_standards_api.get_party_roles_by_keyword`](#unicourtcourt_standards_apiget_party_roles_by_keyword)
- [Logical Operators](#logical-operators-22)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----partyrolequeryobject)
  * [`unicourt.court_standards_api.list_area_of_law`](#unicourtcourt_standards_apilist_area_of_law)
- [Logical Operators](#logical-operators-23)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----areaoflawqueryobject)
  * [`unicourt.court_standards_api.list_case_type_groups`](#unicourtcourt_standards_apilist_case_type_groups)
- [Logical Operators](#logical-operators-24)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casetypegroupqueryobject)
  * [`unicourt.court_standards_api.list_court_systems`](#unicourtcourt_standards_apilist_court_systems)
- [Logical Operators](#logical-operators-25)
  * [All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject](#all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtsystemqueryobject)
  * [`unicourt.judge_analytics_api.get_associated_norm_parties`](#unicourtjudge_analytics_apiget_associated_norm_parties)
- [Terms and Connectors](#terms-and-connectors-22)
- [Example Query](#example-query-22)
  * [`unicourt.judge_analytics_api.get_norm_judge_details`](#unicourtjudge_analytics_apiget_norm_judge_details)
  * [`unicourt.judge_analytics_api.get_norm_judge_search_results_by_id`](#unicourtjudge_analytics_apiget_norm_judge_search_results_by_id)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normjudgesearchqueryobject)
  * [`unicourt.judge_analytics_api.list_associated_norm_attorneys`](#unicourtjudge_analytics_apilist_associated_norm_attorneys)
- [Terms and Connectors](#terms-and-connectors-23)
- [Example Query](#example-query-23)
  * [`unicourt.judge_analytics_api.list_law_firms_associated_with_judge`](#unicourtjudge_analytics_apilist_law_firms_associated_with_judge)
- [Terms and Connectors](#terms-and-connectors-24)
- [Example Query](#example-query-24)
  * [`unicourt.judge_analytics_api.search_norm_judges`](#unicourtjudge_analytics_apisearch_norm_judges)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normjudgesearchqueryobject-1)
  * [`unicourt.law_firm_analytics_api.get_associated_norm_judges`](#unicourtlaw_firm_analytics_apiget_associated_norm_judges)
- [Terms and Connectors](#terms-and-connectors-25)
- [Example Query](#example-query-25)
  * [`unicourt.law_firm_analytics_api.get_norm_law_firm_by_id`](#unicourtlaw_firm_analytics_apiget_norm_law_firm_by_id)
  * [`unicourt.law_firm_analytics_api.get_norm_law_firm_search_result_by_id`](#unicourtlaw_firm_analytics_apiget_norm_law_firm_search_result_by_id)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormLawFirmSearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normlawfirmsearchqueryobject)
  * [`unicourt.law_firm_analytics_api.list_associated_norm_attorneys`](#unicourtlaw_firm_analytics_apilist_associated_norm_attorneys)
- [Terms and Connectors](#terms-and-connectors-26)
- [Example Query](#example-query-26)
  * [`unicourt.law_firm_analytics_api.list_associated_norm_parties`](#unicourtlaw_firm_analytics_apilist_associated_norm_parties)
- [Terms and Connectors](#terms-and-connectors-27)
- [Example Query](#example-query-27)
  * [`unicourt.law_firm_analytics_api.search_law_firms`](#unicourtlaw_firm_analytics_apisearch_law_firms)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormLawFirmSearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normlawfirmsearchqueryobject-1)
  * [`unicourt.pacer_api.import_pacer_case_by_court_using_case_number_get`](#unicourtpacer_apiimport_pacer_case_by_court_using_case_number_get)
  * [`unicourt.pacer_api.search_all_courts_cases`](#unicourtpacer_apisearch_all_courts_cases)
  * [`unicourt.pacer_api.search_all_courts_cases_0`](#unicourtpacer_apisearch_all_courts_cases_0)
  * [`unicourt.pacer_api.search_appeal_courts_cases`](#unicourtpacer_apisearch_appeal_courts_cases)
  * [`unicourt.pacer_api.search_appeal_courts_cases_0`](#unicourtpacer_apisearch_appeal_courts_cases_0)
  * [`unicourt.pacer_api.search_bankruptcy_cases`](#unicourtpacer_apisearch_bankruptcy_cases)
  * [`unicourt.pacer_api.search_bankruptcy_courts`](#unicourtpacer_apisearch_bankruptcy_courts)
  * [`unicourt.pacer_api.search_civil_cases`](#unicourtpacer_apisearch_civil_cases)
  * [`unicourt.pacer_api.search_civil_cases_in_courts`](#unicourtpacer_apisearch_civil_cases_in_courts)
  * [`unicourt.pacer_api.search_criminal_cases`](#unicourtpacer_apisearch_criminal_cases)
  * [`unicourt.pacer_api.search_criminal_cases_0`](#unicourtpacer_apisearch_criminal_cases_0)
  * [`unicourt.pacer_api.search_multi_district_court_cases`](#unicourtpacer_apisearch_multi_district_court_cases)
  * [`unicourt.pacer_api.search_multi_district_court_cases_0`](#unicourtpacer_apisearch_multi_district_court_cases_0)
  * [`unicourt.pacer_credential_api.get_pacer_credential`](#unicourtpacer_credential_apiget_pacer_credential)
  * [`unicourt.pacer_credential_api.list_pacer_credentials`](#unicourtpacer_credential_apilist_pacer_credentials)
  * [`unicourt.pacer_credential_api.register_pacer_credential`](#unicourtpacer_credential_apiregister_pacer_credential)
  * [`unicourt.pacer_credential_api.remove_for_user_id`](#unicourtpacer_credential_apiremove_for_user_id)
  * [`unicourt.party_analytics_api.get_associated_norm_attorneys`](#unicourtparty_analytics_apiget_associated_norm_attorneys)
- [Terms and Connectors](#terms-and-connectors-28)
- [Example Query](#example-query-28)
  * [`unicourt.party_analytics_api.get_norm_party_details`](#unicourtparty_analytics_apiget_norm_party_details)
  * [`unicourt.party_analytics_api.get_norm_party_search_results_by_id`](#unicourtparty_analytics_apiget_norm_party_search_results_by_id)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normpartysearchqueryobject)
  * [`unicourt.party_analytics_api.list_associated_norm_law_firms`](#unicourtparty_analytics_apilist_associated_norm_law_firms)
- [Terms and Connectors](#terms-and-connectors-29)
- [Example Query](#example-query-29)
  * [`unicourt.party_analytics_api.list_judges_associated_with_norm_party`](#unicourtparty_analytics_apilist_judges_associated_with_norm_party)
- [Terms and Connectors](#terms-and-connectors-30)
- [Example Query](#example-query-30)
  * [`unicourt.party_analytics_api.search_norm_parties`](#unicourtparty_analytics_apisearch_norm_parties)
  * [All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject](#all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normpartysearchqueryobject-1)
  * [`unicourt.usage_api.get_api_usage_by_billing_cycle`](#unicourtusage_apiget_api_usage_by_billing_cycle)
  * [`unicourt.usage_api.get_api_usage_by_date`](#unicourtusage_apiget_api_usage_by_date)
  * [`unicourt.usage_api.list_previous_billing_cycles`](#unicourtusage_apilist_previous_billing_cycles)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=UniCourt&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from unicourt_python_sdk import UniCourt, ApiException

unicourt = UniCourt(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Law Firms the attorney has worked for.
    get_associated_law_firms_response = unicourt.attorney_analytics_api.get_associated_law_firms(
        norm_attorney_id="NATYfwmXwRHS279WPY",
        page_number=1,
        q="",
    )
    print(get_associated_law_firms_response)
except ApiException as e:
    print("Exception when calling AttorneyAnalyticsAPIApi.get_associated_law_firms: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["details"])
        pprint(e.body["message"])
        pprint(e.body["object"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["details"])
        pprint(e.body["message"])
        pprint(e.body["object"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["details"])
        pprint(e.body["message"])
        pprint(e.body["object"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from unicourt_python_sdk import UniCourt, ApiException

unicourt = UniCourt(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Law Firms the attorney has worked for.
        get_associated_law_firms_response = await unicourt.attorney_analytics_api.aget_associated_law_firms(
            norm_attorney_id="NATYfwmXwRHS279WPY",
            page_number=1,
            q="",
        )
        print(get_associated_law_firms_response)
    except ApiException as e:
        print("Exception when calling AttorneyAnalyticsAPIApi.get_associated_law_firms: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["code"])
            pprint(e.body["details"])
            pprint(e.body["message"])
            pprint(e.body["object"])
        if e.status == 500:
            pprint(e.body["code"])
            pprint(e.body["details"])
            pprint(e.body["message"])
            pprint(e.body["object"])
        if e.status == 404:
            pprint(e.body["code"])
            pprint(e.body["details"])
            pprint(e.body["message"])
            pprint(e.body["object"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from unicourt_python_sdk import UniCourt, ApiException

unicourt = UniCourt(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Law Firms the attorney has worked for.
    get_associated_law_firms_response = unicourt.attorney_analytics_api.raw.get_associated_law_firms(
        norm_attorney_id="NATYfwmXwRHS279WPY",
        page_number=1,
        q="",
    )
    pprint(get_associated_law_firms_response.body)
    pprint(get_associated_law_firms_response.body["associated_norm_law_firm_array"])
    pprint(get_associated_law_firms_response.body["next_page_api"])
    pprint(get_associated_law_firms_response.body["previous_page_api"])
    pprint(get_associated_law_firms_response.body["total_count"])
    pprint(get_associated_law_firms_response.body["total_pages"])
    pprint(get_associated_law_firms_response.headers)
    pprint(get_associated_law_firms_response.status)
    pprint(get_associated_law_firms_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AttorneyAnalyticsAPIApi.get_associated_law_firms: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["details"])
        pprint(e.body["message"])
        pprint(e.body["object"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["details"])
        pprint(e.body["message"])
        pprint(e.body["object"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["details"])
        pprint(e.body["message"])
        pprint(e.body["object"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `unicourt.attorney_analytics_api.get_associated_law_firms`<a id="unicourtattorney_analytics_apiget_associated_law_firms"></a>

Returns a list of Law Firms the norm Attorney has worked for.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all LawFirms associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_law_firms_response = unicourt.attorney_analytics_api.get_associated_law_firms(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_attorney_id: `str`<a id="norm_attorney_id-str"></a>

Norm ID of Attorney.    - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormLawFirmResponse`](./unicourt_python_sdk/pydantic/associated_norm_law_firm_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorney/{normAttorneyId}/associatedNormLawFirms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.attorney_analytics_api.get_judges_associated_with_attorney`<a id="unicourtattorney_analytics_apiget_judges_associated_with_attorney"></a>

This endpoint returns information on all judges which have appeared in cases with the attorney specified by the normAttorneyId. The returned judges are ordered in descending order of number of cases shared with the relevant attorney.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all judges associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_judges_associated_with_attorney_response = unicourt.attorney_analytics_api.get_judges_associated_with_attorney(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_attorney_id: `str`<a id="norm_attorney_id-str"></a>

Norm ID of Attorney.    - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormJudgeResponse`](./unicourt_python_sdk/pydantic/associated_norm_judge_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorney/{normAttorneyId}/associatedNormJudges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.attorney_analytics_api.get_norm_attorney_by_id`<a id="unicourtattorney_analytics_apiget_norm_attorney_by_id"></a>

This endpoint retrieves information on the attorney in our normalized attorney database which matches the normAttorneyId specified in the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_attorney_by_id_response = unicourt.attorney_analytics_api.get_norm_attorney_by_id(
    norm_attorney_id="NATYs4P6kDBkhKL8CF",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_attorney_id: `str`<a id="norm_attorney_id-str"></a>

Norm ID of Attorney.    - minimum: 18   - maximum: 18 

#### 🔄 Return<a id="🔄-return"></a>

[`NormAttorney`](./unicourt_python_sdk/pydantic/norm_attorney.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorney/{normAttorneyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.attorney_analytics_api.get_norm_attorney_search_results`<a id="unicourtattorney_analytics_apiget_norm_attorney_search_results"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormAttorneySearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normattorneysearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_attorney_search_results_response = unicourt.attorney_analytics_api.get_norm_attorney_search_results(
    norm_attorney_search_id="ASRCJxUHYsgddr4Hc5",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_attorney_search_id: `str`<a id="norm_attorney_search_id-str"></a>

Norm Attorney Search information for the given normAttorneySearchId.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormAttorneySearchResponse`](./unicourt_python_sdk/pydantic/norm_attorney_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorneySearch/{normAttorneySearchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.attorney_analytics_api.list_associated_norm_parties`<a id="unicourtattorney_analytics_apilist_associated_norm_parties"></a>

Returns a list of Parties the Attorney has represented.
<br><br>
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object.. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all parties associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_associated_norm_parties_response = unicourt.attorney_analytics_api.list_associated_norm_parties(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_attorney_id: `str`<a id="norm_attorney_id-str"></a>

Norm ID of Attorney.    - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormPartyResponse`](./unicourt_python_sdk/pydantic/associated_norm_party_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorney/{normAttorneyId}/associatedNormParties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.attorney_analytics_api.search_attorney_info`<a id="unicourtattorney_analytics_apisearch_attorney_info"></a>

### This endpoint retrieves information, including the normAttorneyId, on all attorneys in our normalized attorney database which match the request parameters. All query parameters supported by this API can be found in the schema section below.<a id="this-endpoint-retrieves-information-including-the-normattorneyid-on-all-attorneys-in-our-normalized-attorney-database-which-match-the-request-parameters-all-query-parameters-supported-by-this-api-can-be-found-in-the-schema-section-below"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_attorney_info_response = unicourt.attorney_analytics_api.search_attorney_info(
    q="normAttorneyId:\"NATYhUvNaef3b2iP8D\"",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters.</a> 

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormAttorneySearchResponse`](./unicourt_python_sdk/pydantic/norm_attorney_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorneySearch` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.authentication_api.generate_new_token`<a id="unicourtauthentication_apigenerate_new_token"></a>

This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_new_token_response = unicourt.authentication_api.generate_new_token(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Your Client ID obtainable by logging into your UniCourt account.

##### client_secret: `str`<a id="client_secret-str"></a>

Your Client Secret ID obtainable by logging into your UniCourt account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessTokenRequest`](./unicourt_python_sdk/type/access_token_request.py)
The endpoint accepts your Client ID and Client Secret ID as part of the request.

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./unicourt_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/generateNewToken` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.authentication_api.get_all_token_ids`<a id="unicourtauthentication_apiget_all_token_ids"></a>

An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_token_ids_response = unicourt.authentication_api.get_all_token_ids(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Your Client ID obtainable by logging into your UniCourt account.

##### client_secret: `str`<a id="client_secret-str"></a>

Your Client Secret ID obtainable by logging into your UniCourt account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessTokenRequest`](./unicourt_python_sdk/type/access_token_request.py)
The endpoint accepts your Client ID and Client Secret ID as part of the request.

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenIdListResponse`](./unicourt_python_sdk/pydantic/access_token_id_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/listAllTokenIds` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.authentication_api.invalidate_access_token`<a id="unicourtauthentication_apiinvalidate_access_token"></a>

An endpoint which allows you to invalidate a given access token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invalidate_access_token_response = unicourt.authentication_api.invalidate_access_token(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
    token_id="TKID384a057WFC3Dp3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Your Client ID obtainable by logging into your UniCourt account.

##### client_secret: `str`<a id="client_secret-str"></a>

Your Client Secret ID obtainable by logging into your UniCourt account.

##### token_id: `str`<a id="token_id-str"></a>

The Token ID of token being invalidated

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvalidateAccessTokenRequest`](./unicourt_python_sdk/type/invalidate_access_token_request.py)
The endpoint accepts your Client ID, Client Secret ID and the Token ID for the access token you wish to invalidate as part of the request. You can obtain a list of all Token IDs from the /listAllTokenIds endpoint within this API.

#### 🔄 Return<a id="🔄-return"></a>

[`Success`](./unicourt_python_sdk/pydantic/success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invalidateToken` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.authentication_api.invalidate_all_tokens`<a id="unicourtauthentication_apiinvalidate_all_tokens"></a>

An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invalidate_all_tokens_response = unicourt.authentication_api.invalidate_all_tokens(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Your Client ID obtainable by logging into your UniCourt account.

##### client_secret: `str`<a id="client_secret-str"></a>

Your Client Secret ID obtainable by logging into your UniCourt account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessTokenRequest`](./unicourt_python_sdk/type/access_token_request.py)
The endpoint accepts your Client ID and Secret Client ID as part of the request.

#### 🔄 Return<a id="🔄-return"></a>

[`Success`](./unicourt_python_sdk/pydantic/success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invalidateAllTokens` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.callback_api.list_callbacks_with_count`<a id="unicourtcallback_apilist_callbacks_with_count"></a>

Get list of callback types with count for a requested Date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_callbacks_with_count_response = unicourt.callback_api.list_callbacks_with_count(
    date="2022-03-08T00:00:00.000Z",
    status="IN_PROGRESS",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `datetime`<a id="date-datetime"></a>

Date for which fetch the callback type list. By default, the date will be set to current date.

##### status: `str`<a id="status-str"></a>

Status of the callbacks. Default status will fetch all callbacks.

#### 🔄 Return<a id="🔄-return"></a>

[`CallbackListResponse`](./unicourt_python_sdk/pydantic/callback_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/callbacks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_case_class`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_case_class"></a>

Get Analytics by Case Class.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by Case Class  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_case_class_response = unicourt.case_analytics_api.get_case_count_analytics_by_case_class(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCaseClassResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_case_class_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCaseClass` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_case_filed_date`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_case_filed_date"></a>

Get Case Count Analytics grouped by Filing Date.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by case filed date of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_case_filed_date_response = unicourt.case_analytics_api.get_case_count_analytics_by_case_filed_date(
    page_number=1,
    group_by="Yearly",
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### group_by: `str`<a id="group_by-str"></a>

GroupBy

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCaseFiledDateResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_case_filed_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCaseFiledDate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_case_type_group`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_case_type_group"></a>

Get Analytics by Case Type Group.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by case type catgeory of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_case_type_group_response = unicourt.case_analytics_api.get_case_count_analytics_by_case_type_group(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCaseTypeGroupResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_case_type_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCaseTypeGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_court`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_court"></a>

Get Case Count Analytics grouped by Court.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by Court of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_court_response = unicourt.case_analytics_api.get_case_count_analytics_by_court(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCourtResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_court_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCourt` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_court_location`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_court_location"></a>

Get Case Count Analytics grouped by Court Location.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by court location  of all cases with court id CORTV4vCEaKrhystBz and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=courtId:"CORTV4vCEaKrhystBz" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_court_location_response = unicourt.case_analytics_api.get_case_count_analytics_by_court_location(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCourtLocationResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_court_location_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCourtLocation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_court_system`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_court_system"></a>

Get Case Count Analytics grouped by Court System.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by court system of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_court_system_response = unicourt.case_analytics_api.get_case_count_analytics_by_court_system(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCourtSystemResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_court_system_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCourtSystem` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_court_type`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_court_type"></a>

Get Case Count Analytics grouped by Court Type.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by court type  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_court_type_response = unicourt.case_analytics_api.get_case_count_analytics_by_court_type(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCourtTypeResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_court_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCourtType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_jurisdiction_geo`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_jurisdiction_geo"></a>

Get Case Count Analytics grouped by Jurisdiction Geo.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by jurisdiction geo of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_jurisdiction_geo_response = unicourt.case_analytics_api.get_case_count_analytics_by_jurisdiction_geo(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByJurisdictionGeoResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_jurisdiction_geo_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByJurisdictionGeo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_norm_attorney`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_norm_attorney"></a>

Returns Case Analytics by Attorney.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm attorney of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_norm_attorney_response = unicourt.case_analytics_api.get_case_count_analytics_by_norm_attorney(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormAttorneyResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_attorney_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByNormAttorney` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_norm_judge`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_norm_judge"></a>

Returns Case Analytics by Judge.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm judge of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_norm_judge_response = unicourt.case_analytics_api.get_case_count_analytics_by_norm_judge(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormJudgeResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_judge_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByNormJudge` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_norm_law_firm`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_norm_law_firm"></a>

Returns Case Analytics by Norm Law Firm.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm lawfirm  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_norm_law_firm_response = unicourt.case_analytics_api.get_case_count_analytics_by_norm_law_firm(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormLawFirmResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_law_firm_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByNormLawFirm` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_norm_party`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_norm_party"></a>

Returns Case Analytics by Party.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm party of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_norm_party_response = unicourt.case_analytics_api.get_case_count_analytics_by_norm_party(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormPartyResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_party_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByNormParty` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_attorney_for_norm_attorney`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_opposing_norm_attorney_for_norm_attorney"></a>

Returns Case Analytics by Attorney.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normPartyId** | Single Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Single Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Single Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDiNU45NWikKVxSH"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm attorney with norm id NATYY29p78c7UoyJJ of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_opposing_norm_attorney_for_norm_attorney_response = unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_attorney_for_norm_attorney(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_attorney_id: `str`<a id="norm_attorney_id-str"></a>

Norm ID of Attorney.    - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormAttorneyResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_attorney_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normAttorney/{normAttorneyId}/caseCountAnalyticsByOpposingNormAttorney` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm"></a>

Returns Case Analytics by Norm Law Firm.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Single Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYp7kmEQtt8jQ3eQ"** |
| **normPartyId** | Single Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Single Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm lawfirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm_response = unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_law_firm_id: `str`<a id="norm_law_firm_id-str"></a>

Norm  ID of the Law Firm.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormLawFirmResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_law_firm_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirm/{normLawFirmId}/caseCountAnalyticsByOpposingNormLawFirm` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_party_for_a_norm_party`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_opposing_norm_party_for_a_norm_party"></a>

Returns Case Analytics by Opposing Norm Party.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Single Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normLawFirmId** | Single Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Single Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by norm party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_opposing_norm_party_for_a_norm_party_response = unicourt.case_analytics_api.get_case_count_analytics_by_opposing_norm_party_for_a_norm_party(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_party_id: `str`<a id="norm_party_id-str"></a>

Norm ID of the Party.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByNormPartyResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_norm_party_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normParty/{normPartyId}/caseCountAnalyticsByOpposingNormParty` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_party_role`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_party_role"></a>

Returns Case Analytics by Party Type.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by party role of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_party_role_response = unicourt.case_analytics_api.get_case_count_analytics_by_party_role(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByPartyRoleResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_party_role_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByPartyRole` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_analytics_by_party_role_group`<a id="unicourtcase_analytics_apiget_case_count_analytics_by_party_role_group"></a>

Returns Case Analytics by Party Type Group.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by Party Role Group of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_analytics_by_party_role_group_response = unicourt.case_analytics_api.get_case_count_analytics_by_party_role_group(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByPartyRoleGroupResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_party_role_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByPartyRoleGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_by_area_of_law`<a id="unicourtcase_analytics_apiget_case_count_by_area_of_law"></a>

Get Case Count Analytics by Area Of Law.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by Area Of Law of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_by_area_of_law_response = unicourt.case_analytics_api.get_case_count_by_area_of_law(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByAreaOfLawResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_area_of_law_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByAreaOfLaw` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_analytics_api.get_case_count_by_case_type`<a id="unicourtcase_analytics_apiget_case_count_by_case_type"></a>

Get Case Count Analytics by Case Type.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get case count grouped by case types  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_count_by_case_type_response = unicourt.case_analytics_api.get_case_count_by_case_type(
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseCountAnalyticsByCaseTypeResponse`](./unicourt_python_sdk/pydantic/case_count_analytics_by_case_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseCountAnalyticsByCaseType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_associated_attorney_details`<a id="unicourtcase_docket_apiget_associated_attorney_details"></a>

Retrieve the attorneys in the case with the specified partyId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_attorney_details_response = unicourt.case_docket_api.get_associated_attorney_details(
    party_id="PRTYgu537f3901f406",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### party_id: `str`<a id="party_id-str"></a>

Retrieve the party with the specified partyId value.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PartyAttorneyAssociations`](./unicourt_python_sdk/pydantic/party_attorney_associations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/party/{partyId}/associatedAttorneys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_associated_parties`<a id="unicourtcase_docket_apiget_associated_parties"></a>

Retrieve the parties represented by the attorney with the specified attorneyId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_parties_response = unicourt.case_docket_api.get_associated_parties(
    attorney_id="ATTYgr3ae043d84ebc",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attorney_id: `str`<a id="attorney_id-str"></a>

Retrieve the parties represented by the attorney with the specified attorneyId value.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PartyAttorneyAssociations`](./unicourt_python_sdk/pydantic/party_attorney_associations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attorney/{attorneyId}/associatedParties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_attorney_details`<a id="unicourtcase_docket_apiget_attorney_details"></a>

Retrieve the attorney with the specified attorneyId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attorney_details_response = unicourt.case_docket_api.get_attorney_details(
    attorney_id="ATTYgu01be2e4de654",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attorney_id: `str`<a id="attorney_id-str"></a>

Retrieve the attorney with the specified attorneyId value.

#### 🔄 Return<a id="🔄-return"></a>

[`Attorney`](./unicourt_python_sdk/pydantic/attorney.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attorney/{attorneyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_attorneys_by_case_id`<a id="unicourtcase_docket_apiget_attorneys_by_case_id"></a>

Retrieve the attorneys in the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attorneys_by_case_id_response = unicourt.case_docket_api.get_attorneys_by_case_id(
    case_id="CASEgq5943bd47a6d2",
    is_visible=True,
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### is_visible: `bool`<a id="is_visible-bool"></a>

Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`Attorneys`](./unicourt_python_sdk/pydantic/attorneys.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/attorneys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_case_info`<a id="unicourtcase_docket_apiget_case_info"></a>

Retrieve the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_info_response = unicourt.case_docket_api.get_case_info(
    case_id="CASEgr45196c84f3ff",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

#### 🔄 Return<a id="🔄-return"></a>

[`Case`](./unicourt_python_sdk/pydantic/case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_case_parties`<a id="unicourtcase_docket_apiget_case_parties"></a>

Retrieve the parties involved in the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_parties_response = unicourt.case_docket_api.get_case_parties(
    case_id="CASEgq8f4cea2d8e1a",
    is_visible=True,
    page_number=1,
    party_role_id="aaaaaaaaaaaaaaaaaa",
    party_role_group_id="aaaaaaaaaaaaaaaaaa",
    attorney_representation_type_id="aaaaaaaaaaaaaaaaaa",
    party_classification_type="INDIVIDUAL",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### is_visible: `bool`<a id="is_visible-bool"></a>

Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

##### party_role_id: `str`<a id="party_role_id-str"></a>

Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.

##### party_role_group_id: `str`<a id="party_role_group_id-str"></a>

Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.

##### attorney_representation_type_id: `str`<a id="attorney_representation_type_id-str"></a>

Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.

##### party_classification_type: `str`<a id="party_classification_type-str"></a>

Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.

#### 🔄 Return<a id="🔄-return"></a>

[`Parties`](./unicourt_python_sdk/pydantic/parties.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/parties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_docket_entries`<a id="unicourtcase_docket_apiget_docket_entries"></a>

Retrieve the docket entries in the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_docket_entries_response = unicourt.case_docket_api.get_docket_entries(
    case_id="CASEgle0bf14b74a96",
    docket_number=1,
    sort_by="latest to oldest",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### docket_number: `int`<a id="docket_number-int"></a>

Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.

##### sort_by: `str`<a id="sort_by-str"></a>

Sort the retrieved docket entries in ascending order or descending order of date.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`DocketEntries`](./unicourt_python_sdk/pydantic/docket_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/docketEntries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_hearings_for_case`<a id="unicourtcase_docket_apiget_hearings_for_case"></a>

Gets Hearings for a requested Case ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_hearings_for_case_response = unicourt.case_docket_api.get_hearings_for_case(
    case_id="CASEar3c45901ef267",
    sort_by="latest to oldest",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### sort_by: `str`<a id="sort_by-str"></a>

Specify the sort order of hearings in the case with the specified caseId.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`Hearings`](./unicourt_python_sdk/pydantic/hearings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/hearings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_judge_details`<a id="unicourtcase_docket_apiget_judge_details"></a>

Retrieve the judge with the specified judgeId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_judge_details_response = unicourt.case_docket_api.get_judge_details(
    judge_id="JUDGbaf564ec55624a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### judge_id: `str`<a id="judge_id-str"></a>

Retrieve the judge with the specified judgeId value.

#### 🔄 Return<a id="🔄-return"></a>

[`Judge`](./unicourt_python_sdk/pydantic/judge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/judge/{judgeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_judges_for_case`<a id="unicourtcase_docket_apiget_judges_for_case"></a>

Retrieve the judges involved in the specified case.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_judges_for_case_response = unicourt.case_docket_api.get_judges_for_case(
    case_id="CASEgq6e6ea66cd91d",
    is_visible=True,
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### is_visible: `bool`<a id="is_visible-bool"></a>

Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`Judges`](./unicourt_python_sdk/pydantic/judges.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/judges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_party_details`<a id="unicourtcase_docket_apiget_party_details"></a>

Retrieve the party with the specified partyId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_party_details_response = unicourt.case_docket_api.get_party_details(
    party_id="PRTYgla171a8952aed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### party_id: `str`<a id="party_id-str"></a>

Retrieve the party with the specified partyId value.

#### 🔄 Return<a id="🔄-return"></a>

[`Party`](./unicourt_python_sdk/pydantic/party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/party/{partyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_primary_documents`<a id="unicourtcase_docket_apiget_primary_documents"></a>

Retrieve the primary documents in the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_primary_documents_response = unicourt.case_docket_api.get_primary_documents(
    case_id="CASEgq5da86597e9a4",
    docket_number=1,
    in_library=True,
    after_first_fetch_date="1970-01-01T00:00:00.00Z",
    library_date="1970-01-01T00:00:00.00Z",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### docket_number: `int`<a id="docket_number-int"></a>

Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.

##### in_library: `bool`<a id="in_library-bool"></a>

Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.

##### after_first_fetch_date: `Optional[datetime]`<a id="after_first_fetch_date-optionaldatetime"></a>

Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.

##### library_date: `Optional[datetime]`<a id="library_date-optionaldatetime"></a>

Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`DocketEntryPrimaryDocuments`](./unicourt_python_sdk/pydantic/docket_entry_primary_documents.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/docketEntries/primaryDocuments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_related_cases`<a id="unicourtcase_docket_apiget_related_cases"></a>

Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_related_cases_response = unicourt.case_docket_api.get_related_cases(
    case_id="CASEba328623913f9f",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`RelatedCases`](./unicourt_python_sdk/pydantic/related_cases.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/relatedCases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_docket_api.get_secondary_documents_for_docket_entries`<a id="unicourtcase_docket_apiget_secondary_documents_for_docket_entries"></a>

Retrieve the secondary documents in the case with the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_secondary_documents_for_docket_entries_response = unicourt.case_docket_api.get_secondary_documents_for_docket_entries(
    case_id="CASEgq5da86597e9a4",
    docket_number=1,
    in_library=True,
    after_first_fetch_date="1970-01-01T00:00:00.00Z",
    library_date="1970-01-01T00:00:00.00Z",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Retrieve the case with the specified caseId value.

##### docket_number: `int`<a id="docket_number-int"></a>

Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.

##### in_library: `bool`<a id="in_library-bool"></a>

Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.

##### after_first_fetch_date: `Optional[datetime]`<a id="after_first_fetch_date-optionaldatetime"></a>

Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.

##### library_date: `Optional[datetime]`<a id="library_date-optionaldatetime"></a>

Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`DocketEntrySecondaryDocuments`](./unicourt_python_sdk/pydantic/docket_entry_secondary_documents.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/docketEntries/secondaryDocuments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_documents_api.add_document_order`<a id="unicourtcase_documents_apiadd_document_order"></a>

Add Case Document Order for requested Document Ids.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_document_order_response = unicourt.case_documents_api.add_document_order(
    case_document_id="CDOCcre989d654fa05",
    is_preview_only=True,
    pacer_options={
        "pacer_client_code": "Test UniCourt API",
        "pacer_user_id": "URKYwer3tyh5r56gq2",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_document_id: `str`<a id="case_document_id-str"></a>

Document ID which you want to order.

##### is_preview_only: `bool`<a id="is_preview_only-bool"></a>

Flag value to determine if the document order is a preview order or no.

##### pacer_options: [`CaseDocumentOrderPacerOptions`](./unicourt_python_sdk/type/case_document_order_pacer_options.py)<a id="pacer_options-casedocumentorderpaceroptionsunicourt_python_sdktypecase_document_order_pacer_optionspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CaseDocumentOrderRequest`](./unicourt_python_sdk/type/case_document_order_request.py)
If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseDocumentOrderCallback`](./unicourt_python_sdk/pydantic/case_document_order_callback.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseDocumentOrder` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_documents_api.get_callback_by_id`<a id="unicourtcase_documents_apiget_callback_by_id"></a>

Get Case Document Order Callback for a requested Case Document Order Callback Id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_callback_by_id_response = unicourt.case_documents_api.get_callback_by_id(
    case_document_order_callback_id="CBDOnrb63f4808bjO3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_document_order_callback_id: `str`<a id="case_document_order_callback_id-str"></a>

Unique Id for the Case Document Order Callback.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseDocumentOrderCallback`](./unicourt_python_sdk/pydantic/case_document_order_callback.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseDocumentOrder/callbacks/{caseDocumentOrderCallbackId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_documents_api.get_document_details_by_document_id`<a id="unicourtcase_documents_apiget_document_details_by_document_id"></a>

Gets details for a requested Document ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_details_by_document_id_response = unicourt.case_documents_api.get_document_details_by_document_id(
    case_document_id="CDOCag3e5eba43b870",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_document_id: `str`<a id="case_document_id-str"></a>

Specific Case Dcoument ID for which you want the data for.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseDocument`](./unicourt_python_sdk/pydantic/case_document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseDocument/{caseDocumentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_documents_api.get_documents_for_case`<a id="unicourtcase_documents_apiget_documents_for_case"></a>

Gets Documents for a requested Case ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_documents_for_case_response = unicourt.case_documents_api.get_documents_for_case(
    case_id="CASEgua4c06e119ea8",
    in_library=True,
    after_first_fetch_date="1970-01-01T00:00:00.00Z",
    library_date="1970-01-01T00:00:00.00Z",
    first_fetch_date="1970-01-01T00:00:00.00Z",
    sort_by="latest to oldest",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

Case ID for which you want the data for.

##### in_library: `bool`<a id="in_library-bool"></a>

Filter all the documents those are added to the UniCourt library.

##### after_first_fetch_date: `Optional[datetime]`<a id="after_first_fetch_date-optionaldatetime"></a>

Get all the documents which were added to the case on or after a specific date.

##### library_date: `Optional[datetime]`<a id="library_date-optionaldatetime"></a>

Sort all the documents based on the date when the document was added to the UniCourt Library.

##### first_fetch_date: `Optional[datetime]`<a id="first_fetch_date-optionaldatetime"></a>

Sort all the documents based on the date it was fetched from the source site.

##### sort_by: `str`<a id="sort_by-str"></a>

Sort documents with document order.

##### page_number: `int`<a id="page_number-int"></a>

The page for which the result should be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseDocuments`](./unicourt_python_sdk/pydantic/case_documents.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/case/{caseId}/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_documents_api.get_downloadable_url_for_document`<a id="unicourtcase_documents_apiget_downloadable_url_for_document"></a>

Gets downloadable URL for a requested Document ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_downloadable_url_for_document_response = unicourt.case_documents_api.get_downloadable_url_for_document(
    case_document_id="CDOCaqe42a86394f63",
    is_preview_document=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_document_id: `str`<a id="case_document_id-str"></a>

Document ID which you want to download.

##### is_preview_document: `bool`<a id="is_preview_document-bool"></a>

If the document you want to download is a preview of a document.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseDocumentsApiGetDownloadableUrlForDocumentResponse`](./unicourt_python_sdk/pydantic/case_documents_api_get_downloadable_url_for_document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseDocumentDownload/{caseDocumentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_documents_api.list_document_order_callbacks`<a id="unicourtcase_documents_apilist_document_order_callbacks"></a>

Get Case Document Order Callback list for a requested Date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_document_order_callbacks_response = unicourt.case_documents_api.list_document_order_callbacks(
    date="2022-03-08T10:17:56.000Z",
    status="",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `datetime`<a id="date-datetime"></a>

Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.

##### status: `str`<a id="status-str"></a>

Status of Document Order callbacks. Default status will fetch all callbacks.

##### page_number: `int`<a id="page_number-int"></a>

Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseDocumentOrderCallbackListResponse`](./unicourt_python_sdk/pydantic/case_document_order_callback_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseDocumentOrder/callbacks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_export_api.get_callback_by_id`<a id="unicourtcase_export_apiget_callback_by_id"></a>

Retrieve the specified case export callback object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_callback_by_id_response = unicourt.case_export_api.get_callback_by_id(
    case_export_callback_id="CBCEG63f4e233eXqD1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_export_callback_id: `str`<a id="case_export_callback_id-str"></a>

The caseExportCallbackId value of the case export callback object to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseExportCallback`](./unicourt_python_sdk/pydantic/case_export_callback.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseExport/callbacks/{caseExportCallbackId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_export_api.get_callback_list_for_requested_date`<a id="unicourtcase_export_apiget_callback_list_for_requested_date"></a>

Retrieve callbacks according to the specified criteria.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_callback_list_for_requested_date_response = unicourt.case_export_api.get_callback_list_for_requested_date(
    date="2022-03-08T10:17:56.000Z",
    status="",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `datetime`<a id="date-datetime"></a>

The date for which callbacks are to be retrieved.

##### status: `str`<a id="status-str"></a>

The status code of the callbacks to be retrieved.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the callbacks to be retrieved.<br>   - Minimum: 1 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseExportCallbackListResponse`](./unicourt_python_sdk/pydantic/case_export_callback_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseExport/callbacks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_export_api.get_case_export_by_case_id`<a id="unicourtcase_export_apiget_case_export_by_case_id"></a>

Retrieve information about the specified case export.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_export_by_case_id_response = unicourt.case_export_api.get_case_export_by_case_id(
    case_id="CASEhq2c3224900a48",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

The caseId value of the case for which case export information is to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseExportCallback`](./unicourt_python_sdk/pydantic/case_export_callback.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseExport/{caseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_search_api.get_search_results_by_case_search_id`<a id="unicourtcase_search_apiget_search_results_by_case_search_id"></a>

Retrieve the search results corresponding to the specified caseSearchId value.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_search_results_by_case_search_id_response = unicourt.case_search_api.get_search_results_by_case_search_id(
    case_search_id="CSRCU3qFUH8BjLnba5",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_search_id: `str`<a id="case_search_id-str"></a>

Case Search information for the given caseSearchId.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseSearchResponse`](./unicourt_python_sdk/pydantic/case_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseSearch/{caseSearchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_search_api.search_by_keyword_expressions`<a id="unicourtcase_search_apisearch_by_keyword_expressions"></a>

This endpoint retrieves cases according to keyword expressions you provide.
<br>
Keyword expressions are constructed according to the rules described below.
<br><br>
This API supports multiple use cases:
  - Search for multiple keywords  `Google OR Facebook`.
  - Search within particular attributes.
  - Relational search using terms and connectors.
  - And much more.
----

## Allowed Connectors in Keyword Expressions<a id="allowed-connectors-in-keyword-expressions"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find cases containing each of the terms joined by AND connectors.|**personal AND injury**|
| **OR**  |Find cases containing any of the terms joined by OR connectors.|**order OR decision**|
| **NOT** |Find cases that do not contain the specified term.|**personal AND NOT injury**.  Find cases with the word “personal” and not “injury”.|
| **“[phrase]”** |Find the exact phrase placed between the quotation marks.|**"personal injury”**|
| **~**  |Find cases in which the specified words appear near each other. For example, "personal injury" ~ 5 targets cases in which the word "personal" appears within 5 words of the word "injury".|**“personal injury” ~ 5** - Find cases with “personal” within five words of “injury”. |
| **( … )** |Specifies the order in which connectors are to be appliied in a keyword expression.| **personal AND (injury OR fall)** - Find cases with the word personal injury or personal fall.|

<br><br>
## Fields and Connectors Searching<a id="fields-and-connectors-searching"></a>
| Filed | Description  | Example |
| ------| ------|------|
|**caseNumber** |Find cases with the specified case number (i.e., docket number).| **caseNumber:"2020-L-007212"** - Find cases whose case number matches given case number number.|
|**caseName** |Find cases with the specified case title.| **caseName:"THOMAS P. CARNEY, INC. VS BEHLER JAMES Et Al"** - Find cases whose case name matches given terms.|
|**Court**|Find cases in the specified court.|**(Court:(name:(New York)))** - Find cases in New York state.<br>|
|**CaseStatus**|Find cases witih the specified case status.|**(CaseStatus:(name:Disposed))** - All disposed cases.<br>|
|**CaseType**|Find cases of the specified case type. | **(CaseType:(name:Property))** - Cases with case type “property”.|
|**Party** | Find cases involving the specified party.| **(Party:(name:Apple))** - Find cases involving Apple. |
|**partyId**|Find cases involving a party with the specified partyId value.|**(Party:(partyId:"PRTYgu1ffe866484c2"))**|
|**PartyRole** | Find cases in which at least one party has the specified party role. | **(Party:((PartyRole:(name:"plaintiff"))))** - Find cases with party role “plaintiff”.<br><br> **(Party:((PartyRole:(name:defendant)) AND (AttorneyRepresentationType:(name:(Attorney represented)))))** - Find cases where a party is acting as defendant and represented by an attorney.|
|**AttorneyRepresentationType**| Find cases in which at least one party has the specified attorney representation type.|**(Party:(AttorneyRepresentationType:(name:"attorney represented")))** - Find cases where a party is represented by an attorney. |
|**Attorney** | Find cases involving the specified attorney. | **(Attorney:(name:"David Boies"))** - Find cases involving the attorney David Boies. |
|**AttorneyType**|Find cases involving at least one attorney of the specified attorney type.|**(Attorney:((AttorneyType:(name:"Lead Attorney"))))**|
|**Judge** |Find cases involving the specified judge. | **(Judge:(name:"Posner"))** - Find cases involving Judge Posner.|
|**JudgeType**|Find cases involving at least one judge of the specified judge type.|**(Judge:((JudgeType:(name:"Magistrate"))))**|
|**CaseStats**|Find cases with the specified case statistics.|**(CaseStats:(partyCount:[10 TO 100]))** - Find cases involving 10 to 100 parties.<br>**(CaseStats:(attorneyCount:[2 TO 40]))** - Find cases involving 2 to 40 attorneys.<br>**(CaseStats:(judgeCount:[\* TO 2]))** - Find cases involving up to 2 judges. <br>**(CaseStats:(docketEntryCount:[10 TO 100]))** - Find cases having 10 to 100 docket_entries. <br>**(CaseStats:(allCaseDocumentCount:[10 TO 100]))** - Find cases having 10 to 100 documents. |
|**filedDate** | Find cases that were filed on the specified date or within the specified date range. | **filedDate:[2020-03-15 TO 2021-12-01]** - Find the most recently filed cases between March 15, 2020 and December 1, 2021 (inclusive). |
|**lastFetchDate**| Find cases in which UniCourt last checked for updates on the specified date or within the specified date range. |**(lastFetchDate:[now-60d TO \*\])** - Find cases that were updated by UniCourt in the last 60 days. |
|**lastFetchDateWithUpdates**|Find cases in which UniCourt last detected an update on the specified date or within the specified date range.|**(lastFetchDateWithUpdates:[now-6d TO \*\])** - Find cases for the changes found on court site in last 6 days.|
|**participantsLastFetchDate**|Find cases in which information cocnerning participants was last updated on the specified date or within the specified date range.|**(participantsLastFetchDate:[now-6d TO \*\])** - Find cases where the participant's information was updated in last 6 days.|
|**DocketEntry**|Find cases in which at least one docket entry contains the specified text.|**(DocketEntry:(text:(Motion to Compel Responses) AND docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00]))** - Find cases with docket text “Motion to Compel Responses” and action date between 2020-01-01 and 2020-05-01.|
|**docketEntryDate**|Find cases in which at least one docket entry was made on the specified date or within the specified date range.|**(DocketEntry:(docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00])) AND (CaseStats:(allCaseDocumentCount:[0 TO 10]))** - Find cases with docket action date between 2020-01-01 and 2020-05-01 having up to 10 documents associated with it.|
|**HearingDate**| Find cases with at least one hearing scheduled for the specified date or within the specified date range.|**(Hearing:(hearingDate:[now TO now+10d]))** - Find cases where hearing is scheduled in next 10 days.|
|**HearingDate**| Search for cases where hearing is going to happen in 10 to 20days.|**(Hearing:(hearingDate:[now+10d TO now+20d]))** - Find cases where hearing is scheduled in next 10 to 20 days.|
|**JurisdictionGeo**|Find cases in which the law of the specified state governs.|**(JurisdictionGeo:(state:"New York"))**- Find cases where Jurisdiction is New York state.|
|**Party Address Exists**|Find cases with Party addresses.|**(Party:(Contact:(Address:(stateName:\*))))**- Returns only those cases that have addresses for parties.|
|**Document**|Find cases with specific document name and preview is available for the document.|**(CaseDocument:(name:"civil case cover sheet" AND isPreviewAvailable:true))**- Returns cases with document civil case cover sheet and preview is available.|

<br><br>
---
## Party Sub Filter Examples<a id="party-sub-filter-examples"></a>
|Example |Explanation |
|---|---|
|**(Party:(name:google AND (PartyRole:(name:"plaintiff"))))**|Find cases involving at least one plaintiff whose name contains the term "Google".|
|**(Party:(name:"OTELIA PEREIDA" AND (AttorneyRepresentationType:(name:"Attorney represented")))) AND (Attorney:(name:"Law Offices of Todd M Friedman"))**|Find cases where the Party is *OTELIA PEREIDA* and is represented by the attorney *Law Offices of Todd M Friedman*.|

---
### All query parameters supported for this API can be found in below schema section. Schema -->  CaseSearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema-----casesearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_by_keyword_expressions_response = unicourt.case_search_api.search_by_keyword_expressions(
    q="caseNumber:\"JP07-22-DC00026818\"",
    sort="filedDate",
    order="desc",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Query parameter for keyword expressions.</a> 

##### sort: `str`<a id="sort-str"></a>

Query parameter specifying how results are to be sorted. Results can be sorted according to filedDate or relevancy.

##### order: `str`<a id="order-str"></a>

Query parameter specifying whether search result are sorted in ascending or descending order.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseSearchResponse`](./unicourt_python_sdk/pydantic/case_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseSearch` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_tracking_api.add_case_track`<a id="unicourtcase_tracking_apiadd_case_track"></a>

Track the specified case.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_case_track_response = unicourt.case_tracking_api.add_case_track(
    case_track_params={
        "case_id": "CASEhq9d8b72d0800c",
    },
    schedule={
        "days": [1, 3, 5],
        "type": "weekly",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_track_params: [`CaseUpdateRequest`](./unicourt_python_sdk/type/case_update_request.py)<a id="case_track_params-caseupdaterequestunicourt_python_sdktypecase_update_requestpy"></a>


##### schedule: [`CaseTrackSchedule`](./unicourt_python_sdk/type/case_track_schedule.py)<a id="schedule-casetrackscheduleunicourt_python_sdktypecase_track_schedulepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CaseTrackRequest`](./unicourt_python_sdk/type/case_track_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Success`](./unicourt_python_sdk/pydantic/success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseTrack` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_tracking_api.get_case_track`<a id="unicourtcase_tracking_apiget_case_track"></a>

Retrieve case tracking information for the specified caseId value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_track_response = unicourt.case_tracking_api.get_case_track(
    case_id="CASEak99a698ea5413",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

The caseId value for which case tracking information is to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseTrack`](./unicourt_python_sdk/pydantic/case_track.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseTrack/{caseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_tracking_api.get_case_track_list`<a id="unicourtcase_tracking_apiget_case_track_list"></a>

Retrieve a list of all tracked cases.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_track_list_response = unicourt.case_tracking_api.get_case_track_list(
    last_fetch_date="2022-03-08T10:17:56.000Z",
    last_fetch_date_with_updates="2022-03-08T10:17:56.000Z",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_fetch_date: `datetime`<a id="last_fetch_date-datetime"></a>

The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz. 

##### last_fetch_date_with_updates: `datetime`<a id="last_fetch_date_with_updates-datetime"></a>

The date on which changes were last found in the case information. 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved.<br>   - Minimum: 1 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseTrackListResponse`](./unicourt_python_sdk/pydantic/case_track_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseTracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_tracking_api.remove_case_track_by_id`<a id="unicourtcase_tracking_apiremove_case_track_by_id"></a>

Remove Case Track for a specific Case Id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_case_track_by_id_response = unicourt.case_tracking_api.remove_case_track_by_id(
    case_id="CASEak99a698ea5413",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

The caseId value for which case tracking information is to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`Success`](./unicourt_python_sdk/pydantic/success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseTrack/{caseId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_update_api.add_case_update_for_case_id`<a id="unicourtcase_update_apiadd_case_update_for_case_id"></a>

Request case updates for the specified case.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_case_update_for_case_id_response = unicourt.case_update_api.add_case_update_for_case_id(
    case_id="CASEhq9d8b72d0800c",
    pacer_options={
        "additional_page_array": [{
    "fetch_if_older_than_days": 30,
    "page": "caseSummary",
}, , ],
        "fetch_participants_if_older_than_days": 30,
        "pacer_client_code": "Test UniCourt API",
        "pacer_user_id": "URKYwer3tyh5r56gq2",
        "refresh_type": "fetchNewDocketEntries",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

UniCourt's Case Id for update.

##### pacer_options: [`CaseUpdatePacerOptions`](./unicourt_python_sdk/type/case_update_pacer_options.py)<a id="pacer_options-caseupdatepaceroptionsunicourt_python_sdktypecase_update_pacer_optionspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CaseUpdateRequest`](./unicourt_python_sdk/type/case_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CaseUpdate`](./unicourt_python_sdk/pydantic/case_update.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseUpdate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_update_api.get_case_updates`<a id="unicourtcase_update_apiget_case_updates"></a>

Retrieve case updates for the specified date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_updates_response = unicourt.case_update_api.get_case_updates(
    case_id="CASEak99a698ea5413",
    requested_date="2022-03-08T10:17:56.000Z",
    status="",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

The caseId value of the case for which updates should be retrieved.

##### requested_date: `datetime`<a id="requested_date-datetime"></a>

The date for which case updates are to be retrieved.

##### status: `str`<a id="status-str"></a>

Status of the case updates to be retrieved.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the callbacks to be retrieved.<br>   - Minimum: 1 

#### 🔄 Return<a id="🔄-return"></a>

[`CaseUpdateListResponse`](./unicourt_python_sdk/pydantic/case_update_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseUpdates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.case_update_api.get_case_updates_by_case_id`<a id="unicourtcase_update_apiget_case_updates_by_case_id"></a>

Retrieve case updates for the specified case object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_updates_by_case_id_response = unicourt.case_update_api.get_case_updates_by_case_id(
    case_id="CASEeqfb72ba4726f1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_id: `str`<a id="case_id-str"></a>

The caseId value of the case object for which updates are to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseUpdate`](./unicourt_python_sdk/pydantic/case_update.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/caseUpdate/{caseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_availability_api.get_court_coverage_by_court_id`<a id="unicourtcourt_availability_apiget_court_coverage_by_court_id"></a>

Determine whether the specified court is covered by UniCourt.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_coverage_by_court_id_response = unicourt.court_availability_api.get_court_coverage_by_court_id(
    court_id="CORTV4vCEaKrhystBz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_id: `str`<a id="court_id-str"></a>

The courtId value of the target court.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtCoverage`](./unicourt_python_sdk/pydantic/court_coverage.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courtCoverage/{courtId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.associated_court_for_jurisdiction_geo`<a id="unicourtcourt_standards_apiassociated_court_for_jurisdiction_geo"></a>

Returns Associated Court for given Jurisdiction Geo.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
associated_court_for_jurisdiction_geo_response = unicourt.court_standards_api.associated_court_for_jurisdiction_geo(
    jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### jurisdiction_geo_id: `str`<a id="jurisdiction_geo_id-str"></a>

jurisdictionGeoId

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

Sort field.

##### order: `str`<a id="order-str"></a>

Sort order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtResponse`](./unicourt_python_sdk/pydantic/court_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/jurisdictionGeo/{jurisdictionGeoId}/courts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_additional_charge_info`<a id="unicourtcourt_standards_apiget_additional_charge_info"></a>

Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargeadditionaldataqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_additional_charge_info_response = unicourt.court_standards_api.get_additional_charge_info(
    q="chargeAdditionalDataId:\"CHADoLU7sWaGjWtkBx\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired charge additional data.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeAdditionalDataResponse`](./unicourt_python_sdk/pydantic/charge_additional_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeAdditionalData` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_appeal_courts_for_court`<a id="unicourtcourt_standards_apiget_appeal_courts_for_court"></a>

Retrieve the appeals courts associated with the specified court.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_appeal_courts_for_court_response = unicourt.court_standards_api.get_appeal_courts_for_court(
    court_id="CORThSxcef8eGUSkuC",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_id: `str`<a id="court_id-str"></a>

The courtId value of the target court.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtResponse`](./unicourt_python_sdk/pydantic/court_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/court/{courtId}/appealCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_area_of_law`<a id="unicourtcourt_standards_apiget_area_of_law"></a>

Retrieve the specified area of law.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_area_of_law_response = unicourt.court_standards_api.get_area_of_law(
    area_of_law_id="AOFLGAd9Ah5qkTRNw9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### area_of_law_id: `str`<a id="area_of_law_id-str"></a>

The areaOfLawId value of the desired area of law.

#### 🔄 Return<a id="🔄-return"></a>

[`AreaOfLaw`](./unicourt_python_sdk/pydantic/area_of_law.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/areaOfLaw/{areaOfLawId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_attorney_rep_type`<a id="unicourtcourt_standards_apiget_attorney_rep_type"></a>

Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above.
## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----attorneyrepresentationtypequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attorney_rep_type_response = unicourt.court_standards_api.get_attorney_rep_type(
    q="attorneyRepresentationTypeId: \"ATRPYgPMGJufoCsR6Q\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the attorney representation type.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`AttorneyRepresentationTypeResponse`](./unicourt_python_sdk/pydantic/attorney_representation_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/attorneyRepresentationType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_attorney_rep_type_0`<a id="unicourtcourt_standards_apiget_attorney_rep_type_0"></a>

Retrieve the specified attorney representation type.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attorney_rep_type_0_response = unicourt.court_standards_api.get_attorney_rep_type_0(
    attorney_representation_type_id="ATRPYgPMGJufoCsR6Q",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attorney_representation_type_id: `str`<a id="attorney_representation_type_id-str"></a>

The attorneyRepresentationTypeId value of the desired attorney representation type.

#### 🔄 Return<a id="🔄-return"></a>

[`AttorneyRepresentationType`](./unicourt_python_sdk/pydantic/attorney_representation_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/attorneyRepresentationType/{attorneyRepresentationTypeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_attorney_type_object`<a id="unicourtcourt_standards_apiget_attorney_type_object"></a>

Retrieve a specified attorney type object.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attorney_type_object_response = unicourt.court_standards_api.get_attorney_type_object(
    attorney_type_id="ATYPWXtARwvzu5HLcf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attorney_type_id: `str`<a id="attorney_type_id-str"></a>

The attorneyTypeId value of the desired attorney type.

#### 🔄 Return<a id="🔄-return"></a>

[`AttorneyType`](./unicourt_python_sdk/pydantic/attorney_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/attorneyType/{attorneyTypeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_attorney_type_using_keyword_expression`<a id="unicourtcourt_standards_apiget_attorney_type_using_keyword_expression"></a>

Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----attorneytypequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attorney_type_using_keyword_expression_response = unicourt.court_standards_api.get_attorney_type_using_keyword_expression(
    q="attorneyTypeId:\"ATYPWXtARwvzu5HLcf\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the attorney type.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`AttorneyTypeResponse`](./unicourt_python_sdk/pydantic/attorney_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/attorneyType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_class_by_id`<a id="unicourtcourt_standards_apiget_case_class_by_id"></a>

Retrieve the specified case class.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_class_by_id_response = unicourt.court_standards_api.get_case_class_by_id(
    case_class_id="CSCLNjbKTN7Yfo2wdb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_class_id: `str`<a id="case_class_id-str"></a>

The caseClassId value of the desired case class.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseClass`](./unicourt_python_sdk/pydantic/case_class.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseClass/{caseClassId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_class_by_keyword`<a id="unicourtcourt_standards_apiget_case_class_by_keyword"></a>

Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----caseclassqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_class_by_keyword_response = unicourt.court_standards_api.get_case_class_by_keyword(
    q="caseClassId:\"CSCLNjbKTN7Yfo2wdb\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired case class.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseClassResponse`](./unicourt_python_sdk/pydantic/case_class_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseClass` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_relationship_type_by_id`<a id="unicourtcourt_standards_apiget_case_relationship_type_by_id"></a>

Retrieve the specified case relationship type.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_relationship_type_by_id_response = unicourt.court_standards_api.get_case_relationship_type_by_id(
    case_relationship_type_id="CRTPgkmnzpiBXstT3s",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_relationship_type_id: `str`<a id="case_relationship_type_id-str"></a>

The caseRelationshipTypeId value of the desired case relationship type.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseRelationshipType`](./unicourt_python_sdk/pydantic/case_relationship_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseRelationshipType/{caseRelationshipTypeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_relationship_types`<a id="unicourtcourt_standards_apiget_case_relationship_types"></a>

Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----caserelationshiptypequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_relationship_types_response = unicourt.court_standards_api.get_case_relationship_types(
    q="caseRelationshipTypeId: \"CRTPgkmnzpiBXstT3s\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the case relationship type.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseRelationshipTypeResponse`](./unicourt_python_sdk/pydantic/case_relationship_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseRelationshipType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_status_by_id`<a id="unicourtcourt_standards_apiget_case_status_by_id"></a>

Retrieve the specified case status.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_status_by_id_response = unicourt.court_standards_api.get_case_status_by_id(
    case_status_id="CSSTBtqf3R2LYFt4j4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_status_id: `str`<a id="case_status_id-str"></a>

The caseStatusId value of the desired case status.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseStatus`](./unicourt_python_sdk/pydantic/case_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseStatus/{caseStatusId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_status_by_keyword`<a id="unicourtcourt_standards_apiget_case_status_by_keyword"></a>

Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casestatusqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_status_by_keyword_response = unicourt.court_standards_api.get_case_status_by_keyword(
    q="caseStatusId: \"CSSTBtqf3R2LYFt4j4\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired case status.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseStatusResponse`](./unicourt_python_sdk/pydantic/case_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_status_group`<a id="unicourtcourt_standards_apiget_case_status_group"></a>

Retrieve the specified case status group.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_status_group_response = unicourt.court_standards_api.get_case_status_group(
    case_status_group_id="CSSG6ERqyFdydo52WK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_status_group_id: `str`<a id="case_status_group_id-str"></a>

The caseStatusGroupId value of the desired case status group.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseStatusGroup`](./unicourt_python_sdk/pydantic/case_status_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseStatusGroup/{caseStatusGroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_status_group_using_keyword_expression`<a id="unicourtcourt_standards_apiget_case_status_group_using_keyword_expression"></a>

Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casestatusgroupqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_status_group_using_keyword_expression_response = unicourt.court_standards_api.get_case_status_group_using_keyword_expression(
    q="caseStatusGroupId:\"CSSG6ERqyFdydo52WK\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired case status group.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseStatusGroupResponse`](./unicourt_python_sdk/pydantic/case_status_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseStatusGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_type`<a id="unicourtcourt_standards_apiget_case_type"></a>

Retrieve the specified case type.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_type_response = unicourt.court_standards_api.get_case_type(
    case_type_id="CTYPoLU7sWaGjWtkBx",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_type_id: `str`<a id="case_type_id-str"></a>

The caseTypeId value of the desired case type.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseType`](./unicourt_python_sdk/pydantic/case_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseType/{caseTypeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_type_group`<a id="unicourtcourt_standards_apiget_case_type_group"></a>

Retrieve the specified case type group.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_type_group_response = unicourt.court_standards_api.get_case_type_group(
    case_type_group_id="CTYGSpWaVityBQndsv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### case_type_group_id: `str`<a id="case_type_group_id-str"></a>

caseTypeGroupId

#### 🔄 Return<a id="🔄-return"></a>

[`CaseTypeGroup`](./unicourt_python_sdk/pydantic/case_type_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseTypeGroup/{caseTypeGroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_case_types_by_keyword`<a id="unicourtcourt_standards_apiget_case_types_by_keyword"></a>

Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casetypequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_case_types_by_keyword_response = unicourt.court_standards_api.get_case_types_by_keyword(
    q="caseTypeId: \"CTYPoLU7sWaGjWtkBx\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseTypeResponse`](./unicourt_python_sdk/pydantic/case_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_cause_of_action`<a id="unicourtcourt_standards_apiget_cause_of_action"></a>

Retrieve the specified cause of action.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cause_of_action_response = unicourt.court_standards_api.get_cause_of_action(
    cause_of_action_id="CATNoLU7sWaGjWtkBx",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cause_of_action_id: `str`<a id="cause_of_action_id-str"></a>

The causeOfActionId value of the desired cause of action.

#### 🔄 Return<a id="🔄-return"></a>

[`CauseOfAction`](./unicourt_python_sdk/pydantic/cause_of_action.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/causeOfAction/{causeOfActionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_cause_of_action_additional_data`<a id="unicourtcourt_standards_apiget_cause_of_action_additional_data"></a>

Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----causeofactionadditionaldataqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cause_of_action_additional_data_response = unicourt.court_standards_api.get_cause_of_action_additional_data(
    q="causeOfActionAdditionalDataId:\"CAADiHoKn66p3bkcNs\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired cause of action additional data.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CauseOfActionAdditionalDataResponse`](./unicourt_python_sdk/pydantic/cause_of_action_additional_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/causeOfActionAdditionalData` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_cause_of_action_additional_data_0`<a id="unicourtcourt_standards_apiget_cause_of_action_additional_data_0"></a>

Retrieve the specified cause of action additional data.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cause_of_action_additional_data_0_response = unicourt.court_standards_api.get_cause_of_action_additional_data_0(
    cause_of_action_additional_data_id="CAADoLU7sWaGjWtkBx",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cause_of_action_additional_data_id: `str`<a id="cause_of_action_additional_data_id-str"></a>

The causeOfActionAdditionalDataId value of the desired cause of action additional data.

#### 🔄 Return<a id="🔄-return"></a>

[`CauseOfActionAdditionalData`](./unicourt_python_sdk/pydantic/cause_of_action_additional_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/causeOfActionAdditionalData/{causeOfActionAdditionalDataId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_cause_of_action_by_keyword`<a id="unicourtcourt_standards_apiget_cause_of_action_by_keyword"></a>

Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----causeofactionqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cause_of_action_by_keyword_response = unicourt.court_standards_api.get_cause_of_action_by_keyword(
    q="causeOfActionId:\"CATNiHoKn66p3bkcNs\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired cause of action.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CauseOfActionResponse`](./unicourt_python_sdk/pydantic/cause_of_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/causeOfAction` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_cause_of_action_group`<a id="unicourtcourt_standards_apiget_cause_of_action_group"></a>

Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----causeofactiongroupqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cause_of_action_group_response = unicourt.court_standards_api.get_cause_of_action_group(
    q="causeOfActionGroupId:\"CAGPiHoKn66p3bkcNs\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired cause of action group.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CauseOfActionGroupResponse`](./unicourt_python_sdk/pydantic/cause_of_action_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/causeOfActionGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_cause_of_action_group_0`<a id="unicourtcourt_standards_apiget_cause_of_action_group_0"></a>

Retrieve the specified cause of action group.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cause_of_action_group_0_response = unicourt.court_standards_api.get_cause_of_action_group_0(
    cause_of_action_group_id="CAGPoLU7sWaGjWtkBx",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cause_of_action_group_id: `str`<a id="cause_of_action_group_id-str"></a>

causeOfActionGroupId

#### 🔄 Return<a id="🔄-return"></a>

[`CauseOfActionGroup`](./unicourt_python_sdk/pydantic/cause_of_action_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/causeOfActionGroup/{causeOfActionGroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_additional_data`<a id="unicourtcourt_standards_apiget_charge_additional_data"></a>

Retrieve the specified charge additional data.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_additional_data_response = unicourt.court_standards_api.get_charge_additional_data(
    charge_additional_data_id="CHADiHoKn66p3bkcNs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### charge_additional_data_id: `str`<a id="charge_additional_data_id-str"></a>

The chargeAdditionalDataId value of the desired charge additional data.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeAdditionalData`](./unicourt_python_sdk/pydantic/charge_additional_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeAdditionalData/{chargeAdditionalDataId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_by_id`<a id="unicourtcourt_standards_apiget_charge_by_id"></a>

Retrieve the specified charge.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_by_id_response = unicourt.court_standards_api.get_charge_by_id(
    charge_id="CHRGiHoKn66p3bkcNs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### charge_id: `str`<a id="charge_id-str"></a>

The chargeId value of the desired charge.

#### 🔄 Return<a id="🔄-return"></a>

[`Charge`](./unicourt_python_sdk/pydantic/charge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/charge/{chargeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_degree_by_id`<a id="unicourtcourt_standards_apiget_charge_degree_by_id"></a>

Retrieve the specified charge degree.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_degree_by_id_response = unicourt.court_standards_api.get_charge_degree_by_id(
    charge_degree_id="CHDGiHoKn66p3bkcNs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### charge_degree_id: `str`<a id="charge_degree_id-str"></a>

The chargeDegreeId value of the desired charge degree.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeDegree`](./unicourt_python_sdk/pydantic/charge_degree.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeDegree/{chargeDegreeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_degree_using_keyword_expression`<a id="unicourtcourt_standards_apiget_charge_degree_using_keyword_expression"></a>

Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargedegreequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_degree_using_keyword_expression_response = unicourt.court_standards_api.get_charge_degree_using_keyword_expression(
    q="chargeDegreeId:\"CHDGiHoKn66p3bkcNs\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired charge degree.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeDegreeResponse`](./unicourt_python_sdk/pydantic/charge_degree_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeDegree` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_group`<a id="unicourtcourt_standards_apiget_charge_group"></a>

Retrieve the specified charge group.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_group_response = unicourt.court_standards_api.get_charge_group(
    charge_group_id="CHGPiHoKn66p3bkcNs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### charge_group_id: `str`<a id="charge_group_id-str"></a>

The chargeGroupId value of the desired charge group.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeGroup`](./unicourt_python_sdk/pydantic/charge_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeGroup/{chargeGroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_groups_by_keyword`<a id="unicourtcourt_standards_apiget_charge_groups_by_keyword"></a>

Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargegroupqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_groups_by_keyword_response = unicourt.court_standards_api.get_charge_groups_by_keyword(
    q="chargeGroupId:\"CHRGoLU7sWaGjWtkBx\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired charge group.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeGroupResponse`](./unicourt_python_sdk/pydantic/charge_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_severity`<a id="unicourtcourt_standards_apiget_charge_severity"></a>

Retrieve the specified charge severity.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_severity_response = unicourt.court_standards_api.get_charge_severity(
    charge_severity_id="CHSEiHoKn66p3bkcNs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### charge_severity_id: `str`<a id="charge_severity_id-str"></a>

The chargeSeverityId value of the desired charge severity.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeSeverity`](./unicourt_python_sdk/pydantic/charge_severity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeSeverity/{chargeSeverityId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charge_severity_by_keyword`<a id="unicourtcourt_standards_apiget_charge_severity_by_keyword"></a>

Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargeseverityqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charge_severity_by_keyword_response = unicourt.court_standards_api.get_charge_severity_by_keyword(
    q="chargeSeverityId:\"CHSEiHoKn66p3bkcNs\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired charge severity.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeSeverityResponse`](./unicourt_python_sdk/pydantic/charge_severity_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/chargeSeverity` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_charges_using_keyword`<a id="unicourtcourt_standards_apiget_charges_using_keyword"></a>

Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----chargequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charges_using_keyword_response = unicourt.court_standards_api.get_charges_using_keyword(
    q="chargeId:\"CHRGoLU7sWaGjWtkBx\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired charge.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`ChargeResponse`](./unicourt_python_sdk/pydantic/charge_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/charge` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_location`<a id="unicourtcourt_standards_apiget_court_location"></a>

Retrieve the specified court location or court locations.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtlocationqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_location_response = unicourt.court_standards_api.get_court_location(
    q="courtLocationId:\"COLO9g3fhYM4bmxveA\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtLocationResponse`](./unicourt_python_sdk/pydantic/court_location_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtLocation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_location_object`<a id="unicourtcourt_standards_apiget_court_location_object"></a>

Contains the Court Location Object.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_location_object_response = unicourt.court_standards_api.get_court_location_object(
    court_location_id="COLOV75AKgqMqnfVhM",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_location_id: `str`<a id="court_location_id-str"></a>

courtLocationId

#### 🔄 Return<a id="🔄-return"></a>

[`CourtLocation`](./unicourt_python_sdk/pydantic/court_location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtLocation/{courtLocationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_locations`<a id="unicourtcourt_standards_apiget_court_locations"></a>

Retrieve the court locations associated with the specified court.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_locations_response = unicourt.court_standards_api.get_court_locations(
    court_id="CORThSxcef8eGUSkuC",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_id: `str`<a id="court_id-str"></a>

The courtId value of the target court.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtLocationResponse`](./unicourt_python_sdk/pydantic/court_location_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/court/{courtId}/courtLocations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_object`<a id="unicourtcourt_standards_apiget_court_object"></a>

Retrieve information about a specified court.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_object_response = unicourt.court_standards_api.get_court_object(
    court_id="CORThSxcef8eGUSkuC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_id: `str`<a id="court_id-str"></a>

The courtId value of the target court.

#### 🔄 Return<a id="🔄-return"></a>

[`Court`](./unicourt_python_sdk/pydantic/court.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/court/{courtId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_service_status`<a id="unicourtcourt_standards_apiget_court_service_status"></a>

Retrieve the status of one or more courts using a keyword expression.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtservicestatusqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_service_status_response = unicourt.court_standards_api.get_court_service_status(
    q="courtServiceStatusId: \"CTSSf45fd1bd792e97\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtServiceStatusResponse`](./unicourt_python_sdk/pydantic/court_service_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtServiceStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_service_status_by_id`<a id="unicourtcourt_standards_apiget_court_service_status_by_id"></a>

Retrieve the court status of the specified court.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_service_status_by_id_response = unicourt.court_standards_api.get_court_service_status_by_id(
    court_service_status_id="CTSSf45fd1bd792e97",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_service_status_id: `str`<a id="court_service_status_id-str"></a>

The courtServiceStatusId value of the desired court.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtServiceStatus`](./unicourt_python_sdk/pydantic/court_service_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtServiceStatus/{courtServiceStatusId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_system`<a id="unicourtcourt_standards_apiget_court_system"></a>

Retrieve the specified court system.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_system_response = unicourt.court_standards_api.get_court_system(
    court_system_id="COSY4vuCtGQeAmdDdN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_system_id: `str`<a id="court_system_id-str"></a>

The courtSystemId value of the court system to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtSystem`](./unicourt_python_sdk/pydantic/court_system.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtSystem/{courtSystemId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_type_object`<a id="unicourtcourt_standards_apiget_court_type_object"></a>

Retrieve the information concerning the specific court type.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_type_object_response = unicourt.court_standards_api.get_court_type_object(
    court_type_id="COTPm8jjc2PAydpFhq",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_type_id: `str`<a id="court_type_id-str"></a>

The courtTypeId value of the court type to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtType`](./unicourt_python_sdk/pydantic/court_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtType/{courtTypeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_court_types`<a id="unicourtcourt_standards_apiget_court_types"></a>

Retrieve court types recognized by UniCourt.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courttypequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_court_types_response = unicourt.court_standards_api.get_court_types(
    q="courtTypeId:\"COTPm8jjc2PAydpFhq\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtTypeResponse`](./unicourt_python_sdk/pydantic/court_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_courts`<a id="unicourtcourt_standards_apiget_courts"></a>

Retrieve information about a specified court or courts.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_courts_response = unicourt.court_standards_api.get_courts(
    q="courtId:\"CORThSxcef8eGUSkuC\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtResponse`](./unicourt_python_sdk/pydantic/court_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/court` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_courts_by_location`<a id="unicourtcourt_standards_apiget_courts_by_location"></a>

Retrieve the courts associated with the specified court location.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_courts_by_location_response = unicourt.court_standards_api.get_courts_by_location(
    court_location_id="COLOV75AKgqMqnfVhM",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_location_id: `str`<a id="court_location_id-str"></a>

The courtLocationId value of the court location for which courts are to be retrieved.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtResponse`](./unicourt_python_sdk/pydantic/court_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtLocation/{courtLocationId}/courts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_judge_type_object`<a id="unicourtcourt_standards_apiget_judge_type_object"></a>

Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----judgetypequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_judge_type_object_response = unicourt.court_standards_api.get_judge_type_object(
    q="judgeTypeId: \"JGTPkwrfzkDJUvxpN9\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the judge type.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`JudgeTypeResponse`](./unicourt_python_sdk/pydantic/judge_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/judgeType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_judge_type_object_by_id`<a id="unicourtcourt_standards_apiget_judge_type_object_by_id"></a>

Retrieve the specified judge type.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_judge_type_object_by_id_response = unicourt.court_standards_api.get_judge_type_object_by_id(
    judge_type_id="JGTPkwrfzkDJUvxpN9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### judge_type_id: `str`<a id="judge_type_id-str"></a>

The judgeTypeId of the desired judge type.

#### 🔄 Return<a id="🔄-return"></a>

[`JudgeType`](./unicourt_python_sdk/pydantic/judge_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/judgeType/{judgeTypeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_jurisdiction_geo`<a id="unicourtcourt_standards_apiget_jurisdiction_geo"></a>

Retrieve the specified jurisdiction geography.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_jurisdiction_geo_response = unicourt.court_standards_api.get_jurisdiction_geo(
    jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### jurisdiction_geo_id: `str`<a id="jurisdiction_geo_id-str"></a>

The jurisdictionGeoId value of the desired jurisdiction geography.

#### 🔄 Return<a id="🔄-return"></a>

[`JurisdictionGeo`](./unicourt_python_sdk/pydantic/jurisdiction_geo.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/jurisdictionGeo/{jurisdictionGeoId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_jurisdiction_geo_for_court`<a id="unicourtcourt_standards_apiget_jurisdiction_geo_for_court"></a>

Retrieve one or more jurisdiction geographies using a keyword expression.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----jurisdictiongeoqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_jurisdiction_geo_for_court_response = unicourt.court_standards_api.get_jurisdiction_geo_for_court(
    q="jurisdictionGeoId:\"JUGO8s7HvM84dLvVMu\"",
    page_number=1,
    sort="state",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`JurisdictionGeoResponse`](./unicourt_python_sdk/pydantic/jurisdiction_geo_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/jurisdictionGeo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_jurisdiction_geo_objects_for_court`<a id="unicourtcourt_standards_apiget_jurisdiction_geo_objects_for_court"></a>

Retrieve the jurisdiction geography object for the specified court.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_jurisdiction_geo_objects_for_court_response = unicourt.court_standards_api.get_jurisdiction_geo_objects_for_court(
    court_id="CORThSxcef8eGUSkuC",
    page_number=1,
    sort="state",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### court_id: `str`<a id="court_id-str"></a>

The courtId value of the target court.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`JurisdictionGeoResponse`](./unicourt_python_sdk/pydantic/jurisdiction_geo_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/court/{courtId}/jurisdictionGeo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_party_role`<a id="unicourtcourt_standards_apiget_party_role"></a>

Retrieve the specified party role.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_party_role_response = unicourt.court_standards_api.get_party_role(
    party_role_id="PTYRVRgMKueGmhnxRN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### party_role_id: `str`<a id="party_role_id-str"></a>

The partyRoleId value of the desired party role.

#### 🔄 Return<a id="🔄-return"></a>

[`PartyRole`](./unicourt_python_sdk/pydantic/party_role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/partyRole/{partyRoleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_party_role_group`<a id="unicourtcourt_standards_apiget_party_role_group"></a>

Retrieve the specified party role group.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_party_role_group_response = unicourt.court_standards_api.get_party_role_group(
    party_role_group_id="PTYGBnjxbx6tKNfVEP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### party_role_group_id: `str`<a id="party_role_group_id-str"></a>

The partyRoleGroupId value of the desired party role group.

#### 🔄 Return<a id="🔄-return"></a>

[`PartyRoleGroup`](./unicourt_python_sdk/pydantic/party_role_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/partyRoleGroup/{partyRoleGroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_party_role_groups`<a id="unicourtcourt_standards_apiget_party_role_groups"></a>

Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----partyrolegroupqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_party_role_groups_response = unicourt.court_standards_api.get_party_role_groups(
    q="partyRoleGroupId: \"PTYGBnjxbx6tKNfVEP\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired party role group.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`PartyRoleGroupResponse`](./unicourt_python_sdk/pydantic/party_role_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/partyRoleGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.get_party_roles_by_keyword`<a id="unicourtcourt_standards_apiget_party_roles_by_keyword"></a>

Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----partyrolequeryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_party_roles_by_keyword_response = unicourt.court_standards_api.get_party_roles_by_keyword(
    q="partyRoleId: \"PTYRVRgMKueGmhnxRN\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression targeting the desired party role.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`PartyRoleResponse`](./unicourt_python_sdk/pydantic/party_role_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/partyRole` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.list_area_of_law`<a id="unicourtcourt_standards_apilist_area_of_law"></a>

The keyword expression targeting the desired area of law. 

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----areaoflawqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_area_of_law_response = unicourt.court_standards_api.list_area_of_law(
    q="areaOfLawId: \"AOFLGAd9Ah5qkTRNw9\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`AreaOfLawResponse`](./unicourt_python_sdk/pydantic/area_of_law_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/areaOfLaw` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.list_case_type_groups`<a id="unicourtcourt_standards_apilist_case_type_groups"></a>

Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----casetypegroupqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_case_type_groups_response = unicourt.court_standards_api.list_case_type_groups(
    q="caseTypeGroupId: \"CTYGSpWaVityBQndsv\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CaseTypeGroupResponse`](./unicourt_python_sdk/pydantic/case_type_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/caseTypeGroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.court_standards_api.list_court_systems`<a id="unicourtcourt_standards_apilist_court_systems"></a>

Retrieve information about the specified court system or court systems.

## Logical Operators<a id="logical-operators"></a>
| Connector | Description  | Example |
| ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject<a id="all-filter-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----courtsystemqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_court_systems_response = unicourt.court_standards_api.list_court_systems(
    q="courtSystemId:\"COSY4vuCtGQeAmdDdN\"",
    page_number=1,
    sort="name",
    order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> 

##### page_number: `int`<a id="page_number-int"></a>

The page number of the results to be retrieved. - minimum: 1 - maximum: 100 

##### sort: `str`<a id="sort-str"></a>

The field according to which search results are to be sorted.

##### order: `str`<a id="order-str"></a>

Whether search results are to be shown in ascending or descending order.

#### 🔄 Return<a id="🔄-return"></a>

[`CourtSystemResponse`](./unicourt_python_sdk/pydantic/court_system_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/masterData/courtSystem` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.judge_analytics_api.get_associated_norm_parties`<a id="unicourtjudge_analytics_apiget_associated_norm_parties"></a>

Returns a list of Parties A Judge has seen.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all Parties associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_norm_parties_response = unicourt.judge_analytics_api.get_associated_norm_parties(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_judge_id: `str`<a id="norm_judge_id-str"></a>

Norm  ID of the Judge.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormPartyResponse`](./unicourt_python_sdk/pydantic/associated_norm_party_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normJudge/{normJudgeId}/associatedNormParties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.judge_analytics_api.get_norm_judge_details`<a id="unicourtjudge_analytics_apiget_norm_judge_details"></a>

The Judge API allows you to look up Judge Details by normJudgeId.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_judge_details_response = unicourt.judge_analytics_api.get_norm_judge_details(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_judge_id: `str`<a id="norm_judge_id-str"></a>

Norm  ID of the Judge.   - minimum: 18   - maximum: 18 

#### 🔄 Return<a id="🔄-return"></a>

[`NormJudge`](./unicourt_python_sdk/pydantic/norm_judge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normJudge/{normJudgeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.judge_analytics_api.get_norm_judge_search_results_by_id`<a id="unicourtjudge_analytics_apiget_norm_judge_search_results_by_id"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normjudgesearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_judge_search_results_by_id_response = unicourt.judge_analytics_api.get_norm_judge_search_results_by_id(
    norm_judge_search_id="JSRCNUSK3pLGe48QcU",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_judge_search_id: `str`<a id="norm_judge_search_id-str"></a>

Norm judge Search information for the given normJudgeSearchId.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormJudgeSearchResponse`](./unicourt_python_sdk/pydantic/norm_judge_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normJudgeSearch/{normJudgeSearchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.judge_analytics_api.list_associated_norm_attorneys`<a id="unicourtjudge_analytics_apilist_associated_norm_attorneys"></a>

Returns a list of attorneys associated with a judge.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all attorneys associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_associated_norm_attorneys_response = unicourt.judge_analytics_api.list_associated_norm_attorneys(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_judge_id: `str`<a id="norm_judge_id-str"></a>

Norm  ID of the Judge.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormAttorneyResponse`](./unicourt_python_sdk/pydantic/associated_norm_attorney_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normJudge/{normJudgeId}/associatedNormAttorneys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.judge_analytics_api.list_law_firms_associated_with_judge`<a id="unicourtjudge_analytics_apilist_law_firms_associated_with_judge"></a>

Returns a list of Law Firms a Judge has heard.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLOPUfJRhw5yPxgRi"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all Law Firms associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_law_firms_associated_with_judge_response = unicourt.judge_analytics_api.list_law_firms_associated_with_judge(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_judge_id: `str`<a id="norm_judge_id-str"></a>

Norm  ID of the Judge.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormLawFirmResponse`](./unicourt_python_sdk/pydantic/associated_norm_law_firm_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normJudge/{normJudgeId}/associatedNormLawFirms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.judge_analytics_api.search_norm_judges`<a id="unicourtjudge_analytics_apisearch_norm_judges"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normjudgesearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_norm_judges_response = unicourt.judge_analytics_api.search_norm_judges(
    q="normJudgeId:\"NJUD5STmDbUZGukfQm\"",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters.</a> 

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormJudgeSearchResponse`](./unicourt_python_sdk/pydantic/norm_judge_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normJudgeSearch` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.law_firm_analytics_api.get_associated_norm_judges`<a id="unicourtlaw_firm_analytics_apiget_associated_norm_judges"></a>

Returns list of Judges faced by the Law Firm.
<br><br>
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all judges associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_norm_judges_response = unicourt.law_firm_analytics_api.get_associated_norm_judges(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_law_firm_id: `str`<a id="norm_law_firm_id-str"></a>

Norm  ID of the Law Firm.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormJudgeResponse`](./unicourt_python_sdk/pydantic/associated_norm_judge_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirm/{normLawFirmId}/associatedNormJudges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.law_firm_analytics_api.get_norm_law_firm_by_id`<a id="unicourtlaw_firm_analytics_apiget_norm_law_firm_by_id"></a>

The Law Firm API allows you to look up Law Firms by normLawFirmId.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_law_firm_by_id_response = unicourt.law_firm_analytics_api.get_norm_law_firm_by_id(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_law_firm_id: `str`<a id="norm_law_firm_id-str"></a>

Norm  ID of the Law Firm.   - minimum: 18   - maximum: 18 

#### 🔄 Return<a id="🔄-return"></a>

[`NormLawFirm`](./unicourt_python_sdk/pydantic/norm_law_firm.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirm/{normLawFirmId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.law_firm_analytics_api.get_norm_law_firm_search_result_by_id`<a id="unicourtlaw_firm_analytics_apiget_norm_law_firm_search_result_by_id"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormLawFirmSearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normlawfirmsearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_law_firm_search_result_by_id_response = unicourt.law_firm_analytics_api.get_norm_law_firm_search_result_by_id(
    norm_law_firm_search_id="LSRCeCT9pC3maopkW7",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_law_firm_search_id: `str`<a id="norm_law_firm_search_id-str"></a>

Norm law firm search information for the given normLawFirmSearchId.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormLawFirmSearchResponse`](./unicourt_python_sdk/pydantic/norm_law_firm_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirmSearch/{normLawFirmSearchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.law_firm_analytics_api.list_associated_norm_attorneys`<a id="unicourtlaw_firm_analytics_apilist_associated_norm_attorneys"></a>

Returns a list of Attorneys associated to a Law Firm.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId**  | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate**  | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>        
## Example Query<a id="example-query"></a>
Query to get all attorneys associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_associated_norm_attorneys_response = unicourt.law_firm_analytics_api.list_associated_norm_attorneys(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_law_firm_id: `str`<a id="norm_law_firm_id-str"></a>

Norm  ID of the Law Firm.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormAttorneyResponse`](./unicourt_python_sdk/pydantic/associated_norm_attorney_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirm/{normLawFirmId}/associatedNormAttorneys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.law_firm_analytics_api.list_associated_norm_parties`<a id="unicourtlaw_firm_analytics_apilist_associated_norm_parties"></a>

Returns list of Parties represented by the Law Firm.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all parties associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_associated_norm_parties_response = unicourt.law_firm_analytics_api.list_associated_norm_parties(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_law_firm_id: `str`<a id="norm_law_firm_id-str"></a>

Norm  ID of the Law Firm.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormPartyResponse`](./unicourt_python_sdk/pydantic/associated_norm_party_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirm/{normLawFirmId}/associatedNormParties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.law_firm_analytics_api.search_law_firms`<a id="unicourtlaw_firm_analytics_apisearch_law_firms"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormLawFirmSearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normlawfirmsearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_law_firms_response = unicourt.law_firm_analytics_api.search_law_firms(
    q="normLawFirmId:\"NORGDiJQPjeed2mtvx\"",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters.</a> 

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormLawFirmSearchResponse`](./unicourt_python_sdk/pydantic/norm_law_firm_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normLawFirmSearch` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.import_pacer_case_by_court_using_case_number_get`<a id="unicourtpacer_apiimport_pacer_case_by_court_using_case_number_get"></a>

Import the specified case from PACER. 

	Workflow: 

		1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database. 

		2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId. 

	Note: 

		1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee. 

		2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_pacer_case_by_court_using_case_number_get_response = unicourt.pacer_api.import_pacer_case_by_court_using_case_number_get(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="2:15-mc-12345",
    court_id="CORTjF63b8Z4d2i9UB",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The PACER username of the PACER account under which the case should be imported.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the case should be imported.

##### case_number: `str`<a id="case_number-str"></a>

The case number of the case to be imported.

##### court_id: `str`<a id="court_id-str"></a>

The courtId value of the court from which the case is to be imported.

#### 🔄 Return<a id="🔄-return"></a>

[`PACERImportCase`](./unicourt_python_sdk/pydantic/pacer_import_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacer/importCaseByCourtUsingCaseNumber` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_all_courts_cases`<a id="unicourtpacer_apisearch_all_courts_cases"></a>

Search all courts within the PACER system for a particular case.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_all_courts_cases_response = unicourt.pacer_api.search_all_courts_cases(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="21-119",
    pacer_case_id=17118,
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `Optional[int]`<a id="case_year-optionalint"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLCase`](./unicourt_python_sdk/pydantic/pcl_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/caseSearch/allCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_all_courts_cases_0`<a id="unicourtpacer_apisearch_all_courts_cases_0"></a>

Search for the specified party across all PACER case filings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_all_courts_cases_0_response = unicourt.pacer_api.search_all_courts_cases_0(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="21-119",
    pacer_case_id=1,
    last_name="Warden",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_exact_name_match=True,
    party_role_array=[
        "string_example"
    ],
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_year_from=1,
    case_year_to=1,
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The last name (for an individual) or the entity name (for a business entity) of the target party.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The first name of the target party.

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

The middle name of the target party.

##### generation: `Optional[str]`<a id="generation-optionalstr"></a>

The suffix (e.g., Jr., III) of the target party's name.

##### party_type: `Optional[str]`<a id="party_type-optionalstr"></a>

The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### party_exact_name_match: `bool`<a id="party_exact_name_match-bool"></a>

Specify whether the search string must match the name of the target party exactly.

##### party_role_array: List[`Optional[str]`]<a id="party_role_array-listoptionalstr"></a>

The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case.

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_year_from: `int`<a id="case_year_from-int"></a>

Limit the results of the search to those cases from the year specified or later

##### case_year_to: `int`<a id="case_year_to-int"></a>

Limit the results of the search to those cases from the year specified or earlier

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLParty`](./unicourt_python_sdk/pydantic/pcl_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/partySearch/allCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_appeal_courts_cases`<a id="unicourtpacer_apisearch_appeal_courts_cases"></a>

Search for PACER cases filed in U.S. Courts of Appeals.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_appeal_courts_cases_response = unicourt.pacer_api.search_appeal_courts_cases(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    nature_of_suits_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `Optional[int]`<a id="case_office-optionalint"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### nature_of_suits_array: List[`Optional[str]`]<a id="nature_of_suits_array-listoptionalstr"></a>

The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLCase`](./unicourt_python_sdk/pydantic/pcl_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/caseSearch/appealCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_appeal_courts_cases_0`<a id="unicourtpacer_apisearch_appeal_courts_cases_0"></a>

Search for the specified party across all PACER appeals cases.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_appeal_courts_cases_0_response = unicourt.pacer_api.search_appeal_courts_cases_0(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    last_name="Smith",
    first_name="John",
    middle_name="Doe",
    generation="MD",
    party_type="ptf",
    party_exact_name_match=True,
    party_role_array=[
        "string_example"
    ],
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_year_from=1,
    case_year_to=1,
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The last name (for an individual) or the entity name (for a business entity) of the target party.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The first name of the target party.

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

The middle name of the target party.

##### generation: `Optional[str]`<a id="generation-optionalstr"></a>

The suffix (e.g., Jr., III) of the target party's name.

##### party_type: `Optional[str]`<a id="party_type-optionalstr"></a>

The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### party_exact_name_match: `bool`<a id="party_exact_name_match-bool"></a>

Specify whether the search string must match the name of the target party exactly.

##### party_role_array: List[`Optional[str]`]<a id="party_role_array-listoptionalstr"></a>

The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_year_from: `int`<a id="case_year_from-int"></a>

Limit the results of the search to those cases from the year specified or later

##### case_year_to: `int`<a id="case_year_to-int"></a>

Limit the results of the search to those cases from the year specified or earlier

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLParty`](./unicourt_python_sdk/pydantic/pcl_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/partySearch/appealCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_bankruptcy_cases`<a id="unicourtpacer_apisearch_bankruptcy_cases"></a>

Search for PACER cases filed in U.S. Bankruptcy Courts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_bankruptcy_cases_response = unicourt.pacer_api.search_bankruptcy_cases(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    federal_bankruptcy_chapter_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    case_discharged_start_date="1970-01-01T00:00:00.00Z",
    case_discharged_end_date="1970-01-01T00:00:00.00Z",
    case_dismissed_start_date="1970-01-01T00:00:00.00Z",
    case_dismissed_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### federal_bankruptcy_chapter_array: List[`Optional[str]`]<a id="federal_bankruptcy_chapter_array-listoptionalstr"></a>

The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please see Appendix D for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_discharged_start_date: `Optional[datetime]`<a id="case_discharged_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

##### case_discharged_end_date: `Optional[datetime]`<a id="case_discharged_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

##### case_dismissed_start_date: `Optional[datetime]`<a id="case_dismissed_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

##### case_dismissed_end_date: `Optional[datetime]`<a id="case_dismissed_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLCase`](./unicourt_python_sdk/pydantic/pcl_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/caseSearch/bankruptcyCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_bankruptcy_courts`<a id="unicourtpacer_apisearch_bankruptcy_courts"></a>

Search for the specified party in PACER bankruptcy filings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_bankruptcy_courts_response = unicourt.pacer_api.search_bankruptcy_courts(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    last_name="Smith",
    first_name="John",
    middle_name="Doe",
    generation="MD",
    party_type="ptf",
    party_exact_name_match=True,
    party_role_array=[
        "string_example"
    ],
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_year_from=1,
    case_year_to=1,
    ssn_or_ein="string_example",
    four_digit_ssn="string_example",
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    case_discharged_start_date="1970-01-01T00:00:00.00Z",
    case_discharged_end_date="1970-01-01T00:00:00.00Z",
    case_dismissed_start_date="1970-01-01T00:00:00.00Z",
    case_dismissed_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The last name (for an individual) or the entity name (for a business entity) of the target party.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The first name of the target party.

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

The middle name of the target party.

##### generation: `Optional[str]`<a id="generation-optionalstr"></a>

The suffix (e.g., Jr., III) of the target party's name.

##### party_type: `Optional[str]`<a id="party_type-optionalstr"></a>

The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### party_exact_name_match: `bool`<a id="party_exact_name_match-bool"></a>

Specify whether the search string must match the name of the target party exactly.

##### party_role_array: List[`Optional[str]`]<a id="party_role_array-listoptionalstr"></a>

The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_year_from: `int`<a id="case_year_from-int"></a>

Limit the results of the search to those cases from the year specified or later

##### case_year_to: `int`<a id="case_year_to-int"></a>

Limit the results of the search to those cases from the year specified or earlier

##### ssn_or_ein: `Optional[str]`<a id="ssn_or_ein-optionalstr"></a>

The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.

##### four_digit_ssn: `Optional[str]`<a id="four_digit_ssn-optionalstr"></a>

The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_discharged_start_date: `Optional[datetime]`<a id="case_discharged_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

##### case_discharged_end_date: `Optional[datetime]`<a id="case_discharged_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

##### case_dismissed_start_date: `Optional[datetime]`<a id="case_dismissed_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

##### case_dismissed_end_date: `Optional[datetime]`<a id="case_dismissed_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLParty`](./unicourt_python_sdk/pydantic/pcl_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/partySearch/bankruptcyCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_civil_cases`<a id="unicourtpacer_apisearch_civil_cases"></a>

Search for civil cases filed in PACER.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_civil_cases_response = unicourt.pacer_api.search_civil_cases(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    nature_of_suits_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case.

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### nature_of_suits_array: List[`Optional[str]`]<a id="nature_of_suits_array-listoptionalstr"></a>

The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLCase`](./unicourt_python_sdk/pydantic/pcl_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/caseSearch/civilCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_civil_cases_in_courts`<a id="unicourtpacer_apisearch_civil_cases_in_courts"></a>

Search for the specified party in civil cases filed in PACER.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_civil_cases_in_courts_response = unicourt.pacer_api.search_civil_cases_in_courts(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    last_name="Smith",
    first_name="John",
    middle_name="Doe",
    generation="MD",
    party_type="ptf",
    party_exact_name_match=True,
    party_role_array=[
        "string_example"
    ],
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_year_from=1,
    case_year_to=1,
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The last name (for an individual) or the entity name (for a business entity) of the target party.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The first name of the target party.

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

The middle name of the target party.

##### generation: `Optional[str]`<a id="generation-optionalstr"></a>

The name suffix (e.g., III, MD).

##### party_type: `Optional[str]`<a id="party_type-optionalstr"></a>

The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### party_exact_name_match: `bool`<a id="party_exact_name_match-bool"></a>

Specify whether the search string must match the name of the target party exactly.

##### party_role_array: List[`Optional[str]`]<a id="party_role_array-listoptionalstr"></a>

The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_year_from: `int`<a id="case_year_from-int"></a>

Limit the results of the search to those cases from the year specified or later

##### case_year_to: `int`<a id="case_year_to-int"></a>

Limit the results of the search to those cases from the year specified or earlier

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLParty`](./unicourt_python_sdk/pydantic/pcl_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/partySearch/civilCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_criminal_cases`<a id="unicourtpacer_apisearch_criminal_cases"></a>

Search for criminal cases in PACER.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_criminal_cases_response = unicourt.pacer_api.search_criminal_cases(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLCase`](./unicourt_python_sdk/pydantic/pcl_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/caseSearch/criminalCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_criminal_cases_0`<a id="unicourtpacer_apisearch_criminal_cases_0"></a>

Search for the specified party in PACER criminal cases.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_criminal_cases_0_response = unicourt.pacer_api.search_criminal_cases_0(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="07-1026",
    pacer_case_id=1,
    last_name="Smith",
    first_name="John",
    middle_name="Doe",
    generation="MD",
    party_type="ptf",
    party_exact_name_match=True,
    party_role_array=[
        "string_example"
    ],
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_year_from=1,
    case_year_to=1,
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The last name (for an individual) or the entity name (for a business entity) of the target party.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The first name of the target party.

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

The middle name of the target party.

##### generation: `Optional[str]`<a id="generation-optionalstr"></a>

The suffix (e.g., Jr., III) of the target party's name.

##### party_type: `Optional[str]`<a id="party_type-optionalstr"></a>

The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### party_exact_name_match: `bool`<a id="party_exact_name_match-bool"></a>

Specify whether the search string must match the name of the target party exactly.

##### party_role_array: List[`Optional[str]`]<a id="party_role_array-listoptionalstr"></a>

The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_year_from: `int`<a id="case_year_from-int"></a>

Limit the results of the search to those cases from the year specified or later

##### case_year_to: `int`<a id="case_year_to-int"></a>

Limit the results of the search to those cases from the year specified or earlier

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLParty`](./unicourt_python_sdk/pydantic/pcl_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/partySearch/criminalCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_multi_district_court_cases`<a id="unicourtpacer_apisearch_multi_district_court_cases"></a>

Search for multidistrict litigation in PACER.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_multi_district_court_cases_response = unicourt.pacer_api.search_multi_district_court_cases(
    pacer_user_id="john_doe",
    pacer_client_code="john",
    case_number="12-1234",
    jpml_number=875,
    pacer_case_id=1,
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### jpml_number: `int`<a id="jpml_number-int"></a>

Master JPML Case Number.

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLCase`](./unicourt_python_sdk/pydantic/pcl_case.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/caseSearch/multiDistrictCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_api.search_multi_district_court_cases_0`<a id="unicourtpacer_apisearch_multi_district_court_cases_0"></a>

Search for the specified party in multidistrict litigation in PACER.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_multi_district_court_cases_0_response = unicourt.pacer_api.search_multi_district_court_cases_0(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    jpml_number=1,
    pacer_case_id=1,
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_exact_name_match=True,
    party_role_array=[
        "string_example"
    ],
    case_title="string_example",
    case_office=1,
    case_sequence_number=1,
    case_year=1,
    case_type_array=[
        "string_example"
    ],
    court_region_id_array=[
        "string_example"
    ],
    case_year_from=1,
    case_year_to=1,
    case_filed_start_date="1970-01-01T00:00:00.00Z",
    case_filed_end_date="1970-01-01T00:00:00.00Z",
    case_terminated_start_date="1970-01-01T00:00:00.00Z",
    case_terminated_end_date="1970-01-01T00:00:00.00Z",
    sort_parameter_query="sort=caseYear,DESC",
    case_status="open",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The username of the PACER account under which the search is to be performed.

##### pacer_client_code: `str`<a id="pacer_client_code-str"></a>

The PACER client code under which the search is to be performed.

##### case_number: `Optional[str]`<a id="case_number-optionalstr"></a>

The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).

##### jpml_number: `int`<a id="jpml_number-int"></a>

Master JPML Case Number.

##### pacer_case_id: `int`<a id="pacer_case_id-int"></a>

The PACER-assigned identifier of the target case.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The last name (for an individual) or the entity name (for a business entity) of the target party.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The first name of the target party.

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

The middle name of the target party.

##### generation: `Optional[str]`<a id="generation-optionalstr"></a>

The suffix (e.g., Jr., III) of the target party's name.

##### party_type: `Optional[str]`<a id="party_type-optionalstr"></a>

The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### party_exact_name_match: `bool`<a id="party_exact_name_match-bool"></a>

Specify whether the search string must match the name of the target party exactly.

##### party_role_array: List[`Optional[str]`]<a id="party_role_array-listoptionalstr"></a>

The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

##### case_title: `Optional[str]`<a id="case_title-optionalstr"></a>

The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

##### case_office: `int`<a id="case_office-int"></a>

The divisional office in which the case was filed.

##### case_sequence_number: `int`<a id="case_sequence_number-int"></a>

The PACER-assigned sequence number of the target case. Ex 12345

##### case_year: `int`<a id="case_year-int"></a>

The two- or four-digit year in which the target case was filed.

##### case_type_array: List[`Optional[str]`]<a id="case_type_array-listoptionalstr"></a>

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr

##### court_region_id_array: List[`Optional[str]`]<a id="court_region_id_array-listoptionalstr"></a>

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae

##### case_year_from: `int`<a id="case_year_from-int"></a>

Limit the results of the search to those cases from the year specified or later

##### case_year_to: `int`<a id="case_year_to-int"></a>

Limit the results of the search to those cases from the year specified or earlier

##### case_filed_start_date: `Optional[datetime]`<a id="case_filed_start_date-optionaldatetime"></a>

The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_filed_end_date: `Optional[datetime]`<a id="case_filed_end_date-optionaldatetime"></a>

The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_start_date: `Optional[datetime]`<a id="case_terminated_start_date-optionaldatetime"></a>

The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### case_terminated_end_date: `Optional[datetime]`<a id="case_terminated_end_date-optionaldatetime"></a>

The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

##### sort_parameter_query: `Optional[str]`<a id="sort_parameter_query-optionalstr"></a>

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

##### case_status: `Optional[str]`<a id="case_status-optionalstr"></a>

Whether the target case is marked as 'open' or 'closed' within PACER.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the search results to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PCLParty`](./unicourt_python_sdk/pydantic/pcl_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCaseLocator/partySearch/multiDistrictCourts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_credential_api.get_pacer_credential`<a id="unicourtpacer_credential_apiget_pacer_credential"></a>

Retrieve the PACER credentials for the specified PACER username.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pacer_credential_response = unicourt.pacer_credential_api.get_pacer_credential(
    pacer_user_id="URKYwer3tyh5r56gq2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The PACER username for which PACER credentials are to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PacerCredential`](./unicourt_python_sdk/pydantic/pacer_credential.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCredential/{pacerUserId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_credential_api.list_pacer_credentials`<a id="unicourtpacer_credential_apilist_pacer_credentials"></a>

List registered PACER credentials.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_pacer_credentials_response = unicourt.pacer_credential_api.list_pacer_credentials(
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 

#### 🔄 Return<a id="🔄-return"></a>

[`PacerCredentialListResponse`](./unicourt_python_sdk/pydantic/pacer_credential_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCredential` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_credential_api.register_pacer_credential`<a id="unicourtpacer_credential_apiregister_pacer_credential"></a>

Register PACER credentials with UniCourt.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_pacer_credential_response = unicourt.pacer_credential_api.register_pacer_credential(
    pacer_user_id="URKYwer3tyh5r56gq2",
    password="your password",
    default_pacer_client_code="Test UniCourt API",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

Pacer User Id.

##### password: `str`<a id="password-str"></a>

Password.

##### default_pacer_client_code: `Optional[str]`<a id="default_pacer_client_code-optionalstr"></a>

Pacer Client Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PacerCredentialRequest`](./unicourt_python_sdk/type/pacer_credential_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Success`](./unicourt_python_sdk/pydantic/success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCredential` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.pacer_credential_api.remove_for_user_id`<a id="unicourtpacer_credential_apiremove_for_user_id"></a>

De-register the PACER credentials for the specified PACER username.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_for_user_id_response = unicourt.pacer_credential_api.remove_for_user_id(
    pacer_user_id="URKYwer3tyh5r56gq2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pacer_user_id: `str`<a id="pacer_user_id-str"></a>

The PACER username for which PACER credentials are to be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`Success`](./unicourt_python_sdk/pydantic/success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pacerCredential/{pacerUserId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.party_analytics_api.get_associated_norm_attorneys`<a id="unicourtparty_analytics_apiget_associated_norm_attorneys"></a>

Returns a list of  Attorneys the Party has been represented by.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all attorneys associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_associated_norm_attorneys_response = unicourt.party_analytics_api.get_associated_norm_attorneys(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_party_id: `str`<a id="norm_party_id-str"></a>

Norm ID of the Party.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormAttorneyResponse`](./unicourt_python_sdk/pydantic/associated_norm_attorney_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normParty/{normPartyId}/associatedNormAttorneys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.party_analytics_api.get_norm_party_details`<a id="unicourtparty_analytics_apiget_norm_party_details"></a>

The Party Details API allows you to look up Parties by normPartyId.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_party_details_response = unicourt.party_analytics_api.get_norm_party_details(
    norm_party_id="NORGrPmQyLdx9NGHcT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_party_id: `str`<a id="norm_party_id-str"></a>

Norm ID of the Party.   - minimum: 18   - maximum: 18 

#### 🔄 Return<a id="🔄-return"></a>

[`NormParty`](./unicourt_python_sdk/pydantic/norm_party.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normParty/{normPartyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.party_analytics_api.get_norm_party_search_results_by_id`<a id="unicourtparty_analytics_apiget_norm_party_search_results_by_id"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normpartysearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_norm_party_search_results_by_id_response = unicourt.party_analytics_api.get_norm_party_search_results_by_id(
    norm_party_search_id="PSRCUoacNCGj9ezvqf",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_party_search_id: `str`<a id="norm_party_search_id-str"></a>

Norm Party Search information for the given normPartySearchId.

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormPartySearchResponse`](./unicourt_python_sdk/pydantic/norm_party_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normPartySearch/{normPartySearchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.party_analytics_api.list_associated_norm_law_firms`<a id="unicourtparty_analytics_apilist_associated_norm_law_firms"></a>

Returns a list of Law Firms the Party has been represented by.
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all lawfirms associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_associated_norm_law_firms_response = unicourt.party_analytics_api.list_associated_norm_law_firms(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_party_id: `str`<a id="norm_party_id-str"></a>

Norm ID of the Party.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormLawFirmResponse`](./unicourt_python_sdk/pydantic/associated_norm_law_firm_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normParty/{normPartyId}/associatedNormLawFirms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.party_analytics_api.list_judges_associated_with_norm_party`<a id="unicourtparty_analytics_apilist_judges_associated_with_norm_party"></a>

Returns a list of Judges the party has faced.
<br><br>
## Terms and Connectors<a id="terms-and-connectors"></a>
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query<a id="example-query"></a>
Query to get all judges associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_judges_associated_with_norm_party_response = unicourt.party_analytics_api.list_judges_associated_with_norm_party(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
    q="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### norm_party_id: `str`<a id="norm_party_id-str"></a>

Norm ID of the Party.   - minimum: 18   - maximum: 18 

##### page_number: `int`<a id="page_number-int"></a>

Page number. - minimum: 1 

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

#### 🔄 Return<a id="🔄-return"></a>

[`AssociatedNormJudgeResponse`](./unicourt_python_sdk/pydantic/associated_norm_judge_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normParty/{normPartyId}/associatedNormJudges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.party_analytics_api.search_norm_parties`<a id="unicourtparty_analytics_apisearch_norm_parties"></a>

### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject<a id="all-query-parameters-supported-for-this-api-can-be-found-in-below-schema-section-schema----normpartysearchqueryobject"></a>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_norm_parties_response = unicourt.party_analytics_api.search_norm_parties(
    q="normPartyId:\"NORGJWPpNLekV7dKTm\"",
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters.</a> 

##### page_number: `int`<a id="page_number-int"></a>

Query parameter specifying the page number of the search results to be retrieved. - Minimum: 1 - Maximum: 1000 

#### 🔄 Return<a id="🔄-return"></a>

[`NormPartySearchResponse`](./unicourt_python_sdk/pydantic/norm_party_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/normPartySearch` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.usage_api.get_api_usage_by_billing_cycle`<a id="unicourtusage_apiget_api_usage_by_billing_cycle"></a>

An endpoint to obtain information on API usage for a specific billing cycle.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_api_usage_by_billing_cycle_response = unicourt.usage_api.get_api_usage_by_billing_cycle(
    billing_cycle="2023-01-25to2023-02-25",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### billing_cycle: `str`<a id="billing_cycle-str"></a>

The date obtainable from the /billingCycles endpoint which is used as an identifier for the specific billing cycle you wish to obtain information on.

#### 🔄 Return<a id="🔄-return"></a>

[`BillingCycleUsageResponse`](./unicourt_python_sdk/pydantic/billing_cycle_usage_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billingCycleUsage/{billingCycle}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.usage_api.get_api_usage_by_date`<a id="unicourtusage_apiget_api_usage_by_date"></a>

An endpoint to obtain information on API usage for a specific day.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_api_usage_by_date_response = unicourt.usage_api.get_api_usage_by_date(
    date="2023-02-21T00:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `date`<a id="date-date"></a>

The specific date for which you wish to obtain information on API usage.

#### 🔄 Return<a id="🔄-return"></a>

[`DailyUsageResponse`](./unicourt_python_sdk/pydantic/daily_usage_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dailyUsage/{date}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `unicourt.usage_api.list_previous_billing_cycles`<a id="unicourtusage_apilist_previous_billing_cycles"></a>

An endpoint to obtain information on the previous 12 billing cycles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_previous_billing_cycles_response = unicourt.usage_api.list_previous_billing_cycles()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BillingCyclesResponse`](./unicourt_python_sdk/pydantic/billing_cycles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billingCycles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
