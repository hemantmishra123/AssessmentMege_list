list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    
    """
    First get the All id from the list that store as the key.
    And the whole objects as value for that key in hash_map.
    """
    hash_map = {}
    for data in list_1:
        if not data["id"] in hash_map:
            hash_map[data["id"]] = data

    #Then checking the data for the each id of the hash_map into the list2 for getting the other field data. 
    for data in list_2:
        if data["id"] in hash_map:
            temp_dict = hash_map[data["id"]]
            for key in data.keys():
                if not key in temp_dict:
                    temp_dict[key] = data[key]
            
            hash_map[data["id"]] = temp_dict
    
    output_data = []
    for key in hash_map.keys():
        output_data.append(hash_map[key])

    return output_data

list_3 = merge_lists(list_1, list_2)
print(list_3)