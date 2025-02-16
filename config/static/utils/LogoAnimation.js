const hackerText = document.getElementById('logo');
const originalText = hackerText.textContent;
const chars = '01';

let interval;
let iterations = 0;

function startHackerEffect() {
    interval = setInterval(() => {
        const updatedText = originalText.split('').map((char, index) => {
            if (index < iterations) {
                return originalText[index];
            }
            const randomChar = chars[Math.floor(Math.random()*chars.length)];
            return `<span class="digit">${randomChar}</span>`;
        }).join('');

        hackerText.innerHTML = updatedText;

        if (iterations >= originalText.length) {
            clearInterval(interval);
            setTimeout(startHackerEffect, 1000);
            iterations = 0;
        } else {
            iterations += 1 / 3;
        }
    }, 60);
}

window.onload = startHackerEffect;