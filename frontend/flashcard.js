const flashcard = document.getElementById("flashcard");

for (let i = 0; i < flashcards.length; i++) {
    const flashcard = flashcards[i];
    flashcard.addEventListener("click", function() {
        flashcard.classList.toggle("flip");
    });
}
