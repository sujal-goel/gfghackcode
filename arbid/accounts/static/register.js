
function cardTransitions(clickedCard) {
    let cards = document.querySelectorAll(".cards");
    cards.forEach(card => {
        if (card.classList.contains("cardBlur") && card == clickedCard) {
            card.classList.remove("cardBlur");
        }
        if (card != clickedCard) {
            card.classList.add("cardBlur");
        }
    });
    setTimeout(() => {
        cards.forEach(card => {
            if (card.classList.contains("cardBlur")) {
                card.classList.remove("cardBlur");
            }
        });
    }, 5000);
}
let option
function toRegistrationPage(clickedBtn) {
       option = clickedBtn.classList[1];
        window.location.href = "registration.html";
}

export {option};