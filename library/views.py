from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Algorithm, Category


class HomeView(ListView):
    template_name = 'library/home.html'
    allow_empty = True
    context_object_name = 'algorithms'

    def get_queryset(self):
        category_id = self.request.GET.get('category', '')
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            return category.algorithms.all()

        query = self.request.GET.get('search', '')
        if query:
            return Algorithm.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        else:
            return Algorithm.objects.all()


class AlgView(DetailView):
    model = Algorithm
    context_object_name = 'algorithm'
    template_name = 'library/alg_detail.html'


class CategoriesView(ListView):
    allow_empty = True
    context_object_name = 'categories'
    template_name = 'library/categories.html'

    def get_queryset(self):
        return Category.objects.annotate(algorithm_count=Count('algorithms')).order_by('-algorithm_count')
