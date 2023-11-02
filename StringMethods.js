story = "           Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master.\nPo'sdream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages.            "

const makeParegrath = (story) => story.split(".");

const movieToFilm = (story) => story.replace("movie","film");

const allPandaToBear = (story) => story.replace(/Panda/g,"Bear");

const upperStory = (story) => story.toUpperCase();

const lowerStroy = (story) => story.toLowerCase();

const findFirstPo = (story) => story.indexOf("Po");

const fromPoToend = (story) => {
    const startIndex = findFirstPo(story);
    return story.slice(startIndex);
}

const deleteWhiteSpace = (story) => story.trim();

const fromPoToEndParagrath = (story) => {
    const startIndex = findFirstPo(story);
    const endIndex = story.indexOf(".",startIndex);
    return story.substring(startIndex,endIndex+1);
}

const splitWords = (story) => {
    withOutSpace = deleteWhiteSpace(story);
    return withOutSpace.split(" ");
}

const checkend = (story) => story.trim().endsWith("ages.");

const addLine = (story) => story + " is one of my favorite movies!";
