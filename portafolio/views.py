from django.views.generic import TemplateView

from .models import Categoria, Producto

from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)


class HomePageView(TemplateView):
    template_name = "home.html"


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "categoria_create.html"
    fields = [
        "nombre",
        "descripcion",
    ]
    success_url = "/"


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria_list.html"
    context_object_name = "categorias"


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "categoria_update.html"
    fields = [
        "nombre",
        "descripcion",
    ]
    success_url = "/"


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "categoria_delete.html"
    success_url = "/"


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto_create.html"
    fields = [
        "nombre",
        "descripcion",
        "precio",
        "disponibilidad",
        "categoria",
    ]
    success_url = "/"


class ProductoListView(ListView):
    model = Producto
    template_name = "producto_list.html"
    context_object_name = "productos"


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto_update.html"
    fields = [
        "nombre",
        "descripcion",
        "precio",
        "disponibilidad",
        "categoria",
    ]
    success_url = "/"


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto_delete.html"
    success_url = "/"