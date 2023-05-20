import datetime
import json
import os


def save_to_json(recipes):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    datasets_directory = os.path.join(current_directory, '../datasets')
    os.makedirs(datasets_directory, exist_ok=True)

    filename = f"{datasets_directory}/recipes_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(filename, 'w') as json_file:
        json.dump(recipes, json_file, indent=4)
    print(f"Result saved to {filename}")
