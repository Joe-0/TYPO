var challengeText = getElementbyID(textDisplay.innerText);
var userText = getElementbyID(textInput.innerText);


//timer stuff by joe
const textDisplayElement = document.getElementById('textDisplay')
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
    testInputElement.removeEventListener('input',timePassed)
}

function getTimerTime() {
    return Math.floor((new Date() - startTime) / 1000)
}






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
