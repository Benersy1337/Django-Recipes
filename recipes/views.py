from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe
from django.db.models.query_utils import Q


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def category(request,category_id):

    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })
    
def recipe(request, id):
    
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
    
def search(request):
    
    if request.method == "POST":
        
        searched = request.POST['searched']
        
        recipe = Recipe.objects.filter(title__contains=searched, is_published=True)

        return render(request, 
                    'recipes/pages/searched.html', 
        {'searched':searched,
         'recipes': recipe,
        })
        
    else:
        return render(request, 
                'recipes/pages/searched.html', 
    {})
    
    