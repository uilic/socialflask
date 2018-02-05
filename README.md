# TWENTY FRIENDS APP

## Author

Uros Ilic

### contact:
uros92vozd@gmail.com

### About app

This is a lightweight application called Twenty People Developed in Flask. It provides functionality to choose a person within the group stored in the database and display the following information about this person:

- Direct friends: those people who are directly connected to the chosen user.
- Friends of friends: those who are two steps away from the chosen user but not directly connected to the chosen user.
- Suggested friends: people in the group who know 2 or more direct friends of the chosen user but are not directly connected to the chosen user.

Instead of using any kind of the database concept, because of the small amount of data, I imported the data directly from .json file. In case there would be some kind of a large data set, I would use some database.


### Run

To start the application, you should have Python installed on your machine and type the following in your terminal.:

```
$ git clone https://github.com/uilic/socialflask.git

$ cd socialflask

$ virtualenv venv

$ . venv/bin/activate
```
If you are a Windows user, the last command should be:

```
$ venv\Scripts\activate
```
Then you should install flask:

```
$ pip install Flask
```
And run the app:

```
$ python app.py 
```
If everything went right you should see the app in your browser on the page  http://127.0.0.1:5000/


Home page
![screenshot from 2018-02-05 16-42-08](https://user-images.githubusercontent.com/32105551/35813382-c1da8cf4-0a93-11e8-8774-13481fd0be28.png)
People group page
![screenshot from 2018-02-05 16-42-22](https://user-images.githubusercontent.com/32105551/35813389-c894e65c-0a93-11e8-9510-004bc358a22a.png)
Profile page
![screenshot from 2018-02-05 16-42-57](https://user-images.githubusercontent.com/32105551/35813393-cd0b181e-0a93-11e8-9d27-c4470a4924a5.png)


