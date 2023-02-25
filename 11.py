def get_my_ip() -> str:
    import requests
    
    try:
        return requests.get("https://ipinfo.io/ip").text
    except requests.exceptions.ConnectionError:
        return requests.get("https://ifconfig.me/ip").text


print(get_my_ip())
