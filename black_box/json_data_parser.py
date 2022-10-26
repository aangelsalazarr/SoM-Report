import json

def read_json(filename: str) -> dict:

    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data

def normalize_json(data: dict) -> dict:
    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v

    return new_data

def generate_csv_data(data: dict) -> str:

    # defining csv cols in a list to maintain the order
    csv_cols = data.keys()

    # generate the first row of csv
    csv_data = ",".join(csv_cols) + "\n"

    # generare the single record present
    new_row = list()
    for col in csv_cols:
        new_row.append(str(data[col]))

    # concatenate the record with the col info in csv format
    csv_data += ",".join(new_row) + "\n"

    return csv_data

def write_to_file(data:str, filepath: str) -> bool:

    try:
        with open(filepath, "w+") as f:
            f.write(data)

    except:
        raise Exception(f"Saving data to {filepath} encountered an error")

def main():
    # read the json file as a python dictionary
    data = read_json(filename="article.json")

    # normalize the nested python dict
    new_data = normalize_json(data=data)

    # pretty print the new dict obj
    print("New dict:", new_data)

    # generate the desired csv data
    csv_data = generate_csv_data(data=new_data)

    # save the generated csv data to a csv file
    write_to_file(data=csv_data, filepath="bls_data.csv")

if __name__ == '__main__':
    main()

