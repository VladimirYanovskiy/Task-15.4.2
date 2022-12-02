# Task-15.4.2
Задание 15.4.2

Задание на автоматизацию проверки ответа API от сервера.

У вас есть следующие требования к ответу:

timestamp: int
referer: string (url)
location: string (url)
remoteHost: string
partyId: string
sessionId: string
pageViewId: string
eventType: string (itemBuyEvent или itemViewEvent)
item_id: string
item_price: int
item_url: string (url)
basket_price: string
detectedDuplicate: bool
detectedCorruption: bool
firstInSession: bool
userAgentName: string

Вот здесь https://github.com/SkillfactoryCoding/QAP/blob/master/json_example_QAP.json можно взять пример JSON с ответами некоего интернет-магазина, составленный по этим правилам.

Вам нужно написать простой тест, который проверяет JSON на правильность полей. То есть проверяет, что каждый объект в JSON:

Содержит все перечисленные в требованиях поля.
Не имеет других полей.
Все поля имеют именно тот тип, который указан в требованиях:
int — целое число;
string — произвольная строка;
string (url) — это строка с url. В рамках этого задания проверяем, что url начинается c http:\\ или https:\\;
string (itemBuyEvent или itemViewEvent) — строка, в которой могут быть только эти конкретные два значения и никакие другие;
bool — булево значение, то есть True или False.

Тест должен вернуть Pass или список значений, которые тест посчитал ошибочными, и причину, почему они ошибочные.
