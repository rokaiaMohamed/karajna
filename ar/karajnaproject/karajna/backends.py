from django.contrib.auth.models import User
#from django.contrib.auth.hashers import check_password
class EmailBackend(object):
  """
  Custom Authentication backend that supports using an e-mail address
  to login instead of a username.

  See: http://blog.cingusoft.org/custom-django-authentication-backend
  """
  supports_object_permissions = False
  supports_anonymous_user = False
  supports_inactive_user = False

  def authenticate(self, username=None, password=None):
    try:
      if '@' in username:
        user = User.objects.get(email=username)
      else:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
      return None

    if getattr(user , 'is_active') and user.check_password(password):
      return user
    return None
    # Check password of the user we found
    #if check_password(password, user.password):
    #  return user
    #return None

  # Required for the backend to work properly - unchanged in most scenarios
  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
