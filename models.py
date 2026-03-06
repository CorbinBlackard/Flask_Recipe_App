from datetime import datetime

class Recipe:
	id_counter = 1

	def __init__(self, title, description, ingredients, instructions, prep_time, cook_time, difficulty, cuisine):
		self.title = title
		self.description = description
		self.ingredients = ingredients
		self.instructions = instructions
		self.prep_time = prep_time
		self.cook_time = cook_time
		self.difficulty = difficulty
		self.cuisine = cuisine
		self.created_date = datetime.now()
		self.recipe_id = Recipe.id_counter
		Recipe.id_counter += 1


class User:
	id_counter = 1
	def __init__(self, name):
		self.name = name
		self.my_recipes = []
		self.favorite_recipes = []
		self.meal_plan = set()
		self.user_id = f"USER{User.id_counter:03d}"
		User.id_counter += 1

	def add_recipe(self, recipe):
		self.my_recipes.append(recipe)

	def add_favorite(self, recipe):
		if recipe not in self.favorite_recipes:
			self.favorite_recipes.append(recipe)

	def remove_favorite(self, recipe):
		if recipe in self.favorite_recipes:
			self.favorite_recipes.remove(recipe)






recipes = [
	Recipe(
		"Spaghetti Carbonara", 
		"Classic Roman pasta dish with eggs, cheese, and guanciale",
		["spaghetti", "eggs", "pecorino cheese", "guanciale", "black pepper", "salt"],
		["Bring large pot of salted water to boil", "Cook spaghetti according to package", 
			"Fry guanciale until crispy", "Beat eggs with grated pecorino", 
			"Drain pasta, reserving some water", "Mix hot pasta with egg mixture and guanciale",
			"Add pasta water if needed", "Serve with extra pepper and cheese"],
		10, 15, "Medium", "Italian"
	),
	
	Recipe(
		"Simple Guacamole",
		"Fresh and creamy avocado dip",
		["avocados", "lime", "onion", "cilantro", "jalapeño", "salt", "tomato"],
		["Mash avocados in a bowl", "Finely dice onion and jalapeño", "Chop cilantro",
			"Mix everything together", "Squeeze lime juice", "Dice tomato and fold in", "Salt to taste"],
		10, 0, "Easy", "Mexican"
	),
	
	Recipe(
		"Chicken Stir Fry",
		"Quick weeknight dinner with vegetables",
		["chicken breast", "soy sauce", "broccoli", "carrots", "bell peppers", 
			"garlic", "ginger", "sesame oil", "rice"],
		["Cook rice according to package", "Cut chicken into bite-sized pieces",
			"Chop all vegetables", "Heat oil in wok or large pan", 
			"Cook chicken until golden, remove", "Stir fry vegetables until tender-crisp",
			"Add chicken back to pan", "Add soy sauce and toss", "Serve over rice"],
		15, 10, "Easy", "Asian"
	),
	
	Recipe(
		"Chocolate Chip Cookies",
		"Classic soft and chewy cookies",
		["flour", "butter", "brown sugar", "white sugar", "eggs", "vanilla extract",
			"baking soda", "salt", "chocolate chips"],
		["Preheat oven to 375°F", "Cream butter and sugars together",
			"Beat in eggs and vanilla", "Mix dry ingredients separately",
			"Combine wet and dry ingredients", "Stir in chocolate chips",
			"Drop spoonfuls onto baking sheet", "Bake 10-12 minutes", "Cool on rack"],
		15, 12, "Easy", "Dessert"
	),
	
	Recipe(
		"Vegetable Soup",
		"Hearty and healthy comfort food",
		["onion", "carrots", "celery", "potatoes", "vegetable broth", "tomatoes",
			"garlic", "bay leaf", "thyme", "salt", "pepper", "olive oil"],
		["Chop all vegetables", "Heat oil in large pot", "Sauté onion, carrots, celery",
			"Add garlic and cook 1 minute", "Add broth, tomatoes, potatoes",
			"Add bay leaf and thyme", "Simmer 30 minutes until vegetables tender",
			"Season with salt and pepper", "Serve hot"],
		15, 35, "Easy", "American"
	),
	
	Recipe(
		"Greek Salad",
		"Fresh and colorful summer salad",
		["cucumber", "tomatoes", "red onion", "feta cheese", "kalamata olives",
			"olive oil", "oregano", "red wine vinegar", "salt", "pepper"],
		["Chop cucumber and tomatoes", "Thinly slice red onion",
			"Combine vegetables in bowl", "Add whole olives", "Crumble feta on top",
			"Whisk oil, vinegar, oregano", "Dress salad just before serving",
			"Season with salt and pepper"],
		10, 0, "Easy", "Greek"
	),
	
	Recipe(
		"Beef Tacos",
		"Customizable family favorite",
		["ground beef", "taco seasoning", "tortillas", "lettuce", "tomato",
			"cheddar cheese", "sour cream", "salsa", "onion", "cilantro"],
		["Brown ground beef in skillet", "Drain fat", "Add taco seasoning and water",
			"Simmer until thickened", "Warm tortillas", "Chop lettuce and tomato",
			"Shred cheese", "Set up taco bar with all toppings",
			"Let everyone build their own"],
		10, 15, "Easy", "Mexican"
	),
	
	Recipe(
		"Pancakes",
		"Fluffy breakfast favorite",
		["flour", "milk", "egg", "butter", "baking powder", "sugar", "salt", "maple syrup"],
		["Melt butter and cool slightly", "Mix dry ingredients in large bowl",
			"Whisk milk, egg, and melted butter", "Combine wet and dry ingredients gently",
			"Lumps are okay, don't overmix", "Heat griddle or pan",
			"Pour 1/4 cup batter for each pancake", "Flip when bubbles form",
			"Cook until golden on both sides", "Serve with butter and syrup"],
		5, 15, "Easy", "Breakfast"
	),
	
	Recipe(
		"Lentil Soup",
		"Protein-packed vegetarian soup",
		["lentils", "onion", "carrots", "celery", "garlic", "vegetable broth",
			"tomatoes", "cumin", "bay leaf", "spinach", "lemon", "olive oil"],
		["Rinse lentils", "Chop onion, carrots, celery", "Heat oil in large pot",
			"Sauté vegetables until soft", "Add garlic and cumin, cook 1 minute",
			"Add lentils, broth, tomatoes, bay leaf", "Simmer 30-40 minutes until lentils tender",
			"Stir in spinach until wilted", "Squeeze lemon juice", "Serve hot"],
		10, 40, "Medium", "Mediterranean"
	),
	
	Recipe(
		"Banana Bread",
		"Perfect way to use ripe bananas",
		["ripe bananas", "flour", "butter", "sugar", "eggs", "baking soda",
			"salt", "vanilla extract", "walnuts (optional)"],
		["Preheat oven to 350°F", "Mash bananas in a bowl", "Cream butter and sugar",
			"Beat in eggs and vanilla", "Mix in bananas", "Combine dry ingredients separately",
			"Fold dry ingredients into wet", "Fold in walnuts if using",
			"Pour into loaf pan", "Bake 55-60 minutes", "Cool before slicing"],
		15, 60, "Easy", "Baking"
	)
]

users = [
	User("Alice"),
	User("Corbin")
]
current_user = users[1]