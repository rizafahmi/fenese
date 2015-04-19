from flask.ext.bcrypt import generate_password_hash, check_password_hash

def set_password(User, password):
  User.password = generate_password_hash(password)

  return User

def validate_password(User, password):
  return check_password_hash(User.password, password)
