<h1>Students Performance</h1>

<p>The goal of this project is to predict a student s math score based on his attributes. The dataset was taken from Kaggle. You can access  it clicking <a href="https://www.kaggle.com/datasets/spscientist/students-performance-in-exams">here</a>.</p>

<img src="frontend/public/students-performance.gif" />

<h2>Technologies</h2>
<div><img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)" />
<img src ="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D" />
<img src="https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF" /></div>

<h2>Setup</h2>

<strong>Node</strong> is required to run this application. You can install it <a href="https://nodejs.org/en">here</a>.

With Node already installed, go to the folder `frontend` in the terminal and run the following command:

```bash
npm install
```

This command will get all the vue, vite and vuetify dependecies automatically.

Then, you're ready to start the vuetify setup, just run:

```bash
npm run dev
```

To run the algorithm and the database, first you will need to install the <a href="https://www.python.org/">Python Interpreter</a>.

With Python installed, it's needed to create a virtual environment to isolate all the dependencies in the project folder. To make it easer, just run in the project root directory:

**Linux**

```bash
python3 -m venv venv
```

To activate the virtual env, run:

```bash
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
```

To activate the virtual env, run:

`cmd`

```bash
.\venv\Scripts\activate.bat
```

`PowerShell`

```bash
.\venv\Scripts\activate.ps1
```

**Running SQL Database**

Django detects the changes in the models by running the following command:

```bash
python manage.py makemigrations
```

To effectively build the database tables, run:

```bash
python manage.py migrate
```

Then, you're ready to run the Django project:

```bash
python manage.py runserver
```
