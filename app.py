# libraries
from flask import Flask, render_template, request, redirect, url_for

# using a class to build an object
app = Flask(__name__)

# Simple in-memory store for tasks
todo_list = []
id_counter = 0

@app.route('/')
def index():
    #using an imported object
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        # Store task as a dict with status
        global id_counter
        id_counter += 1
        todo_list.append({'id': id_counter, 'title': title, 'complete': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    # sequential search
    for todo in todo_list:
        if todo['id'] == task_id:
            todo['complete'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # another sequential search
    global todo_list
    todo_list = [todo for todo in todo_list if todo['id'] != task_id]
    return redirect(url_for('index'))

#we can access but not change
@app.route('/count')
def count():
    #id_counter+=1
    return str(id_counter)

if __name__ == "__main__":
    app.run(debug=True)
