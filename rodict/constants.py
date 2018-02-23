from rodict.parsers import JSONParser

SUPPORTED_FILE_FORMATS = ["json"]

PARSER_FROM_EXTENSION = {
    "json": JSONParser
}