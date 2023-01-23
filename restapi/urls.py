from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.contrib import admin

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'todo', views.taskList, basename='todo')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('', views.home),
    path('todolist/', views.taskList, name='todolist'),
    path('createtodo/', views.createTask, name='createtodo'),
    # POST REQUEST IS NEEDED FOR THE BELLOW APIS
    path('updatetodo/', views.updateTask, name='updatetodo'),
    path('deletetodo/>', views.deleteTask, name='deletetodo')
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]