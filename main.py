import json

with open('json_example_QAP.json', encoding='utf8') as f:
    templates = json.load(f)

def CheckInt(item):
    return isinstance(item, int)

def CheckStr(item):
    return isinstance(item, str)

def CheckBool(item):
    return isinstance(item, bool)

def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False

def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def ErrorLog(item, value, string):
    Error.append({item: f'{value}. {string}'})

listofItems = {'timestamp': 'int', \
               'item_price': 'int', \
               'referer': 'url', \
               'location': 'url', \
               'item_url': 'url', \
               'remoteHost': 'str', \
               'partyId': 'str', \
               'sessionId': 'str', \
               'pageViewId': 'str', \
               'item_id': 'str', \
               'basket_price': 'str', \
               'userAgentName': 'str', \
               'eventType': 'val', \
               'detectedDuplicate': 'bool', \
               'detectedCorruption': 'bool', \
               'firstInSession': 'bool'}

Error = []
for items in templates:
    for item in items:
        if item in listofItems:
            if listofItems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofItems[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofItems[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofItems[item] == 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], 'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожидали значение')
        else:
            ErrorLog(item, items[item], 'неожидали значение')

if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)
