# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from unicourt_python_sdk.paths.pacer_import_case_by_court_using_case_number import Api

from unicourt_python_sdk.paths import PathValues

path = PathValues.PACER_IMPORT_CASE_BY_COURT_USING_CASE_NUMBER