
""" Links """
base_url = 'https://stellarburgers.nomoreparties.site'
create_new_user_link = base_url + '/api/auth/register'
login_link = base_url + '/api/auth/login'
get_and_update_user_profile_link = base_url + '/api/auth/user'
create_order_link = base_url + '/api/orders'
get_user_orders_link = base_url + '/api/orders'
delete_user_link = base_url + "/api/auth/user"

""" Data """
correct_ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa72"]}
not_existed_ingredient = {"ingredients": 'ksdfklsdfksdlfsdkf'}

""" Errors """
error_ingredient_id = 'Ingredient ids must be provided'
User_already_exist = 'User already exists'
required_field = 'Email, password and name are required fields'
authorised_required = 'You should be authorised'
incorrect_email_password = 'email or password are incorrect'
