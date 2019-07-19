import os

from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

# #Prescribes a database path and which engine it runs (sqlite)
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
# #Tells flask where the database is stored
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# #Initializes connection to database
# db = SQLAlchemy(app)
# db.create_all()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///bookdb.sqlite")

conn = engine.connect()

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()

Base = declarative_base()

#Define Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key = True)
    title = Column(String(80))

   #This code defines how to represent the model as a string.
    def __repr__(self):
        return "<Title: {}>".format(self.title)

Base.metadata.create_all(engine)        

@app.route("/", methods=["GET", "POST"])
def home():
    
    #This is how we store the input of the form. It's stored as an ImmutableMultiDict,
    #which is a dictionary with the 'name' element of the form as its key.
    #Results in ImmutableMultiDict([('title': 'Blah')])
    #Retrieve and return all the previously entered books 
    books= session.query(Book).all()
     
    if request.form:
        #Saves user input as an instance of the class       
        book = Book(title= request.form.get("title"))
        #Adds and commits it to the database
        session.add(book)
        session.commit()
        
    return render_template("home.html", books=books)

@app.route("/update", methods=["POST"])
def update():
    #Gets the old and updated title
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")    
    #Gets the old info from the database
    book = Book.query.filter_by(title=oldtitle).first()
    #Updates the title
    book.title = newtitle
    #Commits the changes
    session.commit()
    #Redirects the user to the main page
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = session.query.filter_by(title=title).first()
    session.delete(book)
    session.commit()
    return redirect("/"
    )
if __name__ == "__main__":
    app.run(debug=False)    