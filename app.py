from flask import Flask, request, render_template, redirect
from stories import Story, story

app = Flask(__name__)



@app.route('/')
def show_homepage():
    
    return render_template('home.html')

@app.route('/home')
def redirect_home():
    return redirect('/')

@app.route('/form')
def show_madlibs_form():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def render_story_and_display():
    
    completed_story = story.generate(request.args)

    return render_template('story.html', completed_story=completed_story)

@app.route('/create')
def display_story_create_form():
    return render_template('create.html')

@app.route('/form_from_create')
def show_madlibs_from_create():
    words = request.args.get('words')
    text = request.args.get('template')

    prompts = list(words.split(", "))
    return render_template('form_from_create.html', prompts=prompts, words=words, text=text)

@app.route('/story_from_create')
def display_created_story():
    words = request.args.get('words')
    text = request.args.get('text')

    new_story = Story(words, text)

    
    created_story = new_story.generate(request.args)
    return render_template("created_story.html", created_story=created_story)
