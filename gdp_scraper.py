import requests
from bs4 import BeautifulSoup
amt_of_rounds = int(input("Enter the number of countries you want: "))

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

gdp_table = soup.find("table", class_="wikitable")
rows = gdp_table.find_all("tr")
count = 0
for row in rows:
    count += 1
    columns = row.find_all("td")
    if len(columns) > 1:
        country_col = columns[0]
        gdp_col = columns[1]

        country_link = country_col.find("a")
        if country_link:
            country_name = country_link.text.strip()
            gdp_text = gdp_col.text.strip() if gdp_col else "N/A"
            print(f"Country: {country_name} \n GDP in millions USD: {gdp_text}\n Position: {count}\n")
            if count == amt_of_rounds:
                break