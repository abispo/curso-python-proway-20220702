import requests

if __name__ == "__main__":
    r = requests.get(
        "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/master/data/brasileirao-2021.json"
    )

    content = r.json()

    print(content)