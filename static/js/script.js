player_name = prompt("enter your name");
alert(".");
player_guess = prompt(
  "Scissors, Paper, or Rock (make sure the first letter is caps)"
);
computer_guess = randomintFrominterval(1, 3);
if (player_guess == computer_guess) {
  document.getElementById("user_feedback").innerHTML = "<em>Correct</em>";
} else {
  document.getElementById("userfeedback").innerHTML =
    "u got it wrong u suck" + "the computer guessed" + computer_guess;
}
function randomintFrominterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
