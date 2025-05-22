from django.shortcuts import render
from django.http import JsonResponse
from .game_logic import (
    initialize_game,
    bulls_and_cows,
    filter_possibilities,
    calculate_entropy,
    calculate_mutual_information,
)

# Initialize the game state globally.
game_state = initialize_game()


def game_view(request):
    """
    Handles game logic for Bulls and Cows via HTTP requests.
    
    - Supports POST requests for game actions such as guessing, replaying, or exiting.
    - GET requests render the initial game page.
    """
    global game_state  # Use the global game state to track across requests.

    if request.method == "POST":
        # Determine the action from the POST request (default is "guess").
        action = request.POST.get("action", "guess")

        # Action to reset the game.
        if action == "replay":
            game_state = initialize_game()  # Reset the game state.
            return JsonResponse({
                "message": "Game has been reset. You can start guessing!",
                "attempts": 0,
                "history": [],  # Clear the history of guesses.
            })

        # Action to exit the game.
        if action == "exit":
            game_state = initialize_game()  # Reset the game state for a clean exit.
            return JsonResponse({
                "message": "Thank you for playing Bulls and Cows! Goodbye!",
                "exit": True,  # Indicate to the client that the game session has ended.
            })

        # Handle the guessing action.
        guess = request.POST.get("guess")
        
        # Validate the guess:
        # - It must be a 4-digit number.
        # - All digits must be unique.
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            return JsonResponse({
                "error": "Invalid guess. Enter a 4-digit number with unique digits."
            })

        # Access the current secret and possibilities from the game state.
        secret = game_state["secret"]
        possibilities = game_state["possibilities"]

        # Compute Bulls and Cows for the guess.
        bulls, cows = bulls_and_cows(secret, guess)

        # Increment the attempt counter.
        game_state["attempts"] += 1

        # Update possibilities based on the current guess's outcome.
        game_state["possibilities"] = filter_possibilities(
            guess, bulls, cows, possibilities
        )

        # Calculate entropy and mutual information for the updated state.
        entropy = calculate_entropy(game_state["possibilities"])
        mutual_information = calculate_mutual_information(possibilities, guess)

        # Log the current guess and its results in the game history.
        game_state["attempts_history"].append({
            "guess": guess,
            "bulls": bulls,
            "cows": cows,
            "entropy": round(entropy, 2),
            "mutual_information": round(mutual_information, 2),
        })

        # Check if the player has guessed the secret number.
        if bulls == 4:
            return JsonResponse({
                "message": f"Congratulations! You've guessed the secret number {secret} in {game_state['attempts']} attempts. Would you like to play again?",
                "replay": True,  # Indicate that the game can be replayed.
                "history": game_state["attempts_history"],  # Send the attempt history.
            })

        # Respond with the results of the current guess.
        return JsonResponse({
            "guess": guess,
            "bulls": bulls,
            "cows": cows,
            "attempts": game_state["attempts"],
            "possibilities_count": len(game_state["possibilities"]),  # Remaining possibilities.
            "entropy": round(entropy, 2),  # Uncertainty of the current state.
            "mutual_information": round(mutual_information, 2),  # Information gained by the guess.
            "history": game_state["attempts_history"],  # Updated attempt history.
        })

    # Render the game HTML page for a GET request.
    return render(request, "game.html")
