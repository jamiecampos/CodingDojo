// For an additional challenge, add '-' signs to the bottom two percent of A, B,
// C and D scores, and + signs to the top two percent of B, C and D scores
// (sorry, Mr. Cerise never gives an A+). Given 88, console.log "Score: 88.
// Grade: B+". Given 61, log "Score: 61. Grade: D-".

function letterGrades(grade){
    if(grade > 91){
        console.log("Score: " + grade + ". Grade: A.")
    }else if(grade > 89){
        console.log("Score: " + grade + ". Grade: A-.")
    }else if(grade > 87){
        console.log("Score: " + grade + ". Grade: B+.")
    }else if(grade > 81){
        console.log("Score: " + grade + ". Grade: B.")
    }else if(grade > 79){
        console.log("Score: " + grade + ". Grade: B-.")
    }else if(grade > 77){
        console.log("Score: " + grade + ". Grade: C+.")
    }else if(grade > 71){
        console.log("Score: " + grade + ". Grade: C.")
    }else if(grade > 69){
        console.log("Score: " + grade + ". Grade: C-.")
    }else if(grade > 67){
        console.log("Score: " + grade + ". Grade: D+.")
    }else if(grade > 61){
        console.log("Score: " + grade + ". Grade: D.")
    }else if(grade > 59){
        console.log("Score: " + grade + ". Grade: D-.")
    }else{
        console.log("Score: " + grade + ". Grade: F.")
    }
}

letterGrades(91)
