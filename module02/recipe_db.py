import sqlite3 as sql

DB_NAME = "recipes.db"

def get_connection():
  return sql.connect(DB_NAME)



#1 Create the sqlite database if it doesn't already exist
def initialize_db():
  connection = get_connection()
  cursor = connection.cursor()

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS recipes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          instructions TEXT,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
  """)

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS ingredients (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT UNIQUE NOT NULL
      );
  """)

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS recipe_ingredients (
          recipe_id INTEGER,
          ingredient_id INTEGER,
          amount TEXT,
          FOREIGN KEY(recipe_id) REFERENCES recipes(id),
          FOREIGN KEY(ingredient_id) REFERENCES ingredients(id),
          PRIMARY KEY(recipe_id, ingredient_id)
      );
  """)

  connection.commit()
  connection.close()



#2 This function is used to add a recipe into the db
def add_recipe(name, instructions, ingredients_dict):
  con = get_connection()
  cur = con.cursor()

  cur.execute(
      "INSERT INTO recipes (name, instructions) VALUES (?, ?)",
      (name, instructions)
  )
  recipe_id = cur.lastrowid

  for ingredient_name, amount in ingredients_dict.items():
      cur.execute(
          "INSERT OR IGNORE INTO ingredients (name) VALUES (?)",
          (ingredient_name,)
      )

      cur.execute(
          "SELECT id FROM ingredients WHERE name = ?",
          (ingredient_name,)
      )
      ingredient_id = cur.fetchone()[0]

      cur.execute(
          """
          INSERT OR REPLACE INTO recipe_ingredients 
          (recipe_id, ingredient_id, amount)
          VALUES (?, ?, ?)
          """,
          (recipe_id, ingredient_id, amount)
      )

  con.commit()
  con.close()



#3 This function adds a bunch of sample data into the database
def populate_sample_data():
  add_recipe(
      "Pancakes",
      "Mix ingredients and cook on a hot griddle.",
      {
          "Flour": "2 cups",
          "Eggs": "2",
          "Milk": "1.5 cups",
          "Sugar": "2 tbsp",
          "Baking Powder": "2 tsp"
      }
  )

  add_recipe(
      "Spaghetti Bolognese",
      "Brown meat, add sauce, simmer, and serve with pasta.",
      {
          "Ground Beef": "1 lb",
          "Tomato Sauce": "2 cups",
          "Onion": "1, chopped",
          "Spaghetti": "12 oz",
          "Garlic": "2 cloves"
      }
  )

  add_recipe(
      "Guacamole",
      "Mash avocados and mix all ingredients together.",
      {
          "Avocado": "3",
          "Lime": "1 tbsp juice",
          "Salt": "1 tsp",
          "Onion": "1/4 cup, diced",
          "Cilantro": "2 tbsp"
      }
  )

  add_recipe(
    "Chocolate Chip Cookies",
    "Mix ingredients, form dough into balls, bake at 350°F for 12 minutes.",
    {
        "Flour": "2.5 cups",
        "Sugar": "1 cup",
        "Brown Sugar": "1 cup",
        "Butter": "1 cup",
        "Eggs": "2",
        "Chocolate Chips": "2 cups",
        "Vanilla Extract": "2 tsp",
        "Baking Soda": "1 tsp",
        "Salt": "1/2 tsp"
    }
  )

  add_recipe(
      "Caesar Salad",
      "Toss lettuce with dressing, croutons, and Parmesan cheese.",
      {
          "Romaine Lettuce": "1 head",
          "Caesar Dressing": "1/2 cup",
          "Parmesan Cheese": "1/4 cup, grated",
          "Croutons": "1 cup",
          "Lemon Juice": "1 tbsp"
      }
  )

  add_recipe(
      "French Toast",
      "Dip bread in egg mixture and fry until golden brown on both sides.",
      {
          "Bread Slices": "4",
          "Eggs": "2",
          "Milk": "1/2 cup",
          "Sugar": "1 tbsp",
          "Cinnamon": "1 tsp",
          "Butter": "2 tbsp"
      }
  )

  add_recipe(
      "Chicken Stir Fry",
      "Cook chicken, add vegetables, and stir fry with sauce.",
      {
          "Chicken Breast": "1 lb",
          "Broccoli": "2 cups",
          "Carrots": "1 cup, sliced",
          "Soy Sauce": "1/4 cup",
          "Garlic": "2 cloves",
          "Ginger": "1 tsp",
          "Olive Oil": "2 tbsp"
      }
  )

  add_recipe(
      "Tomato Soup",
      "Cook tomatoes and onions, blend, and simmer with seasoning.",
      {
          "Tomatoes": "4 cups, chopped",
          "Onion": "1, chopped",
          "Garlic": "2 cloves",
          "Vegetable Broth": "2 cups",
          "Salt": "1 tsp",
          "Pepper": "1/2 tsp",
          "Olive Oil": "1 tbsp"
      }
  )

  add_recipe(
      "Omelette",
      "Beat eggs, pour into pan, add fillings, and fold.",
      {
          "Eggs": "3",
          "Milk": "2 tbsp",
          "Cheese": "1/4 cup, shredded",
          "Bell Pepper": "1/4 cup, chopped",
          "Salt": "1/4 tsp",
          "Pepper": "1/4 tsp",
          "Butter": "1 tbsp"
      }
  )

  add_recipe(
      "Banana Smoothie",
      "Blend all ingredients until smooth.",
      {
          "Banana": "2",
          "Milk": "1 cup",
          "Yogurt": "1/2 cup",
          "Honey": "1 tbsp",
          "Ice Cubes": "4"
      }
  )

  add_recipe(
      "Grilled Cheese Sandwich",
      "Place cheese between bread slices and grill until golden brown.",
      {
          "Bread Slices": "2",
          "Cheddar Cheese": "2 slices",
          "Butter": "1 tbsp"
      }
  )

  add_recipe(
      "Beef Tacos",
      "Cook beef with seasoning, fill tortillas with beef and toppings.",
      {
          "Ground Beef": "1 lb",
          "Taco Shells": "8",
          "Lettuce": "1 cup, shredded",
          "Cheddar Cheese": "1/2 cup, shredded",
          "Salsa": "1/2 cup",
          "Onion": "1/4 cup, diced"
      }
  )

  add_recipe(
      "Greek Yogurt Parfait",
      "Layer yogurt, fruit, and granola in a glass.",
      {
          "Greek Yogurt": "1 cup",
          "Strawberries": "1/2 cup, sliced",
          "Blueberries": "1/2 cup",
          "Granola": "1/2 cup",
          "Honey": "1 tbsp"
      }
  )



#4 Get a recipe from the database
# It uses a JOIN to get all of the information about the recipe and ingredients
def get_recipe(recipe_id):
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute(
    """
    SELECT r.name, r.instructions, i.name, ri.amount from recipes as r
    INNER JOIN recipe_ingredients ri on r.id = ri.recipe_id
    INNER JOIN ingredients i on ri.ingredient_id = i.id
    WHERE r.id = ?
    """,
    (recipe_id,)
  )
  return cursor.fetchall()



#5 This function gets the number of recipes in the database
def get_recipe_count():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT COUNT(*) FROM recipes")
  count = cursor.fetchone()
  return count[0]



#6 This function updates the amount of an ingredient for a specific recipe
def update_ingredient_amount(recipe_id, ingredient_name, new_amount):
  con = get_connection()
  cur = con.cursor()

  cur.execute("SELECT id FROM ingredients WHERE name = ?", (ingredient_name,))
  row = cur.fetchone()
  if not row:
    con.close()
    return
  ingredient_id = row[0]

  cur.execute(
    "UPDATE recipe_ingredients SET amount = ? WHERE recipe_id = ? AND ingredient_id = ?",
    (new_amount, recipe_id, ingredient_id)
  )
  con.commit()
  con.close()



#7 This function deletes a recipe from the database
def delete_recipe(recipe_id):
  con = get_connection()
  cur = con.cursor()
  cur.execute("DELETE FROM recipe_ingredients WHERE recipe_id = ?", (recipe_id,))
  cur.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
  con.commit()
  con.close()
