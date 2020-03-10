import json


def write_json_to_file(filename, jsondata):
    with open(filename, 'w') as f:
        json.dump(jsondata, f)


def retrieve_data_from_json(filename):
    with open(filename, 'r') as f:
        d = json.load(f)

    return d


def write_and_read():
    file_name = "some_file.json"

    d = {
        'foo': 'bar',
        'alice': 1,
        'wonderland': [1, 2, 3]
    }

    write_json_to_file(file_name, d)
    print(retrieve_data_from_json(file_name))


def read_and_handle():
    file_name = "learn.json"
    json_data = retrieve_data_from_json(file_name)
    print('-------- Without indent: ')
    print(json.dumps(json_data))
    print('\n-------- With indent=2: ')
    print(json.dumps(json_data, indent=2))
    print('\n-------- With indent=4: ')
    print(json.dumps(json_data, indent=4))
    print('\n-------- With indent and sorting: ')
    print(json.dumps(json_data, indent=2, sort_keys=True))


def check_type_of_elements():
    file_name = "learn.json"
    json_data = retrieve_data_from_json(file_name)
    cats = json_data['cats']
    print('-------- print type(json_data): ')
    print(type(json_data))
    print('\n-------- print cats: ')
    print(cats)
    print('\n-------- print cats[0]: ')
    print(cats[0])
    print('\n-------- print type(cats): ')
    print(type(cats))
    print('\n-------- print type(cats[0]): ')
    print(type(cats[0]))


def append_new_element():
    file_name = "learn.json"
    json_data = retrieve_data_from_json(file_name)
    cats = json_data['cats']

    new_cat = {
        'name': "New cat",
        'color': 'New color'
    }

    cats.append(new_cat)
    new_json = {'cats': cats}
    file_name = "new_learn.json"
    write_json_to_file(file_name, new_json)


def check_appended_element():
    file_name = "new_learn.json"
    json_data = retrieve_data_from_json(file_name)
    cats = json_data['cats']
    print(cats[2])


if __name__ == "__main__":
    # write_and_read()
    # read_and_handle()
    # check_type_of_elements()
    append_new_element()
    check_appended_element()
