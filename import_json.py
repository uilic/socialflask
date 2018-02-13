import json
from people import Human


def loadGroup():
    """Importing .json file and returns list of human objec"""
    def getJSON(filePathName):
        with open(filePathName, 'r') as fp:
            return json.load(fp)

    peopleJson = getJSON('./data.json')

    people = []
    for peop in peopleJson:

        ident = peop.get("id")
        firstName = peop.get("firstName")
        surName = peop.get("surname")
        age = peop.get("age")
        gender = peop.get("gender")
        friends = peop.get("friends")

        h = Human(ident, firstName, surName, age, gender, friends)
        people.append(h)

    return people
