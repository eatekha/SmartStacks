// flip.js
document.querySelectorAll('.flashcard').forEach(function (card) {
    card.addEventListener('click', function () {
        card.classList.toggle('flipped');
    });
});
