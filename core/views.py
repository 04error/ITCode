from django.db.models import QuerySet
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core import models, forms
from core.datatools import calc_datatools


class TitleMixin:
    title = None

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


'''
def index(request):
    user = request.user.username
    if user != 'admin':
        html = "<html> <head> <title>Главная страница </title>" \
               "<style>.fade-effect{transition: color 0.5s; color:#000000} .fade-effect:hover{color:#999999}</style></head>" \
               "<body> <h1 class='fade-effect'> Привет, анон </h1> </body> </html>"
    return HttpResponse(html)
'''


# region ListViews
class RecipesList(TitleMixin, ListView):
    model = models.Recipe
    template_name = 'core/recipes_list.html'
    context_object_name = 'recipes'
    title = 'База рецептов'
    form = forms.RecipeSearch()

    def get_queryset(self) -> list :
        name = self.request.GET.get('name')
        qs = models.Recipe.objects.all()
        for i in qs:
            calc_datatools.calculate_primecost(i)

        if name:
            return qs.filter(name__icontains=name)
        return qs

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.RecipeSearch(self.request.GET or None)
        context['request_name'] = self.request.GET.get('name',)
        return context


class ComponentsList(TitleMixin, ListView):
    model = models.Component
    template_name = 'core/components_list.html'
    context_object_name = 'components'
    title = 'База ингредиентов'

    def get_queryset(self) -> list:
        name = self.request.GET.get('name',)
        parent_components = list(filter(lambda x: x.parent, models.Component.objects.all()))
        qs = parent_components
        print(qs)
        if name:
            return qs.filter(name__icontains=name)
        return qs

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.ComponentSearch(self.request.GET or None)
        context['request'] = self.request.GET.get('name')
        return context


class ToolsList(TitleMixin, ListView):
    model = models.Tool
    template_name = 'core/tools_list.html'
    context_object_name = 'tools'
    title = 'База инструментов'

    def get_queryset(self):
        name = self.request.GET.get('name')
        parent_tools = models.Tool.objects.all()  # .filter(parent__iexact=True)
        qs = parent_tools
        if name:
            return qs.filter(name__icontains=name)
        return qs

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.ToolSearch(self.request.GET or None)
        context['request'] = self.request.GET.get('name')
        return context
# endregion


# region DetailViews
class RecipeDetail(DetailView):
    model = models.Recipe
    template_name = 'core/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs) -> dict:
        recipe = models.Recipe.objects.get(id=self.kwargs['pk'])
        calc_datatools.calculate_primecost(recipe)

        context = super().get_context_data(**kwargs)
        context['title'] = f'Рецепт «{recipe.name}»'
        context['primecost_str'] = \
            f'Себестоимость: {recipe.primecost} ({format(recipe.primecost/recipe.count, ".2f")} / 1 у. е.)'
        return context


class ComponentDetail(DetailView):
    model = models.Component
    template_name = 'core/component_detail.html'
    context_object_name = 'recipe_component'

    def get_context_data(self, **kwargs) -> dict:
        component = self.model.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['title'] = f"Ингредиент «{component.name}»"
        context['param1'] = ['Цена', component.price]
        if not component.parent:
            context['param2'] = ['Количество (у.е.)', component.count]
        return context


class ToolDetail(DetailView):
    model = models.Tool
    template_name = 'core/component_detail.html'
    context_object_name = 'recipe_tool'

    def get_context_data(self, **kwargs) -> dict:
        tool = self.model.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['title'] = f"Инструмент «{tool.name}»"
        context['param1'] = ['Цена', tool.cost]
        if not tool.parent:
            context['param2'] = ['Время применения (час)', tool.time]
        else:
            context['param2'] = ['Срок использования (мес.)', tool.usage]
        return context

# endregion


# region CreateViews
class ComponentCreate(TitleMixin, CreateView):
    title = 'Создание ингредиента'
    template_name = 'core/create_component.html'
    form_class = forms.CreateComponent
    success_url = reverse_lazy('core:components')


class ToolCreate(TitleMixin, CreateView):
    title = 'Создание инструмента'
    model = models.Tool
    template_name = 'core/create_tool.html'
    form_class = forms.CreateTool
    success_url = reverse_lazy('core:tools')


class RecipeCreate(TitleMixin, CreateView):
    title = 'Создание рецепта'
    model = models.Recipe
    template_name = 'core/create_recipe.html'
    form_class = forms.CreateRecipe

    def get_success_url(self, **kwargs):
        return reverse_lazy('core:recipe', kwargs={'pk': self.object.pk})


# region UpdateViews
class UpdateComponent(UpdateView):
    model = models.Component
    template_name = 'core/update_component.html'
    form_class = forms.CreateComponent
    success_url = reverse_lazy('core:components')


class UpdateTool(UpdateView):
    model = models.Tool
    template_name = 'core/update_tool.html'
    form_class = forms.CreateTool
    success_url = reverse_lazy('core:tools')


class UpdateRecipe(UpdateView):
    model = models.Recipe
    template_name = 'core/update_recipe.html'
    form_class = forms.CreateRecipe

    def get_success_url(self, **kwargs):
        return reverse_lazy('core:recipe', kwargs={'pk': self.object.pk})

# endregion


# region DeleteViews
class DeleteComponent(DeleteView):
    model = models.Component
    template_name = 'core/delete_component.html'
    success_url = reverse_lazy('core:components')


class DeleteTool(DeleteView):
    model = models.Tool
    template_name = 'core/delete_tool.html'
    success_url = reverse_lazy('core:tools')


class DeleteRecipe(DeleteView):
    model = models.Recipe
    template_name = 'core/delete_recipe.html'
    success_url = reverse_lazy('core:recipes')

# endregion
