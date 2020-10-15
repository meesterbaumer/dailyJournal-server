MOODS = [
    {
      "id": 1,
      "label": "Overjoyed"
    },
    {
      "id": 2,
      "label": "Happy"
    },
    {
      "id": 3,
      "label": "Meh..."
    },
    {
      "id": 4,
      "label": "Sad"
    },
    {
      "id": 5,
      "label": "Miserable"
    }
]

def get_all_moods():
    return MOODS

def get_single_mood(id):
    requested_mood = None

    for mood in MOODS:
        if mood["id"] == id:
            requested_mood = mood
    return requested_mood