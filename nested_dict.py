d = {}

keyList1 = ["Person", "Male", "Boy", "Student", "id_123", "Name"]
keyList2 = ["Person", "Male", "Boy", "Student", "id_123", "Age"]
value1 = "Roger"
value2 = 3

def insert(cur, list, value):
    if len(list) == 1:
        cur[list[0]] = value
        return
    if list[0] not in cur:
        cur[list[0]] = {}
    print(list[1:])
    insert(cur[list[0]], list[1:], value)

insert(d, keyList1, value1)
insert(d, keyList2, value2)

print(d


'''{'Person': {'Male': {'Boy': {'Student': {'id_123': {'Age': 3, 'Name': 'Roger'}}}}}}'''