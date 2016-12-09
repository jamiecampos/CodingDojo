// This weekend, for a challenge, create a fill-in-the-blank quiz game. Ask the
// user's name, then refer to the user by name as you ask him/her a series of
// questions that you have stored in an array. Use the prompt() function to get
// each input from the user and compare it to the answer you expected. When the
// user enters "Q" (for quit), or perhaps when the user hits [Cancel], exit the
// game and print the statistics of the game to the console: user name, number
// of questions answered and questions correct.


function quizGame() {
    var correctAnswers = 0
    var incorrectAnswers = 0

    var quizQuestions = [", what is the capital city of Iowa?", ", what is the capital city of Illinois?", ", what is the capital city of Georgia?", ", what is the capital city of Kansas?", ", what is the capital city of Wisconsin?"]
    var quizAnswers = ["Des Moines", "Springfield", "Atlanta", "Topeka", "Madison"]

    var name = prompt("Hello, what is your name?");

    for(i = 0; i < 5; i++){
        var answer = prompt(name + quizQuestions[i])
        if(answer == quizAnswers[i]){
            correctAnswers += 1
        }else if(answer == "Q"){
            break;
        }else{
            incorrectAnswers += 1
        }

    }
    var questionsAnswered = correctAnswers + incorrectAnswers
    console.log("Name: " + name)
    console.log("Questions answered: " + questionsAnswered)
    console.log("Correct answers: " + correctAnswers)
}

quizGame()
