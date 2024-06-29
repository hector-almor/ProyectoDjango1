from django.urls import path 
from .views import (
    HomePageView,
    CategoriaCreateView,
    CategoriaListView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    ProductoCreateView,
    ProductoListView,
    ProductoUpdateView,
    ProductoDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("categoria/create/", CategoriaCreateView.as_view(), name="categoria_create"),
    path("categoria/list/", CategoriaListView.as_view(), name="categoria_list"),
    path(
        "categoria/update/<int:pk>/",
        CategoriaUpdateView.as_view(),
        name="categoria_update",
    ),
    path(
        "categoria/delete/<int:pk>/",
        CategoriaDeleteView.as_view(),
        name="categoria_delete",
    ),
    path("producto/create/", ProductoCreateView.as_view(), name="producto_create"),
    path("producto/list/", ProductoListView.as_view(), name="producto_list"),
    path(
        "producto/update/<int:pk>/",
        ProductoUpdateView.as_view(),
        name="producto_update",
    ),
    path(
        "producto/delete/<int:pk>/",
        ProductoDeleteView.as_view(),
        name="producto_delete",
    ),
]