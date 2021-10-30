/*
 This javascript file contains code adapted from https://github.com/WebDevSimplified/JS-Speed-Typing-Game
 written by WebDevSimplified
 */

// mkae variable holding required html elements
const textDisplayElement = document.getElementById('textDisplay')
const textInputElement = document.getElementById('textInput')
const timeElapsedElement = document.getElementById('timeElapsed')
const WPMelement = document.getElementById('WPM')
const CPMelement = document.getElementById(('CPM'))
const accuracyElement = document.getElementById('accuracy')

// get the number of words and character in the challenge text
const num_words = textDisplayElement.innerText.split(' ').length
const num_char = textDisplayElement.innerText.length


let time = 0
let Interval
let count = 1
let strt = textDisplayElement.innerHTML
let strin_len


textDisplayElement.innerHTML = ''
strt.split('').forEach(char => {
    const charSpan = document.createElement('span')
    charSpan.innerText = char
    textDisplayElement.appendChild(charSpan)

})

textInputElement.addEventListener('input', () => {
    let correct = false
    strin_len = textInputElement.value.length
    if (count === 1) {
        starttimer()
        count = 2
    }

    if (strin_len === num_char) {
        correct = true
    }

    if (correct) endchallenge()

    const arrayText = textDisplayElement.querySelectorAll('span')
    const arrayInText = textInputElement.value.split('')
    arrayText.forEach((characterSpan, index) => {
        const character = arrayInText[index]
        if (character == null) {
            characterSpan.classList.remove('correct')
            characterSpan.classList.remove('incorrect')
        } else if (character === characterSpan.innerText) {
            characterSpan.classList.add('correct')
            characterSpan.classList.remove('incorrect')
        } else {
            characterSpan.classList.remove('correct')
            characterSpan.classList.add('incorrect')
        }

    })

})


function timePassed() {
    timeElapsedElement.innerText = 0
    time++
    timeElapsedElement.innerText = time

}

function starttimer() {
    Interval = setInterval(timePassed, 1000)
}


function endchallenge() {
    clearInterval(Interval);
    let count_correct = 1
    let end_time = timeElapsedElement.innerText / 60
    let wpm = Math.floor(num_words / end_time)
    let cpm = Math.floor(num_char / end_time)
    WPMelement.innerHTML = wpm
    CPMelement.innerHTML = cpm
    const arr_text = textDisplayElement.querySelectorAll('span')
    arr_text.forEach((charSpan, index) => {
        if (charSpan.classList.contains('correct')) {
            count_correct++
        }
    })
    console.log(num_char, count_correct)
    let accuracy = (count_correct / num_char) * 100
    accuracyElement.innerHTML = accuracy.toFixed(2)

}




