# 🐄🐂 Cows and Bulls - A Number Guessing Game Using Entropy and Mutual Information

## 📌 Overview

**Cows and Bulls** is a classic number guessing game reimagined with concepts from information theory, such as **entropy** and **mutual information**, to make intelligent and efficient guesses.

The project was developed as part of the **Mathematical Foundations of Data Science** course by **Nikhitha Nagalla**.

---

## 🎯 Objective

Create a web-based version of the Cows and Bulls game where the computer generates a secret number, and the player guesses it using clues (cows and bulls). The game highlights how **entropy-based** strategies can help reduce guesswork and improve decision-making.

---

## 🧠 Game Concept

- **Bulls**: Correct digit in the correct position  
- **Cows**: Correct digit in the wrong position

The player guesses a number, and the system provides feedback in terms of cows and bulls. Using this feedback, the player can reduce uncertainty and home in on the correct number using information-theoretic principles.

---

## 📈 Information Theory Application

### Entropy
Entropy measures the uncertainty in the system. In the context of the game:
- It helps narrow down the potential solution space.
- Guides efficient guessing rather than random choices.
- Reduces average guesses needed.

### Mutual Information
Mutual information helps in evaluating how much a guess reduces the overall uncertainty.

---

## 💡 Benefits of Entropy-Based Guessing

1. **Efficient Guessing**: Reduces the number of attempts.
2. **Avoid Random Guesses**: Informed choices narrow down solutions faster.
3. **Handles Complexity**: Suitable for more difficult versions with large solution spaces.

---

## ⚠️ Limitations

- Computational cost in evaluating all possible feedback outcomes.
- Misinterpretation of feedback may lead to inefficient updates.
- Doesn’t always guarantee the quickest path in every single game.
- Might reduce creative elements of gameplay.

---

## 🛠️ Technology Stack

- **Programming Language**: Python
- **Interface**: Web-based frontend using HTML/CSS/JavaScript
- **Backend Logic**: Entropy and mutual information calculations for intelligent guessing

---

## 🌐 How to Play

1. Computer generates a secret number.
2. Player enters a guess.
3. The game returns number of cows and bulls.
4. Player uses the feedback to make better guesses.
5. Game ends when the secret number is correctly guessed.

---

## 🚀 Future Enhancements

- Improved UI/UX with animations.
- Add session management (pause/play).
- Support for 5-digit or more complex variants.
- Timer-based challenges for added difficulty.

---

## 🧾 Conclusion

This project showcases how mathematical foundations like **entropy** and **mutual information** can be applied to improve strategic thinking in games. It transforms a simple number guessing game into a powerful demonstration of information theory in action.

---

## 👤 Author

**Nikhitha Nagalla**  
Mathematical Foundations of Data Science  
12/01/2024

