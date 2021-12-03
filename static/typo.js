/*
 This javascript file contains code adapted from https://github.com/WebDevSimplified/JS-Speed-Typing-Game
 written by WebDevSimplified
 Code from this source was used in changing the color and styling of the challenge text as users input text into the input box.
*/

// make variable holding required html elements
const textDisplayElement = document.getElementById('textDisplay')
const textInputElement = document.getElementById('textInput')
const timeElapsedElement = document.getElementById('timeElapsed')
const WPMelement = document.getElementById('WPM')
const AWPMelement = document.getElementById(('AWPM'))
const accuracyElement = document.getElementById('accuracy')
const alertElement = document.getElementById('alert_box')
const timeElement = document.getElementById('timetrack')
const session_element = document.getElementById('session_log')
// get the number of words and character in the challenge text
const num_words = textDisplayElement.innerText.split(' ').length
const num_char = textDisplayElement.innerText.length
const session_val = session_element.value

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

function ready() {
    textInputElement.addEventListener('input', text_color)
}

function text_color() {
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

}


function timePassed() {
    timeElapsedElement.innerText = 0
    time++
    timeElapsedElement.innerText = (time/100).toFixed(2)
}

function starttimer() {
    Interval = setInterval(timePassed, 10)
}


function endchallenge() {
    clearInterval(Interval);
    alertElement.innerHTML = "Typing Test Comlpeted! If you wish to test again, then click the restart button"
    textInputElement.removeEventListener('input', text_color)
    textInputElement.disabled = true
    let count_correct = 1
    let end_time = timeElapsedElement.innerText / 60
    let wpm = (num_words / end_time)
    WPMelement.innerHTML = wpm.toFixed(0)
    const arr_text = textDisplayElement.querySelectorAll('span')
    arr_text.forEach((charSpan, index) => {
        if (charSpan.classList.contains('correct')) {
            count_correct++
        }
    })
    if (count_correct ==1){
        count_correct= 0
    }
    console.log(count_correct)
    console.log(num_char)
    let accuracy = (count_correct / num_char) * 100
    accuracyElement.innerHTML = accuracy.toFixed(1)
    let accurate_WPM = (wpm * accuracy)/100
    AWPMelement.innerHTML = accurate_WPM.toFixed(0)


    if (session_val) {
        const user_id = document.getElementById('user_id').value
        const user_name = document.getElementById('user_name').value
        var http = new XMLHttpRequest();
        var url = '/check_highscore';
        const params = 'highscore=' + AWPMelement.innerHTML +"&user_id="+user_id;
        http.open('POST', url, true);
        http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        http.send(params);

        const d = new Date()
        const day = d.getDate()
        const month = d.getMonth() +1
        const year = d.getFullYear()
        const date = month+'/'+day+'/'+year

        var http2 = new XMLHttpRequest();
        var url2 = '/attempts';
        const params2 = 'wpm='+ WPMelement.innerHTML +'&acc='+accuracyElement.innerHTML+'&acc_wpm=' + AWPMelement.innerHTML +"&user_name="+user_name+"&date="+date;
        http2.open('POST', url2, true);
        http2.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        http2.send(params2)
    }
}

document.addEventListener("DOMContentLoaded",ready)



