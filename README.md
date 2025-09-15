# Intro to Python in Context - Web Application

### Lesson Introduction: Notice & Wonder

Begin by launching the todo-app for the students. Display the running application in a browser, allowing students to interact:
- Add tasks
- Mark tasks complete
- Delete tasks
- View the count of tasks

Ask students to:
- **Notice**: What features do they see? What happens when they interact?
- **Wonder**: How does clicking “Add” actually create a task? What controls the “Complete” and “Delete” actions? Where does the app store tasks?
(Capture responses on the board for reference during the lesson.)

### Exploring the App Structure

#### The Flask Framework

- Introduce **Flask** as a lightweight Python web framework.
- Discuss the basics: routing, HTTP methods (GET, POST), templates.

#### Code Walkthrough: app.py

- Show the `app.py` file.
- Highlight the **Flask object** instantiation:  
  ```python
  app = Flask(__name__)
  ```
- Explain routing:
  - `'/'` for displaying tasks (notice how `base.html` renders the todo list)
  - `/add` for adding tasks
  - `/complete/<task_id>` and `/delete/<task_id>` for modifying tasks
  - `/count` for returning the number of tasks

#### Data Structures

- Discuss the `todo_list` as a Python **list of dictionaries** storing task state.
- Point out `id_counter` as a simple way to uniquely identify each task.

#### Template Rendering

- Show how **templates** are used with `render_template('base.html', todo_list=todo_list)`.
- Highlight separation of logic (Python) and presentation (HTML).

### Theory Connection: Key Python Concepts

- **Functions & Routing**: Each route is a Python function wrapped with a decorator.
- **Global Variables**: `todo_list` and `id_counter` demonstrate state management.
- **Dictionaries**: Used to store individual tasks, showcasing key-value pairs.
- **Loops**: Sequential search for marking complete or deleting uses Python’s `for` loop.
- **Web Principles**: How POST/GET actions connect web forms and server actions.

### Building Step-by-Step

Guide students through:
1. Setting up Flask and the basic app.
2. Creating routes for core actions.
3. Managing data in-memory with Python lists and dictionaries.
4. Connecting templates to Python data via Jinja2 (used in Flask templates).

### Discussion and Reflection

- Return to the “wonder” questions: “How does the app keep track of tasks?” “Why use dictionaries?”
- Ask students to modify or extend the app, e.g., add an edit feature, persist data with files, or add categories.

## Assignment: Extending the Todo-App

**Objective**: Reinforce understanding of Flask routes, Python data structures, and templates by modifying and improving the todo application.

#### Task List

- **Add an "Edit" Feature**  
  Implement a route and form that lets users edit the title of an existing task. This will require a new route and HTML form in the template.

- **Persist Data to a File**  
  Modify the application so that tasks are saved to and loaded from a local text (or JSON) file, instead of only in memory. Use appropriate Python file I/O methods.  
  (Hint: Save the `todo_list` after any change, and load it at startup.)

- **Improve the Template**  
  In `base.html`, add conditional formatting so that completed tasks are visually different (e.g., grayed out, strikethrough).

- **Reflection**  
  Write a brief reflection (150-200 words) answering:  
  - How does Flask handle HTTP methods and URLs?  
  - Why is it important to persist data in web applications?  
  - Share one challenge encountered and how it was solved.

#### Submission Requirements

- Modified versions of `app.py` and `base.html`.
- A sample JSON or text file showing saved tasks.
- The written reflection.

### Assessment Criteria

- **Functionality**: Features work as described (edit, persist).
- **Code Quality**: Python code follows best practices, is readable and commented.
- **Understanding**: Reflection demonstrates grasp of concepts and thoughtful problem-solving.
