import sys
import requests

url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("ошибка timeout, url:", url)
except requests.HTPPError as err:
    code = err.response.status_code
    print("ошибка url: {0}, code: {1}". format(url, code))
except requests.RequestException:
    print("ошибка скачивания url:", url)
else:
    print(response.content)
