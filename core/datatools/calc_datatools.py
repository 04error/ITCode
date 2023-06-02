from core import models


def calculate_primecost(recipe: models.Recipe):
    primecost = 0
    if recipe.components:
        for i in recipe.components.all():
            primecost += update_component(i).cost

    if recipe.tools:
        for i in recipe.tools.all():
            primecost += update_tool(i).depreciation

    recipe.primecost = float(format(primecost, '.2f'))
    recipe.save()
    return


def update_component(component: models.Component) -> models.Component:
    parent = models.Component.objects.get(id=component.parent_id)

    if component.price != parent.price:
        component.price = parent.price

    component.cost = float(format(component.price * component.count, '.2f'))
    component.save()
    return component


def update_tool(tool: models.Tool) -> models.Tool:
    parent = models.Tool.objects.get(id=tool.parent_id)

    if tool.cost != parent.cost:
        tool.cost = parent.cost
    if tool.usage != parent.usage:
        tool.usage = parent.usage

    tool.depreciation = float(format(tool.cost / 12 / 30 / 24 * tool.usage * tool.time, '.2f'))
    tool.save()
    return tool
