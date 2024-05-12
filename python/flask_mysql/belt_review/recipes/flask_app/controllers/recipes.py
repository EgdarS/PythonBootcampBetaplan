from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/add/recipe')
def addRecipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    loggedUser = User.get_user_by_id(data)
    return render_template('addRecipe.html', loggedUser=loggedUser)

@app.route('/create/recipe', methods = ['POST'])
def createRecipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect(request.referrer)
    data={
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'under': request.form['under'],
        'user_id': session['user_id'],
    }
    Recipe.create(data)
    return redirect('/')

@app.route('/view/recipe/<int:id>')
def viewRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id': id,
        'id': session['user_id']
    }
    recipe = Recipe.get_recipe_by_id(data)
    # if not recipe:
    #     return "Recipe not found"
    loggedUser = User.get_user_by_id(data)
    # if not loggedUser:
    #     return "User not found"
    return render_template('recipe.html', recipe=recipe, loggedUser=loggedUser)

@app.route('/delete/recipe/<int:id>')
def deleteRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'recipe_id':id,
        'id':session['user_id']
    }
    recipe=Recipe.get_recipe_by_id(data)
    loggedUser=User.get_user_by_id(data)
    if loggedUser['id']==recipe['user_id']:
        Recipe.delete_recipe(data)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def editRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'recipe_id':id,
        'id':session['user_id']
    }
    recipe=Recipe.get_recipe_by_id(data)
    loggedUser=User.get_user_by_id(data)
    return render_template('edit.html', recipe=recipe, loggedUser=loggedUser)

@app.route('/update/recipe/<int:id>', methods=['POST'])
def updateRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'recipe_id':id,
        'id':session['user_id'],
        'name':request.form['name'],
        'description' :request.form['description'],
        'instructions':request.form['instructions'],
        'date':request.form['date'],
        'under':request.form['under']       
    }
    Recipe.update_recipe(data)
    return redirect('/')



