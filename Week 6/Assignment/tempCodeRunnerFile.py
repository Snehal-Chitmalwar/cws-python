def merge_dictionaries(dict1, dict2):
    new_dict = dict1.copy()
    for k, v in dict2.items():
        new_dict[k] = v
    print(new_dict)


merge_dictionaries({"Rose": 23, "Jack": 67, "Michaela": 78}, {
                   "Rose": 90, "Jin": 89, "Jennifer": 60})
