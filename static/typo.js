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
const alertElement = document.getElementById('alert_alert')
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



/// make the text display empty
textDisplayElement.innerHTML = ''

/// for each character in the challenge text. make span tag for rach element so we can address each elements styling separately
strt.split('').forEach(char => {
    const charSpan = document.createElement('span')
    charSpan.innerText = char
    textDisplayElement.appendChild(charSpan)

})

/// listen for inputs in the inputbox
function ready() {
    textInputElement.addEventListener('input', text_color)
}

/// function that changes the styling of each character in the text based on the users input
function text_color() {
    let correct = false

    /// get the number of character in the challenge text
    strin_len = textInputElement.value.length

    /// this is used to trigger the start timer function just once
    if (count === 1) {
        starttimer()
        count = 2
    }

    /// if number of character in the input box equals the number of character in the challenge text, then set correct to true
    if (strin_len === num_char) {
        correct = true
    }

    /// store all the spans with the character in the challenge text an array
    const arrayText = textDisplayElement.querySelectorAll('span')

    /// store all the character in the input box so far in an array by splitting at each character
    const arrayInText = textInputElement.value.split('')

    /// loop over the character spans
    arrayText.forEach((characterSpan, index) => {
        const character = arrayInText[index]

        /// if that character has not been input yet, then let the span for that character remain yellow i.e don't change its color
        /// this is done by removing all classes from it
        if (character == null) {
            characterSpan.classList.remove('correct')
            characterSpan.classList.remove('incorrect')
        /// if that character in the input equals the corresponding character in the challenge text, then that character is correct
        } else if (character === characterSpan.innerText) {
            characterSpan.classList.add('correct')
            characterSpan.classList.remove('incorrect')
        /// else that character is incorrect
        } else {
            characterSpan.classList.remove('correct')
            characterSpan.classList.add('incorrect')
        }

    })
    /// if correct is true. i.e number of input characters equals number of character in the challenge, the triggger the endchallenge function.
    if (correct) endchallenge()

}

/// this function increments the timer
function timePassed() {
    timeElapsedElement.innerText = 0
    time++
    /// divide the time values by 100 to convert each 10 miliseconds to seconds
    timeElapsedElement.innerText = (time/100).toFixed(2)
}

/// this executes the timepassed function every 10 miliseconds
function starttimer() {
    Interval = setInterval(timePassed, 10)
}


function endchallenge() {

    /// clear the interval which stops the timer
    clearInterval(Interval);

    /// flash a message indicating that the typing challenge has ended
    alertElement.innerHTML = "Typing Test Comlpeted! If you wish to test again, then click the restart button"

    /// remove the input event listerner and disable the input box
    textInputElement.removeEventListener('input', text_color)
    textInputElement.disabled = true

    /// calculate the wpn by dividing the number of words in the text by the time passed in minutes
    let count_correct = 0
    let end_time = timeElapsedElement.innerText / 60
    let wpm = (num_words / end_time)

    /// display wpm on the webpage
    WPMelement.innerHTML = Math.floor(wpm)

    /// grab all the span the have the character for the challenge text
    const arr_text = textDisplayElement.querySelectorAll('span')
    arr_text.forEach((charSpan, index) => {

        /// if that span has the "correct" class then increment the count_correct timer
        /// which just stores the number of characters that were input correctly
        if (charSpan.classList.contains('correct')) {
            count_correct++
        }
    })

    /// divide count_correct by the total number of character in the challenge texts. multiply this by 100 to get a
    /// percentage accuracy of the correctness of the input compared to the challenge text and display it
    let accuracy = (count_correct / num_char) * 100
    accuracyElement.innerHTML = accuracy.toFixed(1)

    /// calculate the actual wpm and display it
    let accurate_WPM = (wpm * accuracy)/100
    AWPMelement.innerHTML = Math.floor(accurate_WPM)

    /// the session_val is a bool which tells us if a user is logged in or not
    if (session_val) {

        /// if they are logged in then get their id and username and send and ajax request to the which trigger the check_highscore() function in flask
        const user_id = document.getElementById('user_id').value
        const user_name = document.getElementById('user_name').value
        var http = new XMLHttpRequest();
        var url = '/check_highscore';

        /// send the score of the attempt and the logged in users id with the request
        const params = 'highscore=' + AWPMelement.innerHTML +"&user_id="+user_id;
        http.open('POST', url, true);
        http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        http.send(params);

        /// get the current date
        const d = new Date()
        const day = d.getDate()
        const month = d.getMonth() +1
        const year = d.getFullYear()
        const date = month+'/'+day+'/'+year

        /// send another ajax request that triggers the addAttempts() function in flask which add all attempts to the attempts database
        var http2 = new XMLHttpRequest();
        var url2 = '/attempts';

        /// send all the results of the attemmpt and it date with the request
        const params2 = 'wpm='+ WPMelement.innerHTML +'&acc='+accuracyElement.innerHTML+'&acc_wpm=' + AWPMelement.innerHTML +"&user_name="+user_name+"&date="+date;
        http2.open('POST', url2, true);
        http2.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        http2.send(params2)
    }
}

/// execute the ready function only after the DOM has loaded
document.addEventListener("DOMContentLoaded",ready)



