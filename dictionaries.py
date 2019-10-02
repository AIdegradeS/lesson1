spisok = {'city': 'Москва', 'temperature': 20}
print(spisok["city"])
spisok["temperature"] = spisok["temperature"] - 5
print(spisok)
spisok.get("country")
spisok.get("country", "Россия")
spisok['date'] = '27.05.2019'
print(len(spisok))