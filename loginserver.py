'''

In this login server  I will be adding the options to login in as an user and access to next pages: 
index and profile .
Extracted and adapted code from :https://github.com/PrettyPrinted/youtube_video_code/blob/master/2020/02/10/Creating%20a%20Login%20Page%20in%20Flask%20Using%20Sessions/flask_session_example/templates/login.htm

'''
#first we import the necessary modules: 
from flask import Flask, session, url_for,redirect, abort,request, render_template,g



#creating class User to introduce concept of user and offer option to login in page. 
class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username = username
        self.password=password
    def __repr__(self): #creating function to return a printable copy of this instance of a object
        return f'<User:{self.username}>'

#creating global variable that represents all users: 
users=[]
users.append(User(id=1, username="Tommy", password="hola"))#adding user credentials using append
users.append(User(id=2, username="Leslie", password="bye"))

#print(users) #PRINTING users for test. 

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secretkey'#created secret key
#checking session and it does exist, put the information isnice the request context , we use "g" module

@app.before_request
def before_request():
    if 'user_id' in session:
        user =[x for x in users if x.id == session['user_id']][0]
        g.user= user#Now we will have access to the user if they are logged in already


@app.route('/')
def home():
    home='hey welcome!'#testing if it works
    return home

@app.route('/login', methods= ['GET', 'POST'])#with his one we return the login page: 
def login():
    if request.method == 'POST':#adding conditional if the method is post
        session.pop('user_id',None)#adding option to remove user id from session if you are trying to login again while your previous session is ongoing
        username=request.form['username']  #here we request the user and password names that come from the form created in the html file "login.html" this will be then the username
        password=request.form['password'] #same procedure for password
        user= [x for x in users if x.username==username][0]#looping through the user list created previously and checking if username   is valid
        if user and user.password == password:#if the password and user that user enters matches the password and user in our system(user.password)
            #then I can start the session for this user.
            session['user_id']=user.id#key for session
            return redirect (url_for('profile'))#now we redirect them to their profile if all information is correct

        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/profile')#returning the profile page, both pages in templates folder for access
def profile():
    if not g.user:#if user is not correct we want to abort, we dont want to show profile page
        return redirect(url_for('login'))
    return render_template('profile.html')



if __name__ == '__main__' :
    app.run(debug= True)