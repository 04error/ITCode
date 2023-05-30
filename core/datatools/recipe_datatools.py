from core import models


def calculate_primecost(recipe):
    primecost = 0

    if recipe.components:
        for i in recipe.components.all():
            parent = models.Component.objects.get(id=i.parent_id)

            if i.price != parent.price:
                i.price = parent.price

            i.cost = float(format(i.price * i.count, '.2f'))
            primecost += i.cost
            i.save()

    if recipe.tools:
        for i in recipe.tools.all():
            parent = models.Tool.objects.get(id=i.parent_id)

            if i.cost != parent.cost:
                i.cost = parent.cost
            if i.usage != parent.usage:
                i.usage = parent.usage

            i.depreciation = float(format(i.cost / 12 / 30 / 24 * i.usage * i.time, '.2f'))
            primecost += i.depreciation
            i.save()

    recipe.primecost = float(format(primecost, '.2f'))
    recipe.save()
    return
