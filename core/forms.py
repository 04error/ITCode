from django import forms
from core import models


# region SearchForms
class RecipeSearch(forms.Form):

    name = forms.CharField(label='Поиск рецепта', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))


class ComponentSearch(forms.Form):
    name = forms.CharField(label='Поиск ингредиента', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))


class ToolSearch(forms.Form):
    name = forms.CharField(label='Поиск инструмента', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
# endregion


# region CreateForms
class CreateComponent(forms.ModelForm):
    price = forms.FloatField(label="Цена", min_value=0.1)

    class Meta:
        model = models.Component
        fields = ('name', 'unit', 'price')

    def clean_name(self) -> str:
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError('Имя не может быть числом!')
        return name

    def clean_unit(self) -> str:
        unit = self.cleaned_data['unit']
        if unit.isdigit():
            raise forms.ValidationError('Введите буквенную единицу измерения!')
        return unit


class CreateTool(forms.ModelForm):
    name = forms.CharField(label='Название', min_length=2)
    cost = forms.FloatField(label="Стоимость", min_value=1)
    usage = forms.IntegerField(label="Срок использования (месяцев)", min_value=1)
    # time = forms.FloatField(label="Время применения (часов)", min_value=0.1)

    class Meta:
        model = models.Tool
        fields = ('name', 'cost', 'usage',)

    def clean_name(self) -> str:
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError('Название не может быть числом!')
        return name


'''
class ComponentMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name} (Цена: {obj.price})'


class ToolMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name} (Стоимость: {obj.cost}, срок использования: {obj.usage})'
'''


class CreateRecipe(forms.ModelForm):
    # components = ComponentMultipleChoiceField(models.Component.objects.filter(parent=True).order_by('name'))
    # tools = ToolMultipleChoiceField(models.Tool.objects.filter(parent=True).order_by('name'))
    name = forms.CharField(label='Название', min_length=2)
    description = forms.CharField(label='Описание', widget=forms.Textarea, required=False)

    class Meta:
        model = models.Recipe
        fields = ('name', 'description', 'count')

    def clean_name(self) -> str:
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError('Название не может быть числом!')
        return name
# endregion
