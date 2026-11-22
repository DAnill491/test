Курсы валют
usd_rate = 90
eur_rate = 100

Спрашиваем сумму в рублях
rub = float(input("Введите сумму в рублях: "))

 Проверяем, что сумма больше нуля (Тест 3)
if rub <= 0:
    print("Ошибка: сумма должна быть больше нуля.")
else:
     Спрашиваем валюту
    currency = input("Введите валюту (USD или EUR): ")

     Считаем и выводим результат (Тесты 1, 2 и 4)
    if currency == "USD":
        result = rub / usd_rate
        print(f"{result:.2f} USD")
    elif currency == "EUR":
        result = rub / eur_rate
        print(f"{result:.2f} EUR")
    else:
        print("Ошибка: неподдерживаемая валюта.")
