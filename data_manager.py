import requests

PRICES_ENDPOINT = "ENDPOINT OF API SHEETY FOR THE PRICES "
USERS_ENDPOINT = "ENDPOINT OF API SHEETY FOR USERS"


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)

    def get_customer_emails(self):
        customers_endpoint = USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
