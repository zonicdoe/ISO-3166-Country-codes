# **ISO-3166 Country Codes JSON**

The purpose of ISO 3166 is to define internationally recognized codes of letters and/or numbers that we can use when we refer to countries and their subdivisions.

This repository contains several JSON files formatted in different ways to suit different kind of needs.
For basic Country to Alpha-2 or Alpha-3 translation and vise-versa, use one of the [short JSON files](#short).

## **Table of contents:**
* [File summary](#files)
* [Original JSON:](#original) full JSON data fetched from the [ISO.org Vaadin webapp](https://www.iso.org/obp/ui/#search/code/)
* [Curated JSON:](#curated) empty and useless data removed
  + [Not indexed](#curated-not-indexed)
  + [Indexed by Alpha-2 country code](#curated-alpha2)
  + [Indexed by numeric country code](#curated-num)
  + [Indexed by country name](#curated-name)
* [Short JSON:](#short) with only the basic required data
  + [Not indexed](#short-not-indexed)
  + [Indexed by Alpha-2 country code](#short-alpha2)
  + [Indexed by numeric country code](#short-num)
  + [Indexed by country name](#short-name)
* [Changelog](#changelog)
* [What does "extractor.py" do?](#extractor-description)

## <a name="files"></a>**File summary**
--------------------------------------------

<table>
    <tr>
        <td colspan="2"></td>
        <th>Indented JSON<br>(human readable files)</th>
        <th>Single line JSON<br>(compact files)</th>
    </tr>
    <tr>
        <td><b><a href=#original>Original data</a></b><br>(Original JSON data<br>fetched from ISO.org)</th>
        <td><b>Not indexed</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-ISO.ORG.json>ISO-3166-ID-ISO.ORG.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-ISO.ORG.json>ISO-3166-SL-ISO.ORG.json</a></td>
    </tr>
    <tr>
        <td rowspan="4"><b><a href=#curated>Curated data</a></b><br>(with empty and<br>useless data removed)</td>
        <td><b>Not indexed</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-CURATED.json>ISO-3166-ID-CURATED.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-CURATED.json>ISO-3166-SL-CURATED.json</a></td>
    </tr>
    <tr>
        <td><b>Indexed by Alpha-2 country code</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-CURATED-ALPHA2.json>ISO-3166-ID-CURATED-ALPHA2.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-CURATED-ALPHA2.json>ISO-3166-SL-CURATED-ALPHA2.json</a></td>
    </tr>
    <tr>
        <td><b>Indexed by numeric country code</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-CURATED-NUM.json>ISO-3166-ID-CURATED-NUM.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-CURATED-NUM.json>ISO-3166-SL-CURATED-NUM.json</a></td>
    </tr>
    <tr>
        <td><b>Indexed by country name</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-CURATED-NAME.json>ISO-3166-ID-CURATED-NAME.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-CURATED-NAME.json>ISO-3166-SL-CURATED-NAME.json</a></td>
    </tr>
    <tr>
        <td rowspan="4"><b><a href=#short>Short data</a></b><br>(with only the basic<br>required data)</td>
        <td><b>Not indexed</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-SHORT.json>ISO-3166-ID-SHORT.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-SHORT.json>ISO-3166-SL-SHORT.json</a></td>
    </tr>
    <tr>
        <td><b>Indexed by Alpha-2 country code</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-SHORT-ALPHA2.json>ISO-3166-ID-SHORT-ALPHA2.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-SHORT-ALPHA2.json>ISO-3166-SL-SHORT-ALPHA2.json</a></td>
    </tr>
    <tr>
        <td><b>Indexed by numeric country code</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-SHORT-NUM.json>ISO-3166-ID-SHORT-NUM.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-SHORT-NUM.json>ISO-3166-SL-SHORT-NUM.json</a></td>
    </tr>
    <tr>
        <td><b>Indexed by country name</b></td>
        <td><a href=Indented-lists/ISO-3166-ID-SHORT-NAME.json>ISO-3166-ID-SHORT-NAME.json</a></td>
        <td><a href=Single-line-lists/ISO-3166-SL-SHORT-NAME.json>ISO-3166-SL-SHORT-NAME.json</a></td>
    </tr>
</table>

## <a name="original"></a>**Original JSON**
--------------------------------------------

### [Indented, human readable JSON file  »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-ISO.ORG.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-ISO.ORG.json)

|Key | description |
|---|---|
|"149" | Uknown purpose value (always empty) |
|"151" | Uknown purpose value (always empty)|
|"153" | Entry type (always "country") |
|"155" | Alpha-2 country code |
|"157" | Uknown purpose boolean (always false) |
|"159" | Country name |
|"161" | Redundat Alpha-2 code, already present ("155" key) |
|"163" | Description label |
|"165" | Uknown purpose value (always empty) |
|"167" | XML file path |
|"169" | Country name localization [ENGLISH, FRENCH, NATIVE] |
|"171" | French short name |
|"173" | Numeric country code |
|"175" | HTML anchor (extra info). Ex. https://www.iso.org/obp/ui/#iso:code:3166:US |
|"177" | Alpha-3 country code |
|"179" | Entry status remarks (optional) |
|"181" | Remarks in french (optional) |
|"183" | Uknown purpose value (always empty) |
|"185" | Entry remarks (optional) |
|"187" | Entry status |

**Structure sample:**
```
[
    ...,
    {
        "149": "",
        "151": "",
        "153": "country",
        "155": "SX",
        "157": "false",
        "159": "Sint Maarten (Dutch part)",
        "161": "SX",
        "163": "[Country code: SX]",
        "165": "",
        "167": "/content/iso/code/3166/SX_69.xml",
        "169": "[Sint Maarten (Dutch part), Saint-Martin (partie néerlandaise), Sint Maarten]",
        "171": "Saint-Martin (partie néerlandaise)",
        "173": "534",
        "175": "iso:code:3166:SX",
        "177": "SXM",
        "179": "The island of Saint Martin is divided into the French northern part and the Dutch southern part",
        "181": " Les Antilles néerlandaises (AN, ANT, 530) ont été divisées entre  Bonaire, Saint-Eustache et Saba (BQ, BES, 535), Curaçao (CW, CUW, 531) et Saint-Martin (partie néerlandaise) (SX, SXM, 534). Voir aussi codet ANHH.",
        "183": "",
        "185": "The Netherlands Antilles (AN, ANT, 530) was divided into Bonaire, Saint Eustatius and Saba (BQ, BES, 535), Curaçao (CW, CUW, 531) and Sint Maarten (Dutch part) (SX, SXM, 534). See also code element ANHH.",
        "187": "Officially assigned"
    },
    ...
]
```

Ex. get the country name of the 5th country (index 4) of the list:\
`JSON[0][4]["159"]`

## <a name="curated"></a>**Curated JSON**
-----------------------------------------

|Key | description |
|---|---|
|"alpha2" | Alpha-2 country code |
|"alpha3" | Alpha-3 country code |
|"name" | Country name |
|"l10n" | Country name localization [ENGLISH, FRENCH, NATIVE] |
|"num" | Numeric country code |
|"r" | Entry remarks (optional) |
|"s" | Entry status |
|"sr" | Entry status remarks (optional) |

### <a name="curated-not-indexed"></a>**Not indexed**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-CURATED.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-CURATED.json)

Structure sample:
```
[
    ...,
    {
        "alpha2": "SX",
        "alpha3": "SXM",
        "name": "Sint Maarten (Dutch part)",
        "l10n": "[Sint Maarten (Dutch part), Saint-Martin (partie néerlandaise), Sint Maarten]",
        "num": "534",
        "r": "The Netherlands Antilles (AN, ANT, 530) was divided into Bonaire, Saint Eustatius and Saba (BQ, BES, 535), Curaçao (CW, CUW, 531) and Sint Maarten (Dutch part) (SX, SXM, 534). See also code element ANHH.",
        "s": "Officially assigned",
        "sr": "The island of Saint Martin is divided into the French northern part and the Dutch southern part"
    },
    ...
]
```

Ex. get the country name of the 5th country (index 4) of the list:\
`JSON[0][4]["name"]`

### <a name="curated-alpha2"></a>**Indexed by Alpha-2 country code**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-CURATED-ALPHA2.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-CURATED-ALPHA2.json)

Structure sample:
```
{
    ...,
    "SX": {
        "alpha3": "SXM",
        "name": "Sint Maarten (Dutch part)",
        "l10n": "[Sint Maarten (Dutch part), Saint-Martin (partie néerlandaise), Sint Maarten]",
        "num": "534",
        "r": "The Netherlands Antilles (AN, ANT, 530) was divided into Bonaire, Saint Eustatius and Saba (BQ, BES, 535), Curaçao (CW, CUW, 531) and Sint Maarten (Dutch part) (SX, SXM, 534). See also code element ANHH.",
        "s": "Officially assigned",
        "sr": "The island of Saint Martin is divided into the French northern part and the Dutch southern part"
    },
    ...
}
```

Ex. get the country name corresponding to the Alpha-2 country code "US":\
`JSON["US"]["name"]`

### <a name="curated-num"></a>**Indexed by numeric country code**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-CURATED-NUM.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-CURATED-NUM.json)

Structure sample:
```
{
    ...,
    "534": {
        "alpha2": "SX",
        "alpha3": "SXM",
        "name": "Sint Maarten (Dutch part)",
        "l10n": "[Sint Maarten (Dutch part), Saint-Martin (partie néerlandaise), Sint Maarten]",
        "r": "The Netherlands Antilles (AN, ANT, 530) was divided into Bonaire, Saint Eustatius and Saba (BQ, BES, 535), Curaçao (CW, CUW, 531) and Sint Maarten (Dutch part) (SX, SXM, 534). See also code element ANHH.",
        "s": "Officially assigned",
        "sr": "The island of Saint Martin is divided into the French northern part and the Dutch southern part"
    },
    ...
}
```

Ex. get the country name corresponding to the numeric country code "840":\
`JSON["840"]["name"]`

### <a name="curated-name"></a>**Indexed by country name**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-CURATED-NAME.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-CURATED-NAME.json)

Structure sample:
```
{
    ...,
    "Sint Maarten (Dutch part)": {
        "alpha2": "SX",
        "alpha3": "SXM",
        "l10n": "[Sint Maarten (Dutch part), Saint-Martin (partie néerlandaise), Sint Maarten]",
        "num": "534",
        "r": "The Netherlands Antilles (AN, ANT, 530) was divided into Bonaire, Saint Eustatius and Saba (BQ, BES, 535), Curaçao (CW, CUW, 531) and Sint Maarten (Dutch part) (SX, SXM, 534). See also code element ANHH.",
        "s": "Officially assigned",
        "sr": "The island of Saint Martin is divided into the French northern part and the Dutch southern part"
    },
    ...
}
```

Ex. get the Alpha-2 country code of the United States of America:\
`JSON["United States of America (the)"]["alpha2"]`

## <a name="short"></a>**Short JSON**
---

|Key | description |
|---|---|
|"alpha2" | Alpha-2 country code |
|"alpha3" | Alpha-3 country code |
|"name" | Country name |
|"num" | Numeric country code |

### <a name="short-not-indexed"></a>**Not indexed**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-SHORT.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-SHORT.json)

Structure sample:
```
[
    ...,
    {
        "alpha2": "US",
        "alpha3": "USA",
        "name": "United States of America (the)",
        "num": "840"
    },
    ...
]
```

Ex. get the country name of the 5th country (index 4) of the list:\
`JSON[0][4]["name"]`

### <a name="short-alpha2"></a>**Indexed by Alpha-2 country code**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-SHORT-ALPHA2.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-SHORT-ALPHA2.json)

Structure sample:
```
{
    ...,
    "US": {
        "alpha3": "USA",
        "name": "United States of America (the)",
        "num": "840"
    },
    ...
}
```

Ex. get the country name corresponding to the Alpha-2 country code "US":\
`JSON["US"]["name"]`

### <a name="short-num"></a>**Indexed by numeric country code**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-SHORT-NUM.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-SHORT-NUM.json)

Structure sample:
```
{
    ...,
    "840": {
        "alpha2": "US",
        "alpha3": "USA",
        "name": "United States of America (the)"
    },
    ...
}
```

Ex. get the country name corresponding to the country numeric code "840":\
`JSON["840"]["name"]`

### <a name="short-name"></a>**Indexed by country name**

#### [Indented, human readable JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Indented-lists/ISO-3166-ID-SHORT-NAME.json) &nbsp;**|**&nbsp; [Single line, compact JSON file »](https://github.com/zonicdoe/ISO-3166-Country-codes/Single-line-lists/ISO-3166-SL-SHORT-NAME.json)

Structure sample:
```
{
    ...,
    "United States of America (the)": {
        "alpha2": "US",
        "alpha3": "USA",
        "num": "840"
    },
    ...
}
```

Ex. get the Alpha-2 country code of the United States of America:\
`JSON["United States of America (the)"]["alpha2"]`

## **Changelog**
----------------
* version 1.0.0 - 09/30/2020: Initial commit

## <a name="extractor-description"></a>**What does "extractor.py" do?**
-----------------------------------------------------------------------
It is a Pyhton script that requests JSON data from the ISO.org's Vaadin webapp server and generates all the JSON files contained in this repository.

To update the JSON files, execute the script with:\
`$ python extractor.py`

First, it requests a new [anti-CSRF token](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) (anti-cross site request forgery token) and the app version number from:\
`https://www.iso.org/obp/ui/?v-1601327571800`

Sample HTTP request:
```
POST /obp/ui/?v-1601327571800 HTTP/1.1
Host: www.iso.org
User-Agent: python-requests/2.24.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Accept-Language: en-US,en;q=0.3
Content-type: application/x-www-form-urlencoded
Content-Length: 283

v-browserDetails=1&theme=iso-red&v-appId=obpui-105541713&v-sh=933&v-sw=1920&v-cw=1920&v-ch=933&v-curdate=1601327571800&v-tzo=0&v-dstd=0&v-rtzo=0&v-dston=false&v-tzid=UTC&v-vw=1920&v-vh=933&v-loc=https%3A%2F%2Fwww.iso.org%2Fobp%2Fui%2F%23search&v-wn=obpui-105541713-0.9915450455033209
```

Sample HTTP response:
```
HTTP/1.1 200 
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Application-Context: obp:prod,iso,prod_iso:8080
Set-Cookie: JSESSIONID=01654CBE2DF8724FA2EA4899E4245F8A;path=/obp;HttpOnly
Content-Type: application/json;charset=UTF-8
Content-Length: 27273
Date: Wed, 30 Sep 2020 20:54:04 GMT
Connection: close
Set-Cookie: BIGipServerpool_prod_iso_obp=914903434.36895.0000; path=/; Httponly; Secure;SameSite=none
Strict-Transport-Security: max-age=31536000; includeSubDomains

{"v-uiId":0,"uidl":"<JSON_DATA>"}
```

from where "v-uiId" is the version number and "uidl" is a JSON string containing a key called "Vaadin-Security-Key", which in turn contains the anti-CSRF token.

With this data, the script then can directly interact with the Vaddin webapp endpoint:\
`https://www.iso.org/obp/ui/UIDL/`\
sending a URL parameter "v-uiId=" with value of the previously described version number.\
Endpoint example:\
`https://www.iso.org/obp/ui/UIDL/?v-uiId=0`

The script then sends commands to this endpoint via JSON messages with the following structure:

```
{
  "csrfToken": "<CSRF_TOKEN>",
  "rpc": [
    [
      "<FIXED_ELEMENT_ID>",
      "<VAADIN_MODULE>",
      "<ACTION>",
      [
        <PARAM_LIST>
      ]
    ]
  ],
  "syncId": <AUTOINCREMENT_INT>,
  "clientId": <AUTOINCREMENT_INT>
}
```


CSRF_TOKEN is always the same, and it's the anti-CSRF token previously described.\
AUTOINCREMENT_INT is a number that increases with every request sent to the server, starting from 0.

Sample HTTP request:

```
POST /obp/ui/UIDL/?v-uiId=0 HTTP/1.1
Host: www.iso.org
User-Agent: python-requests/2.24.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Accept-Language: en-US,en;q=0.3
Content-Type: application/json; charset=UTF-8
Cookie: JSESSIONID=01654CBE2DF8724FA2EA4899E4245F8A; BIGipServerpool_prod_iso_obp=914903434.36895.0000
Content-Length: 158

{"csrfToken":"9abe196a-7d72-4c34-8dd0-f525045fe2ab","rpc":[["146","com.vaadin.shared.data.DataRequestRpc","requestRows",[0,400,0,0]]],"syncId":3,"clientId":3}
```

There are 4 steps required (HTTP requests than need to be sent, in order) to fetch all the country codes from the server.

1. **Select data set (7 for country codes)**\
FIXED_ELEMENT_ID = 19\
VAADIN_MODULE = com.vaadin.shared.data.selection.SelectionServerRpc\
ACTION = select\
PARAM_LIST = "7"\
AUTOINCREMENT_INT = 0
2. **Trigger view change (fake click)**\
FIXED_ELEMENT_ID = 26\
VAADIN_MODULE = com.vaadin.shared.ui.button.ButtonServerRpc\
ACTION = click\
PARAM_LIST = {"altKey":false,"button":"LEFT","clientX":1292,"clientY":438,"ctrlKey":false,"metaKey":false,"relativeX":36,"relativeY":21,"shiftKey":false,"type":1}\
AUTOINCREMENT_INT = 1
3. **Select pagination (8 for 300 results per page)**\
FIXED_ELEMENT_ID = 56\
VAADIN_MODULE = com.vaadin.shared.data.selection.SelectionServerRpc\
ACTION = select\
PARAM_LIST = "8"\
AUTOINCREMENT_INT = 2
4. **Request data**\
FIXED_ELEMENT_ID = 146\
VAADIN_MODULE = com.vaadin.shared.data.DataRequestRpc\
ACTION = requestRows\
PARAM_LIST = 0,300,0,0\
AUTOINCREMENT_INT = 3

The response for the 4th request has the following structure:
```
for(;;);[
  {
    "syncId": <AUTOINCREMENT_INT>,
    "clientId": <AUTOINCREMENT_INT>,
    "changes": [],
    "state": {},
    "types": {
      "146": "18"
    },
    "hierarchy": {
      "146": []
    },
    "rpc": [
      [
        "146",
        "com.vaadin.shared.data.DataCommunicatorClientRpc",
        "setData",
        [
          0,
          [
              ...,
              {
                "k": "261",
                "d": {
                  "149": "",
                  "151": "",
                  "153": "country",
                  "155": "US",
                  "157": "false",
                  "159": "United States of America (the)",
                  "161": "US",
                  "163": "[Country code: US]",
                  "165": "",
                  "167": "/content/iso/code/3166/US_69.xml",
                  "169": "[United States of America (the), États-Unis d'Amérique (les)]",
                  "171": "États-Unis d'Amérique (les)",
                  "173": "840",
                  "175": "iso:code:3166:US",
                  "177": "USA",
                  "179": "",
                  "181": "",
                  "183": "",
                  "185": "",
                  "187": "Officially assigned"
                },
                "cs": {
                  "159": "wrap",
                  "171": "wrap"
                }
              },
              ...
          ]
        ]
      ]
    ],
    "meta": {},
    "resources": {}
  }
]
```

The script gets rid of the 'for(;;);' part from the beginning and then parse the content as JSON.

After that, it follows the following path to retrieve each country information:\
`response[0]["rpc"][0][3][1][<INDEX>]["d"]`\
from where INDEX is a number of the range from 0 to X amount of fetched countries.\
0 corresponds to the first country of the list, 1 to the second, 2 to the third, so on and so forth.

Ex. get the Alpha-2 country code of the 5th country (INDEX = 4) of the list:\
`response[0]["rpc"][0][3][1][4]["d"]["155"]`