INSTRUCTORS = [
    {
        "id": 1,
        "firstName": "Steve",
        "lastName": "Brownlee"
    },
    {
        "id": 2,
        "firstName": "Kristen",
        "lastName": "Norris"
    },
    {
        "id": 3,
        "firstName": "Spencer",
        "lastName": "Truett"
    }
]


def get_all_instructors():
    return INSTRUCTORS


def get_single_instructor(id):
    requested_instructor = None

    for instructor in INSTRUCTORS:
        if instructor["id"] == id:
            requested_instructor = instructor
    return requested_instructor
