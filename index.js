document.addEventListener('DOMContentLoaded', function(){
    let correct = document.querySelector('.correct');
    correct.addEventListener('click', function(){
        correct.style.backgroundColor = "green";
        document.querySelector('#feedback').innerHTML = "correct!"
    });

    let incorrects = document.querySelectorAll('.multi');
    for(let i of incorrects){
        i.addEventListener('click', function(){
            i.style.backgroundColor = "red";
            i.style.color = "white";
            document.querySelector('#feedback').innerHTML = "Incorrect"
        })
    };


    let checkAnswer = document.getElementById("checkAnswer")

    checkAnswer.onclick = function(){
        let q2 = document.getElementById("q2").value
        if (q2 === "India"){
            checkAnswer.style.backgroundColor ="green"
            checkAnswer.style.color = "white"
        }
        else{
            checkAnswer.style.backgroundColor = "red"
            checkAnswer.style.color = "white"
        }

    };

})