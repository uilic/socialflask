#!/usr/bin/env python
from import_json import loadGroup
from flask import Flask, render_template
app = Flask(__name__)

people = loadGroup()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profiles/')
def profiles():
    return render_template('profiles.html', people=people)


@app.route('/profiles/<int:id>')
def account(id):
    friends = people[id].getFriends(people)
    frof = people[id].getFriendsOfFriends(people)
    sug = people[id].getSuggestedFriends(people)
    return render_template('profile.html', human=people[id], friends=friends, frof=frof, sug=sug)


if __name__ == '__main__':
    app.debug = True
    app.run()
