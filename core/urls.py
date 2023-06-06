"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    # path('index/', views.index, name='index'),

    path('recipes/', views.RecipesList.as_view(), name='recipes'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe'),
    path('recipes/components/<int:pk>', views.ComponentDetail.as_view(), name='recipe_component'),
    path('recipes/tools/<int:pk>', views.ToolDetail.as_view(), name='recipe_tool'),
    path('recipe_create', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipe_update/<int:pk>', views.UpdateRecipe.as_view(), name='recipe_update'),
    path('recipe_delete/<int:pk>', views.DeleteRecipe.as_view(), name='recipe_delete'),

    path('components/', views.ComponentsList.as_view(), name='components'),
    path('components/<int:pk>', views.ComponentDetail.as_view(), name='component'),
    path('component_create', views.ComponentCreate.as_view(), name='component_create'),
    path('component_update/<int:pk>', views.UpdateComponent.as_view(), name='component_update'),
    path('component_delete/<int:pk>', views.DeleteComponent.as_view(), name='component_delete'),

    path('tools/', views.ToolsList.as_view(), name='tools'),
    path('tools/<int:pk>', views.ToolDetail.as_view(), name='tool'),
    path('tool_create', views.ToolCreate.as_view(), name='tool_create'),
    path('tool_update/<int:pk>', views.UpdateTool.as_view(), name='tool_update'),
    path('tool_delete/<int:pk>', views.DeleteTool.as_view(), name='tool_delete'),
]
