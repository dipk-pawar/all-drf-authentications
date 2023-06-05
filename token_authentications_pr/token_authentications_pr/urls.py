from django.contrib import admin
from django.urls import path, include
from auth_app import views
from rest_framework.routers import DefaultRouter
from auth_app.custom_auth import CustomAuthToken
# from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name="get_token") # you can use this for custom auth token
    # path('login/', obtain_auth_token)
]


"""To fetch the token use below API from postman"""
# http://127.0.0.1:8000/login/
# Body:
#     {
#         "username":"dipak123",
#         "password":"xyz123"
#     }


"""To fetch the data use below API"""
# http://127.0.0.1:8000/studentapi/
# Headers : Authorization : Token 275d6052eb256c9a3a9b6a2e099cfa01610159fa