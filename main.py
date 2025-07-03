import requests

API_KEY = "BURAYA_KENDİ_API_KEY'İNİ_YAZ"
city = input("Şehir ismi girin: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\nŞehir: {data['name']}")
    print(f"Sıcaklık: {data['main']['temp']}°C")
    print(f"Durum: {data['weather'][0]['description']}")
    print(f"Nem: {data['main']['humidity']}%")
else:
    print("Şehir bulunamadı ya da API anahtarınız geçersiz.")
