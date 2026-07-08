import requests

API = "https://reimagined-system.onrender.com/generate-pair?number="


def generate_pair(phone):
    url = API + phone
    response = requests.get(url, timeout=60)
    return response.text


def main():
    phone = input("Enter your WhatsApp number with country code: ")

    print("Generating pairing code...")

    code = generate_pair(phone)

    print("Pairing code:")
    print(code)


if __name__ == "__main__":
    main()
