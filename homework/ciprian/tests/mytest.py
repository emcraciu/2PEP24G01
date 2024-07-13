import json
import requests

def data_getter(url: str = r"http://127.0.0.1:5000//"):
    result = []
    response = requests.get(url,)
    text = response.text
    try:
        for obj in json.loads(text):
            result.append(obj)
    except Exception:
        return []
    return result


if __name__ == "__main__":
    print(data_getter("http://127.0.0.1:5000//"))
