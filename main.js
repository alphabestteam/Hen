const main_heading = document.getElementById("main-heading");
console.log(main_heading.id);

console.log(main_heading.className);

console.log(main_heading.classList);

console.log(main_heading.dataset)

console.log(main_heading.getAttribute("nonStandard"));

main_heading.classList.add("bg-lightcyan");
main_heading.classList.add("border");

console.log(main_heading.textContent);

console.log(main_heading.textContent.trim());

main_heading.textContent = "Hello there pearl!"

const lineBreak = document.createElement("br");
main_heading.appendChild(lineBreak);

const newSpan = document.createElement("span");
newSpan.textContent = "\nits me SpongeBob!";
main_heading.appendChild(newSpan);

console.log(main_heading);

const cloned = main_heading.cloneNode(true);

const subHeading = document.createElement("h2");

subHeading.textContent = "jellyfish hunting is the best!";

document.body.appendChild(subHeading);

const text = "Lorem ipsum dolor sit amet consectetur adipisicing elit.Labore eum, earum deserunt numquam quis explicabo. Delectusid, cum voluptate dicta aperiam sunt voluptatum quis eaquealiquam distinctio reiciendis iste minima?";

arrayText = text.split(" ");

const colors = ["red","orange","yellow","greenyellow","lightblue","mediumpurple"];

const getRandomColor=()=>{
    const randomIndex = Math.floor(Math.random() * colors.length);
    return colors[randomIndex];
}

const random_words = document.getElementById("random-words");

arrayText.forEach(word => {
    const span = document.createElement("span");
    const style = "background-color: " + getRandomColor();
    span.setAttribute("style", style);
    span.textContent = word;
    span.className = "random-word";
    random_words.appendChild(span);
});

const button = document.querySelector("button");

button.addEventListener("click", () => {
    const spans = random_words.querySelectorAll("span");
    spans.forEach(span => {
        const style = "background-color: " + randomRRGGBB();
        span.setAttribute("style", style);
    });
});

function randomRRGGBB() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
};