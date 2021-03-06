from flask_restplus import fields,Namespace




class UserDto():
    user_ns = Namespace("user function", description="User registration, login, logout, change password")

    user_model = user_ns.model("login_model",
                                {
                                    "username":fields.String,
                                    "email":fields.String,
                                    "id":fields.Integer,
                                    "token":fields.String,
                                    "message":fields.String
                                })
    user_login_data_model_expect = user_ns.model("user_login_data_model_expect",
                                {
                                    "username":fields.String,
                                    "password":fields.String,
                                })

    user_list_model = user_ns.model("user list",
                                    {
                                        "total_number":fields.Integer,
                                        "users":fields.List(fields.Nested(user_model))

                                    })
    user_Forgetpassword_data_model_expect= user_ns.model("user_Forgetpassword_data_model_expect",
                                {
                                    "username":fields.String,
                                    "email":fields.String,
                                })
    user_UserSignup_model_response= user_ns.model("user_UserSignup_data_model_expect",
                                {
                                    "username":fields.String,
                                    "message":fields.String,
                                })
    user_Forgetpassword_model_response = user_ns.model("user_Forgetpassword_model_response",
                                                          {
                                                              "username": fields.String,
                                                              "password": fields.String,
                                                              "message": fields.String
                                                          })

    user_ChangPassword_model_response= user_ns.model("user_ChangPassword_model_response",
                                                          {
                                                              "username": fields.String,
                                                              "new_password": fields.String,
                                                              "message": fields.String
                                                          })
    user_UserSignup_data_model_expect= user_ns.model("user_UserSignup_data_model_expect",
                                {
                                    "username":fields.String,
                                    "password1": fields.String,
                                    "password2": fields.String,
                                    "email":fields.String,
                                })
    user_ChangPassword_data_model_expect= user_ns.model("user_ChangPassword_data_model_expect",
                                {
                                    "username":fields.String,
                                    "old_password": fields.String,
                                    "new_password": fields.String,
                                })
class RecipeDto():
    Recipe_ns = Namespace("Recipe function", description="Recipe information,upload,search")

    Recipe_model = Recipe_ns.model("Recipe_model",
                                {
                                    "R_name":fields.String,
                                    "R_description":fields.String,
                                    "R_category":fields.String,
                                    "R_calorie":fields.String,
                                    "R_imgdata":fields.String,
                                    "id":fields.Integer
                                })

    recipe_list_model = Recipe_ns.model("Recipe list",
                                    {
                                        "total_number": fields.Integer,
                                        "Recipes": fields.List(fields.Nested(Recipe_model))

                                    })
