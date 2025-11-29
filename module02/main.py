import tkinter as tk
from tkinter import simpledialog, messagebox
import recipe_db as db
import random

RECIPE_ID = None
recipe_count = 0



#8 Gets the number of recipes in the DB and saves it to a global variable
def refresh_recipe_count():
  global recipe_count
  recipe_count = db.get_recipe_count()



#9 Gets the recipe from the DB and puts it into the UI (RETRIEVE)
def show_recipe(recipe_id):
  global RECIPE_ID
  RECIPE_ID = recipe_id
  recipe = db.get_recipe(recipe_id)

  listbox.delete(0, tk.END)

  if recipe:
    recipe_name.config(text=recipe[0][0])
    for row in recipe:
      ingredient = row[2]
      amount = row[3]
      listbox.insert("end", f"{ingredient} - {amount}")



#10 Uses the count of recipes in the DB, then generates a random number to then show the recipe corresponding to that number
def get_random_recipe():
  if recipe_count == 0:
    messagebox.showinfo("Info", "No recipes in the database.")
    return
  recipe_id = random.randint(1, recipe_count)
  show_recipe(recipe_id)



#11 Update the amount for an ingredient (MODIFY)
def update_ingredient():
  if RECIPE_ID is None:
    messagebox.showwarning("Warning", "Select a recipe first!")
    return

  ingredient_input = simpledialog.askstring(
    "Ingredient", "Enter ingredient name to update:"
  )
  if not ingredient_input:
    return

  amount_input = simpledialog.askstring(
    "Amount", f"Enter new amount for {ingredient_input}:"
  )
  if not amount_input:
    return

  db.update_ingredient_amount(RECIPE_ID, ingredient_input, amount_input)
  show_recipe(RECIPE_ID)



#12 Add a new recipe into the database (INSERT)
def add_new_recipe():
  name = simpledialog.askstring("Recipe Name", "Enter recipe name:")
  if not name:
    return
  instructions = simpledialog.askstring("Instructions", "Enter instructions:")
  if not instructions:
    return

  ingredients_dict = {}

  while True:
    ing_name = simpledialog.askstring("Ingredient", "Enter ingredient name (or leave blank to finish):")
    if not ing_name:
      break
    amount = simpledialog.askstring("Amount", f"Enter amount for {ing_name}:")
    if not amount:
      amount = ""
    ingredients_dict[ing_name] = amount

  if ingredients_dict:
    db.add_recipe(name, instructions, ingredients_dict)
    refresh_recipe_count()
    messagebox.showinfo("Success", f"Recipe '{name}' added!")



#13 Delete the current recipe (DELETE)
def delete_recipe():
  if RECIPE_ID is None:
    messagebox.showwarning("Warning", "Select a recipe first!")
    return

  confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this recipe?")
  if confirm:
    db.delete_recipe(RECIPE_ID)
    refresh_recipe_count()
    listbox.delete(0, tk.END)
    recipe_name.config(text="")
    messagebox.showinfo("Deleted", "Recipe deleted!")
# ------------------------------------------------------------------------------------------------------------------



# Initialize database
db.initialize_db()
refresh_recipe_count()

if recipe_count == 0:
  db.populate_sample_data()
  refresh_recipe_count()


#14 Set up the UI
root = tk.Tk()
root.title("Recipe Book")
root.geometry("500x400")
root.config(background="lightgreen")

recipe_name = tk.Label(root, text="", font=("Arial", 16), bg="lightgreen")
recipe_name.pack(pady=10)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="lightgreen")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Random Recipe", command=get_random_recipe).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Ingredient", command=update_ingredient).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Add Recipe", command=add_new_recipe).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Delete Recipe", command=delete_recipe).grid(row=0, column=3, padx=5)

root.mainloop()