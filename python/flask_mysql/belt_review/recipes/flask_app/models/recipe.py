from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name = 'loginregistration'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        self.user_id= data['user_id']

    @classmethod
    def create(cls,data):
        query = 'INSERT INTO recipes (name, description, instructions, date, under, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date)s, %(under)s, %(user_id)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def getAllRecipes(cls):
        query = 'SELECT * FROM recipes'
        results = connectToMySQL(cls.db_name).query_db(query)
        if results:
            recipes= []
            for recipe in results:
                recipes.append(recipe)
        return recipes


    @classmethod
    def get_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes where id = %(recipe_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False

    # @classmethod
    # def get_recipe_by_id(cls,data):
    #     query = "SELECT * FROM recipes left join users on recipe.user_id = users.id where recipe.id = %(recipe_id)s;"
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     if results:
    #         return results[0]
    #     return False
    
    @classmethod
    def delete_recipe(cls,data):
        query = 'DELETE FROM recipes WHERE id=%(recipe_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def update_recipe(cls,data):
        query = 'UPDATE recipes set name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under = %(under)s WHERE id = %(recipe_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name'])<3:
            flash('Name should include more than 3 characters!','NameRecipeRegister')
            is_valid=False
        if len(data['description'])<3:
            flash('Description should include more than 3 characters!', 'DescriptionRecipeRegister')
            is_valid=False
        if len(data['instructions'])<3:
            flash('Instructions should include more than 3 characters!', 'InstructionsRecipeRegister')
        if not data['date']:
            is_valid=False
            flash('The date this recipe was created at is required!', 'DateRecipeRegister')
            is_valid=False
        if not data['under']:
            flash('The time it takes to cook this recipe is required to be included!', 'UnderRecipeRegister')
            is_valid=False
        return is_valid