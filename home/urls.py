from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
#     blogs
    path("", views.Blog.as_view(), name="blogs"),
    path("blog/<str:slug>/", views.blog_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.delete_blog_post, name="delete_blog_post"),

    
#     profile
    path("profile/", views.profile, name="profile"),

#    user authentication
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
