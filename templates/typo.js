//Timer code adapted from https://www.youtube.com/watch?v=R-7eQIHRszQ
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
