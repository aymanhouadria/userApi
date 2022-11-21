
from django.urls import path
from users_api.views import (CreateUserView, GetUsersView,GetUserView ,DeleteUsersView, UpdateUsersView)

app_name = "users"

urlpatterns = [
    path('createUsers', CreateUserView.as_view(), name="create_user"),
    path('getusers', GetUsersView.as_view(), name="get_users"),
    path('getusersById/<int:pk>', GetUserView.as_view(), name="get_users_by_id"),
    path('updateUsersById/<int:pk>', UpdateUsersView.as_view(), name="update_users_by_id"),
    path('deleteUsersById/<int:pk>', DeleteUsersView.as_view(), name="delete_users_by_id"),


    #path('getUserById/^(?P<id>[0-9])$', GetUsersByIdView.as_view(), name="get_user_by_id"),
]
