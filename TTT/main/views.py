from django.shortcuts import render
from django.http import HttpResponse
from .game import TicTacToe
from .AI import AI 

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})



ai = AI()
game = TicTacToe(ai)
played_moves = []

def process_move(request):
   
    if request.method == "POST":
        if "cell_value" in request.POST:
            # User clicked a cell button, process the move and update game state
            cell_value = request.POST.get("cell_value")

            if int(cell_value) in played_moves:
                return HttpResponse("Invalid move", status=400)
            played_moves.append(cell_value)

            game.play(cell_value)
            updated_game_data = game.get_board()
            

            
            return render(request, "main/base.html", {"game_data": updated_game_data})

        elif "restart_button" in request.POST:
            # User clicked the "Restart" button, handle the restart logic
            # For example, reset the game state to its initial state
            # Then, return a response to the game template
            initial_game_data = {
                "cell_0": "",  # An empty cell
                "cell_1": "",
                "cell_2": "",
                "cell_3": "",
                "cell_4": "",
                "cell_5": "",
                "cell_6": "",
                "cell_7": "",
                "cell_8": "",
                "winner": "",  # No winner at the beginning
            }

            return render(request, "main/base.html", {"game_data": initial_game_data})

    return HttpResponse("Invalid request method", status=400)

