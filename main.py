import httpx
import time
import argparse
import validators

# Необходимо разработать CLI-утилиту совершающую HTTP Healthcheck'и по заданному URL'у.
 
# Проверка совершается в цикле с заданным интервалом. На каждой итерации необходимо совершить HTTP GET по заданному URL'у.
# Есть три возможных результата проверки:
# 1. `OK(200)`, в случае, если запрос вернул HTTP status code `200`.
# 2. `ERR({HTTP_CODE})`, в случае, если запрос вернул HTTP status code отличный от `200`.
# 3. `URL parsing error`, в случае, если второй аргумент не является валидным HTTP URL'ом. После чего приложение завершается.

def verify_url(url : str) -> bool:
    if not validators.url(url):
        return False
    else:
        return True

parser = argparse.ArgumentParser()
parser.add_argument('--int', type=float, default=1000)
parser.add_argument('--url', type=str, required=True)

args = parser.parse_args()

while True:     
    if verify_url(args.url) == True:
        response = httpx.get(url=args.url)
        if response.status_code == 200:
            print(f"HTTP Status: {response.status_code}")
        else:
            print(f"Failure HTTP Status: {response.status_code}")
    else:
        print('URL parsing error')
        exit(1)
            
    
    time.sleep(args.int)