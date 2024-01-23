import json

def load_email_data(data):
    try:
        with open(data, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f"The file {data} was not found.")
    except json.JSONDecodeError:
        raise Exception(f"The file {data} is not a valid JSON file.")


credentials = load_email_data("data/json/credentials.json")
email_details = load_email_data("data/json/email_details.json")