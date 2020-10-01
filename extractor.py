#!/bin/python3

# ISO.org scrapper.
# Extracts a full list of country codes as specified in the ISO-3166,
# fetching the data from the Vaadin webap server located at:
# https://www.iso.org/obp/ui/UIDL

import os
import requests
import json
from copy import deepcopy

MAX_COUNTRY_CODES = 300  # Max limit of countries to extract
INDENTED_OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'Indented-lists/ISO-3166-ID{}.json')
SINGLE_LINE_OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'Single-line-lists/ISO-3166-SL{}.json')


def getCSRFToken_Version(session):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-type': 'application/x-www-form-urlencoded',
        'Connection': 'close',
    }
    version = None

    data = 'v-browserDetails=1&theme=iso-red&v-appId=obpui-105541713&v-sh=933&v-sw=1920&v-cw=1920&v-ch=933&v-curdate=1601327571800&v-tzo=0&v-dstd=0&v-rtzo=0&v-dston=false&v-tzid=UTC&v-vw=1920&v-vh=933&v-loc=https%3A%2F%2Fwww.iso.org%2Fobp%2Fui%2F%23search&v-wn=obpui-105541713-0.9915450455033209'
    response = session.post('https://www.iso.org/obp/ui/?v-1601327571800', data=data, headers=headers)
    try:
        data = json.loads(response.text)
        version = data['v-uiId']
        data = json.loads(data['uidl'])
    except json.JSONDecodeError as e:
        print('Fatal error: ' + str(e))
        exit(-1)

    if 'Vaadin-Security-Key' in data:
        return data['Vaadin-Security-Key'], str(version)
    else:
        print('Fatal error: Unable to extract CSRF token from response.')
        exit(-1)


def parseCookies(cookies):
    cookieList = []
    for key in cookies:
        cookieList.append(key + '=' + cookies[key])

    return '; '.join(cookieList)


def renameOrDelete(list, oldKey, newKey):
    if len(list[oldKey]) > 0:
        list[newKey] = list[oldKey]
    del list[oldKey]


def mutateList(countryList, key):
    copy = deepcopy(countryList)
    mutated = {}

    for element in copy:
        mutated[element[key]] = element
        del mutated[element[key]][key]

    return mutated


def sendRequest(version, csrfToken, commandId, module, command, args, syncId, clientId):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json; charset=UTF-8',
        'Connection': 'close'
    }

    url = 'https://www.iso.org/obp/ui/UIDL/?v-uiId=' + version
    data = '{"csrfToken":"' + csrfToken + '","rpc":[["' + commandId + '","' + module + '","' + command + '",' + args + ']],"syncId":' + syncId + ',"clientId":' + clientId + '}'

    response = session.post(url, headers=headers, data=data)
    try:
        data = json.loads(response.text.replace('for(;;);', ''))
    except json.JSONDecodeError as e:
        print('Fatal error: ' + str(e))
        exit(-1)
    return str(data[0]['syncId']), str(data[0]['clientId']), data[0]['state'], data[0]['rpc']


def saveAsJSON(countryList, outputFile, indent=None):
    try:
        file = open(
            outputFile,
            "w",
            encoding='utf-8'
        )
        json.dump(countryList, file, ensure_ascii=False, indent=indent)
        file.close()
    except (PermissionError, TypeError) as e:
        print('X Fatal error: {}...\n'.format(str(e)))
        exit(-1)
    return


def JSONFromFile(inputFile):
    try:
        file = open(
            inputFile,
            "r",
            encoding='utf-8'
        )
        countries = json.load(file)
        file.close()
        return countries
    except PermissionError as e:
        print('X Fatal error: {}...\n'.format(str(e)))
        exit(-1)
    return


syncId = '0'
clientId = '0'
status = None
data = None
finalCountryList = []

print('Getting session data...')
# session.verify = False  # For request debugging
session = requests.Session()
csrfToken, version = getCSRFToken_Version(session)
cookie = parseCookies(session.cookies.get_dict())
print('CSRF token: ' + csrfToken)
print('Cookies: ' + cookie + '\n')

print('Selecting query type (7, country codes)')
syncId, clientId, status, data = sendRequest(
    version,
    csrfToken,
    '19',
    'com.vaadin.shared.data.selection.SelectionServerRpc',
    'select',
    '["7"]',
    syncId,
    clientId
)
print('New syncid: ' + syncId)
print('New clientId: ' + clientId)
print('Status: ', end='')
print(status)
print('Data: ', end='')
print(data)
print()

print('Forgerying Click action...')
syncId, clientId, status, data = sendRequest(
    version,
    csrfToken,
    '26',
    'com.vaadin.shared.ui.button.ButtonServerRpc',
    'click',
    '[{"altKey":false,"button":"LEFT","clientX":1292,"clientY":438,"ctrlKey":false,"metaKey":false,"relativeX":36,"relativeY":21,"shiftKey":false,"type":1}]',
    syncId,
    clientId
)
print('New syncid: ' + syncId)
print('New clientId: ' + clientId + '\n')

print('Changing pagination...')
syncId, clientId, status, data = sendRequest(
    version,
    csrfToken,
    '56',
    'com.vaadin.shared.data.selection.SelectionServerRpc',
    'select',
    '["8"]',
    syncId,
    clientId
)
print('New syncid: ' + syncId)
print('New clientId: ' + clientId)
print('Status: ', end='')
print(status)
print('Data: ', end='')
print(data)
print()

print('Querying country codes...')
syncId, clientId, status, data = sendRequest(
    version,
    csrfToken,
    '146',
    'com.vaadin.shared.data.DataRequestRpc',
    'requestRows',
    '[0,' + str(MAX_COUNTRY_CODES) + ',0,0]',
    syncId,
    clientId
)
print('New syncid: ' + syncId)
print('New clientId: ' + clientId + '\n')

print('Total countries fetched: ' + str(len(data[0][3][1])))

# ORIGINAL JSON GOTTEN FROM ISO.ORG ##############################################
##################################################################################
print('\nGenerating "original" country lists...')
for country in data[0][3][1]:
    finalCountryList.append(country['d'])

# Indented:
print('Saving as indented JSON ({})...'.format(INDENTED_OUTPUT_FILE.format('-ISO.ORG')))
saveAsJSON(finalCountryList, INDENTED_OUTPUT_FILE.format('-ISO.ORG'), 4)
# Single line:
print('Saving as single line JSON ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-ISO.ORG')))
saveAsJSON(finalCountryList, SINGLE_LINE_OUTPUT_FILE.format('-ISO.ORG'))


# CURATED LISTS ##################################################################
##################################################################################
print('\nGenerating "curated" country list...')
for country in finalCountryList:
    # Remove useless elements:
    del country['149']  # Empty value
    del country['151']  # Empty value
    del country['153']  # Entry type (country)
    del country['157']  # Uknown purpose boolean (always false)
    del country['161']  # Redundat Alpha-2 code, already present (contry['155'])
    del country['163']  # Description label
    del country['165']  # Empty value
    del country['167']  # XML file path
    del country['171']  # French short name
    del country['175']  # HTML anchor (extra info)
    del country['181']  # Remarks in french
    del country['183']  # Empty value
    # Rename keys:
    renameOrDelete(country, '155', 'alpha2')  # Alpha-2 code
    renameOrDelete(country, '177', 'alpha3')  # Alpha-3 code
    renameOrDelete(country, '159', 'name')  # Country name
    renameOrDelete(country, '169', 'l10n')  # Country name localization [ENGLISH, FRENCH, NATIVE]
    renameOrDelete(country, '173', 'num')  # Numeric code
    renameOrDelete(country, '185', 'r')  # Entry remarks (optional)
    renameOrDelete(country, '187', 's')  # Entry status
    renameOrDelete(country, '179', 'sr')  # Entry status remarks (optional)

# Array of countries, indented:
print('Saving as indented JSON ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED')))
saveAsJSON(finalCountryList, INDENTED_OUTPUT_FILE.format('-CURATED'), 4)
# Array of countries, single line:
print('Saving as single line JSON ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED')))
saveAsJSON(finalCountryList, SINGLE_LINE_OUTPUT_FILE.format('-CURATED'))
# Arranged by Alpha-2 code, indented:
mutatedList = mutateList(finalCountryList, 'alpha2')
print('Saving as indented JSON, arranged by Alpha-2 code. ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED-ALPHA2')))
saveAsJSON(mutatedList, INDENTED_OUTPUT_FILE.format('-CURATED-ALPHA2'), 4)
# Arranged by Alpha-2 code, single line:
print('Saving as single line JSON, arranged by Alpha-2 code. ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-ALPHA2')))
saveAsJSON(mutatedList, SINGLE_LINE_OUTPUT_FILE.format('-CURATED-ALPHA2'))
# Arranged by num code, indented:
mutatedList = mutateList(finalCountryList, 'num')
print('Saving as indented JSON, arranged by Num code. ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED-NUM')))
saveAsJSON(mutatedList, INDENTED_OUTPUT_FILE.format('-CURATED-NUM'), 4)
# Arranged by num code, single line:
print('Saving as single line JSON, arranged by Num code. ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NUM')))
saveAsJSON(mutatedList, SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NUM'))
# Arranged by name, indented:
mutatedList = mutateList(finalCountryList, 'name')
print('Saving as indented JSON, arranged by name. ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED-NAME')))
saveAsJSON(mutatedList, INDENTED_OUTPUT_FILE.format('-CURATED-NAME'), 4)
# Arranged by name, single line:
print('Saving as sinlge line JSON, arranged by name. ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NAME')))
saveAsJSON(mutatedList, SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NAME'))

# SHORT LISTS ####################################################################
##################################################################################
print('\nGenerating "short" country lists...')
for country in finalCountryList:
    # Remove none etential elements:
    del country['l10n']  # Country name localization [ENGLISH, FRENCH, NATIVE]
    if 'r' in country:
        del country['r']  # Entry remarks
    del country['s']  # Entry status
    if 'sr' in country:
        del country['sr']  # Entry status remarks

# Array of countries, indented:
print('Saving as indented JSON ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT')))
saveAsJSON(finalCountryList, INDENTED_OUTPUT_FILE.format('-SHORT'), 4)
# Array of countries, single line:
print('Saving as single line JSON ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT')))
saveAsJSON(finalCountryList, SINGLE_LINE_OUTPUT_FILE.format('-SHORT'))
# Arranged by Alpha-2 code, indented:
mutatedList = mutateList(finalCountryList, 'alpha2')
print('Saving as indented JSON, arranged by Alpha-2 code. ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT-ALPHA2')))
saveAsJSON(mutatedList, INDENTED_OUTPUT_FILE.format('-SHORT-ALPHA2'), 4)
# Arranged by Alpha-2 code, single line:
print('Saving as single line JSON, arranged by Alpha-2 code. ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-ALPHA2')))
saveAsJSON(mutatedList, SINGLE_LINE_OUTPUT_FILE.format('-SHORT-ALPHA2'))
# Arranged by num code, indented:
mutatedList = mutateList(finalCountryList, 'num')
print('Saving as indented JSON, arranged by Num code. ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT-NUM')))
saveAsJSON(mutatedList, INDENTED_OUTPUT_FILE.format('-SHORT-NUM'), 4)
# Arranged by num code, single line:
print('Saving as single line JSON, arranged by Num code. ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NUM')))
saveAsJSON(mutatedList, SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NUM'))
# Arranged by name, indented:
mutatedList = mutateList(finalCountryList, 'name')
print('Saving as indented JSON, arranged by name. ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT-NAME')))
saveAsJSON(mutatedList, INDENTED_OUTPUT_FILE.format('-SHORT-NAME'), 4)
# Arranged by name, single line:
print('Saving as sinlge line JSON, arranged by name. ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NAME')))
saveAsJSON(mutatedList, SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NAME'))


print('\nTESTING JSON FILES INTEGRITY...')

# INDENTED FILES #################################################################
##################################################################################
# Original list, indented file:
print('\n"Original" list, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-ISO.ORG')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-ISO.ORG'))
print(countries[100])
# Curated list, indented file:
print('\n"Curated" list, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-CURATED'))
print(countries[100])
# Short list, indented file:
print('\n"Short" list, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-SHORT'))
print(countries[100])
# Curated list, arranged by Alpha-2 code, indented file:
print('\n"Curated" list, arranged by Alpha-2 code, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED-ALPHA2')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-CURATED-ALPHA2'))
print(countries['US'])
# Short list, arranged by Alpha-2 code, indented file:
print('\n"Short" list, arranged by Alpha-2 code, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT-ALPHA2')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-SHORT-ALPHA2'))
print(countries['US'])
# Curated list, arranged by Num code, indented file:
print('\n"Curated" list, arranged by Num code, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED-NUM')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-CURATED-NUM'))
print(countries['840'])
# Short list, arranged by Num code, indented file:
print('\n"Short" list, arranged by Num code, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT-NUM')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-SHORT-NUM'))
print(countries['840'])
# Curated list, arranged by name, indented file:
print('\n"Curated" list, arranged by name, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-CURATED-NAME')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-CURATED-NAME'))
print(countries['United States of America (the)'])
# Short list, arranged by name, indented file:
print('\n"Short" list, arranged by name, indented ({})...'.format(INDENTED_OUTPUT_FILE.format('-SHORT-NAME')))
countries = JSONFromFile(INDENTED_OUTPUT_FILE.format('-SHORT-NAME'))
print(countries['United States of America (the)'])

# SINGLE LINE FILES ##############################################################
##################################################################################
# Original list, single line file:
print('\n"Original" list, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-ISO.ORG')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-ISO.ORG'))
print(countries[100])
# Curated list, single line file:
print('\n"Curated" list, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-CURATED'))
print(countries[100])
# Short list, single line file:
print('\n"Short" list, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-SHORT'))
print(countries[100])
# Curated list, arranged by Alpha-2 code, single line file:
print('\n"Curated" list, arranged by Alpha-2 code, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-ALPHA2')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-ALPHA2'))
print(countries['US'])
# Short list, arranged by Alpha-2 code, single line file:
print('\n"Short" list, arranged by Alpha-2 code, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-ALPHA2')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-ALPHA2'))
print(countries['US'])
# Curated list, arranged by Num code, single line file:
print('\n"Curated" list, arranged by Num code, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NUM')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NUM'))
print(countries['840'])
# Short list, arranged by Num code, single line file:
print('\n"Short" list, arranged by Num code, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NUM')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NUM'))
print(countries['840'])
# Curated list, arranged by name, single line| file:
print('\n"Curated" list, arranged by name, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NAME')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-CURATED-NAME'))
print(countries['United States of America (the)'])
# Short list, arranged by name, single line file:
print('\n"Short" list, arranged by name, single line ({})...'.format(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NAME')))
countries = JSONFromFile(SINGLE_LINE_OUTPUT_FILE.format('-SHORT-NAME'))
print(countries['United States of America (the)'])

print('\n\nPROCESS DONE.\n')
