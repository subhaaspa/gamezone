from django.urls import  path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "sudoku"

# urlpatterns = [
#     path('<level>/',views.play_sudoku, name="playsudoku"),
#     path('',views.play_sudoku, name="playsudoku")
# ]

urlpatterns = [
    path('<level>/',login_required(views.SudokuView.as_view()), name="playsudoku"),
    path('',login_required(views.SudokuView.as_view()), name="playsudoku")
]
