const textDisplayElement = document.getElementById('textDisplay')
const testInputElement = document.getElementById('textInput')
const timeElapsedElement = document.getElementById('timeElapsed')

testInputElement.addEventListener('input', timePassed)


let startTime

function timePassed() {
    timeElapsedElement.innerText = 0
    startTime = new Date()
    setInterval(() => {
        timeElapsedElement.innerText = getTimerTime()
    }, 1000)
    getEndTime()
    testInputElement.removeEventListener('input', timePassed)
}

function getTimerTime() {
    return Math.floor((new Date() - startTime) / 1000)
}

let endTime

function getEndTime() {
    endTime = Math.floor((new Date() - startTime) / 1000)
    console.log(getTimerTime())
}


