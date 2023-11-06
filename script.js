const quotes = [
    "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
    "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
    "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
    "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
    "The inner machinations of my mind are an enigma. - Patrick Star",
    "I can't hear you, it's too dark in here! - Patrick Star",
    "I'm ugly and I'm proud! - SpongeBob SquarePants",
    "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
    "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
    "Is mayonnaise an instrument? - Patrick Star",
    "Can you give SpongeBob his brain back? - Patrick Star",
    "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
    "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
    "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
    "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
    "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
    "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
    "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
    "SpongeBob: Can I be excused for the rest of my life?",
    "SpongeBob: I'm not just ready, I'm ready Freddy!",
    "SpongeBob: You don't need a license to drive a sandwich.",
    "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
    "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
    "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
    "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
];
  
const inputElement = document.getElementById("input");
const startButton = document.getElementById("start-btn");
inputElement.disabled = true; 
let seconds = 0;
let intervalId;



function getRandomQuote() {
    const randomSentence = Math.floor(Math.random()* quotes.length);
    return quotes[randomSentence];
}


function startGame() {
    const sentence = getRandomQuote();
    typeSentence = document.getElementById("quote");
    const sentence_length = sentence.length;

    for (let i = 0; i < sentence_length; i++) {
        const charSpan = document.createElement("span");
        charSpan.textContent = sentence[i];
        typeSentence.appendChild(charSpan);
    }
}

function checkInput() {
    const input = document.getElementById("input");
    const input_text = input.value;
    const typeSentence = document.getElementById("quote");
    const spanElements = typeSentence.querySelectorAll("span");
    for(let i =0;i<input_text.length;i++){
        const inputChar = input_text[i];
        const spanChar = spanElements[i].textContent;

        if (inputChar === spanChar) {
            spanElements[i].classList.add("correct");
            spanElements[i].classList.remove("incorrect");
        } else {
            spanElements[i].classList.add("incorrect");
            spanElements[i].classList.remove("correct");
        }
    }
    if(input_text.length === spanElements.length){
        input.removeEventListener("input", checkInput);
        startButton.removeEventListener("click", startButtonClickHandler);
        const inputElement = document.getElementById("input");
        inputElement.disabled = true;
        clearInterval(intervalId);
        endGame()  
    }
    for (let i = input_text.length; i < spanElements.length; i++) {
        spanElements[i].classList.remove("correct", "incorrect");
    }
}

function accuracy(str) {
    const spanElements = str.querySelectorAll("span");
    let mistakes = 0;
    spanElements.forEach((span) => {
        if (span.classList.contains("incorrect")) {
            mistakes += 1;
        }
    });
    const totalSpans = spanElements.length;
    const correctSpans = totalSpans - mistakes;
    const accuracyPercentage = (correctSpans / totalSpans) * 100;

    return accuracyPercentage.toFixed(2);
}

function endGame() {
    const typeSentence = document.getElementById("quote");
    const result = document.getElementById("result");
    const finalTime = document.getElementById("timer") ;


    const timeSpan = document.createElement("p");
    const wordSpan = document.createElement("p");
    const speedSpan = document.createElement("p");
    const presentSpan = document.createElement("p");


    const countWords = typeSentence.textContent.split(" ");
    wordSpan.textContent = "you type "+ countWords.length + " words";
    timeSpan.textContent = "you finish in "+finalTime.textContent+" seconds";
    const timeInSeconds = parseFloat(finalTime.textContent);
    const speed = (countWords.length/timeInSeconds)*60;
    speedSpan.textContent = "your speed "+speed.toFixed(2) +"";
    const present = accuracy(typeSentence);
    presentSpan.textContent = "you right in "+ present + " accuracy";


    result.appendChild(timeSpan);
    result.appendChild(wordSpan);
    result.appendChild(speedSpan);
    result.appendChild(presentSpan);
}


function startButtonClickHandler() {
    inputElement.disabled = false;
    inputElement.focus();
    const timerElement = document.getElementById("timer");
    let startTime = performance.now();
    intervalId = setInterval(function () {
        let currentTime = performance.now();
        let elapsedTime = currentTime - startTime;
        seconds = Math.floor(elapsedTime / 1000);
        timerElement.textContent = seconds;
    }, 1000);
}

startButton.addEventListener("click", startButtonClickHandler);
startGame();
document.getElementById("input").addEventListener("input",checkInput);