def string_or_default(primary_value, secondary_value):
    retVal = primary_value
    if retVal is None or retVal.strip() == '':
        retVal = secondary_value
    return retVal
    # return secondary_value if (primary_value is None or primary_value.strip()) == '' else primary_value

def is_null_or_whitespace(val):
    return val is None or val.strip() == ''

def is_null_or_empty(val):
    return val is None or val == ''

def str_ignorecase_equals(str1, str2):
    return str1.upper() == str2.upper()

def str_ignorecase_index(str1, str2):
    return str1.upper().index(str2.upper())
