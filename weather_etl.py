import http.client

conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "f7f63e4fb7mshb13f97223b4fd53p13298ajsnf736fd0f8f77",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com"
}

conn.request("GET", "/city/london/EN", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

