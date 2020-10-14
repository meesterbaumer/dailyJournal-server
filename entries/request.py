ENTRIES = [
    {
        "date": "2020-08-04",
        "concept": "css",
        "entry": "ttttttttttttttt",
        "moodId": 1,
        "instructorId": 1,
        "id": 1
    },
    {
        "date": "2020-08-07",
        "concept": "Python",
        "entry": "test entry 2",
        "moodId": 3,
        "instructorId": 1,
        "id": 2
    },
    {
        "date": "2020-10-04",
        "concept": "javascript",
        "entry": "Test entry 3",
        "moodId": 2,
        "instructorId": 2,
        "id": 3
    }
]


def get_all_entries():
    return ENTRIES


def get_single_entry(id):
    requested_entry = None

    for entry in ENTRIES:
        if entry["id"] == id:
            requested_entry = entry
    return requested_entry
