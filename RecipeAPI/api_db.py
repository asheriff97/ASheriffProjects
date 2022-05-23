import flask
from flask import Flask, request, jsonify, render_template
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')    

@app.route('/api/recipes/all', methods=['GET'])
def recipe_all():
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_recipes = cur.execute('SELECT recipes.recipe_name FROM recipes;').fetchall()

    return jsonify(all_recipes)

@app.route('/api/ingredients/all', methods=['GET'])
def ingredient_all():
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_ingredients = cur.execute('SELECT ingredients.ingredient_name FROM ingredients;').fetchall()

    return jsonify(all_ingredients)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/recipes', methods=['GET'])
def recipe_filter():
    query_parameters = request.args

    id = query_parameters.get('recipeid')
    name = query_parameters.get('recipe_name')
    #User shouldnt search by instructions

    query_recipe = "SELECT recipes.recipe_name, recipes.instructions FROM recipes WHERE"
    to_filter = []

    if id:
        query_recipe += ' recipeid=? AND'
        to_filter.append(id)
    if name:
        query_recipe += ' recipe_name=? AND'
        to_filter.append(name)
    if not (id or name):
        return render_template('filt_recipe.html')

    query_recipe = query_recipe[:-4] + ';'

    query_ingredients = "select ingredients.ingredient_name FROM recipes, ingredients, relationship WHERE" 
    two_filter = []

    if id:
        query_ingredients += ' recipeid=? AND '
        two_filter.append(id)
    if name:
        query_ingredients += ' recipe_name=? AND '
        two_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    
    
    query_ingredients += "ingredients.ingredientid = relationship.relationship_ingredientid AND recipes.recipeid = relationship.relationship_recipeid;"
    

    conn = sqlite3.connect('recipes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query_recipe, to_filter).fetchall()
    results2 = cur.execute(query_ingredients, two_filter).fetchall()

    return jsonify(results + results2)

@app.route('/api/ingredients', methods = ['GET'])
def ingredient_filter():
    query_parameters = request.args

    id = query_parameters.get('ingredientid')
    name = query_parameters.get('ingredient_name')

    query_ingredient = "SELECT recipes.recipe_name FROM recipes, ingredients, relationship WHERE"
    to_filter = []

    if id:
        query_ingredient += ' ingredientid=? AND'
        to_filter.append(id)
    if name:
        query_ingredient += ' ingredient_name=? AND'
        to_filter.append(name)
    if not (id or name):
        return render_template('filt_ingredient.html')

    query_ingredient += ' ingredients.ingredientid = relationship.relationship_ingredientid AND recipes.recipeid = relationship.relationship_recipeid;'

    conn = sqlite3.connect('recipes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query_ingredient, to_filter).fetchall()

    return jsonify(results)



app.run()

'''
To Do:
- Have ingredients returned with recipe
- UI Interactive (Search by a form w/ submit button)
- Add recipes/ingredients to db 
- Figure out how to order by name first (currently orders alphabetically with instructions showing first)
- Clean up instructions (No line breaks)

select ingredients.ingredient_name 
    from recipes, ingredients, relationship  
    where recipe_name = 'Cheeseburger' AND 
    ingredients.ingredientid = relationship.relationship_ingredientid AND 
    recipes.recipeid = relationship.relationship_recipeid;
'''