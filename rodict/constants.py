from rodict.parsers import json_parser

SUPPORTED_FILE_FORMATS = ["json"]

PARSER_FROM_EXTENSION = {
    "json": json_parser,
}