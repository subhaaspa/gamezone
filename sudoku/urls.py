from django.urls import  path
from . import views

app_name = "sudoku"

urlpatterns = [
    path('<level>/',views.play_sudoku, name="playsudoku"),
    path('',views.play_sudoku, name="playsudoku")
]
