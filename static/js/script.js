function playGame() {
  const choices = ["rock", "paper", "scissors"];
  const userChoice = prompt(
    "Enter your choice (rock, paper, scissors):"
  ).toLowerCase();
  if (!choices.includes(userChoice)) {
    alert("Invalid choice! Please enter rock, paper, or scissors.");
    return;
  }

  const computerChoice = choices[Math.floor(Math.random() * choices.length)];
  let result = "";

  if (userChoice == computerChoice) {
    result = "It's a tie!";
  } else if (
    (userChoice == "rock" && computerChoice == "scissors") ||
    (userChoice == "paper" && computerChoice == "rock") ||
    (userChoice == "scissors" && computerChoice == "paper")
  ) {
    result = "You win!";
  } else {
    result = "You lose!";
  }

  alert(`You chose ${userChoice}, computer chose ${computerChoice}. ${result}`);
}
