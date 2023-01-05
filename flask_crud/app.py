from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

app = Flask(__name__)
#creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer,nullable=True)
    group=db.Column(db.String(200),nullable=True)
    college_name = db.Column(db.String(300),default='Stockholn uni')
    #date = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Record %r>' %self.id

#@app.route("/")

@app.route("/", methods=['GET','POST'])
def index():   
    if request.method == 'POST':
    
        s_name = request.form['name']
        s_age = request.form['age']
        s_group = request.form ['group'] 
        new_student = Student(name=s_name,age=s_age,group=s_group)
        
        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect('/')
        except:
            return 'There is an issue in adding student info'

    else:
        records = Student.query.order_by(Student.name).all()
        return render_template('index.html',records=records)  

@app.route('/delete/<int:id>')
def delete(id):
  record_to_delete = Student.query.get_or_404(id)
  try:
    db.session.delete(record_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'There was an issue in deleting the task' 

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
  record_to_update = Student.query.get_or_404(id)

  if request.method == 'POST':
    record_to_update.name = request.form['name']

    try:
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue in updating the task'
  else:
    return render_template('update.html', record = record_to_update)    




if __name__ == "__main__":
    app.run(debug=True)


'''from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Todo(db.Model):
 id = db.Column(db.Integer,primary_key=True)
 content = db.Column(db.String(200),nullable = False)
 completed = db.Column(db.Integer, default=0)
 date_created = db.Column(db.DateTime,default= datetime.utcnow)
 def __repr__(self):
  return '<Task %r>' %self.id
@app.route('/',methods=['POST','GET'])
def index():
  if request.method == 'POST':
    task_content = request.form['content']
    new_task = Todo(content=task_content)
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')
    except:
      return 'There is an issue in adding the task'
  else:
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html',tasks=tasks)
@app.route('/delete/<int:id>')
def delete(id):
  task_to_delete = Todo.query.get_or_404(id)
  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'There was an issue in deleting the task'
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
  task_to_update = Todo.query.get_or_404(id)
  if request.method == 'POST':
    task_to_update.content = request.form['content']
    try:
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue in updating the task'
  else:
    return render_template('update.html',task = task_to_update)
if __name__ == "__main__":
 app.run(debug=True)
 '''    
