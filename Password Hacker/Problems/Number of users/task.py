with open("users.json", "r") as jf:
    print(len(json.load(jf)["users"]))
