from flask import Flask, render_template, request, redirect, url_for
from models import Recipe, User, recipes, users, current_user

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', recipes=recipes, current_user=current_user)

@app.route('/recipe_detail/<int:recipe_id>')
def recipe_detail(recipe_id):
	recipe = next((r for r in recipes if r.recipe_id==recipe_id), None)
	if recipe:
		return render_template('recipe_detail.html', recipe=recipe, recipes=recipes, current_user=current_user)
	else:
		return "Recipe not found.", 404

@app.route('/user/<string:user_id>')
def user_recipes(user_id):
	user = next((u for u in users if u.user_id==user_id), None)
	if user:
		return render_template('user_recipes.html', user=user, current_user=current_user)
	else:
		return "User not found.", 404
	
@app.route('/add/favorite/<int:recipe_id>')
def add_favorite(recipe_id):
	recipe = next((r for r in recipes if r.recipe_id==recipe_id), None)
	if recipe:
		current_user.add_favorite(recipe)
	return redirect(url_for('index', recipe_id=recipe_id))

@app.route('/remove/favorite/<int:recipe_id>')
def remove_favorite(recipe_id):
	recipe = next((r for r in recipes if r.recipe_id==recipe_id), None)
	if recipe in current_user.favorite_recipes:
		current_user.favorite_recipes.remove(recipe)
	return redirect(url_for('index'))

	
@app.route('/recipe/add', methods=['GET', 'POST'])
def add_recipe():
	if request.method == 'POST':
		title = request.form['title']
		description = request.form['description']
		ingredients = request.form['ingredients'].split('\n')
		instructions = request.form['instructions'].split('\n')
		prep_time = int(request.form['prep_time'])
		cook_time = int(request.form['cook_time'])
		difficulty = request.form['difficulty']
		cuisine = request.form['cuisine']

		new_recipe = Recipe(
				title, description, ingredients, instructions,
				prep_time, cook_time, difficulty, cuisine
		)

		recipes.append(new_recipe)
		current_user.add_recipe(new_recipe)
		
		return redirect(url_for('recipe_detail', recipe_id=new_recipe.recipe_id))
	
	return render_template('add_recipe.html', current_user=current_user)

if __name__ == '__main__':
	app.run(debug=True, port=5002)