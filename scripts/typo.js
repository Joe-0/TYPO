//Timer code adapted from https://www.youtube.com/watch?v=R-7eQIHRszQ



//timer stuff by joe
/*const textDisplayElement = document.getElementById('textDisplay')
const testInputElement = document.getElementById('textInput')
const timeElapsedElement = document.getElementById('timeElapsed')

testInputElement.addEventListener('input',timePassed)



let startTime
function timePassed() {
    timeElapsedElement.innerText = 0
    startTime = new Date()
    setInterval(() => {
        timeElapsedElement.innerText = getTimerTime()
    }, 1000)
    getEndTime()
    testInputElement.removeEventListener('input',timePassed)
}

function getTimerTime() {
    return Math.floor((new Date() - startTime) / 1000)
}
let endTime

function getEndTime(){
    endTime = Math.floor((new Date() - startTime) / 1000)
    console.log(getTimerTime())
}

*/




var challengeText = getElementbyID(textDisplay.innerText);
var userText = getElementbyID(textInput.innerText);
//listens for inputs
typoInputElement.addEventListener('input', () => {
    const arrayChallenge = challengeText.querySelectorAll('span')
    const arrayInput = userText.value.split('')
    arrayChallenge.forEach((characterSpan, index) => {
        const character = arrayInput[index]
        if (character === characterSpan.innerText) {
            characterSpan.classList.add('correct')
            characterSpan.classList.remove('incorrect')
        } else {
            characterSpan.classList.remove('correct')
            characterSpan.classList.add('incorrect')
        }
    })

})
