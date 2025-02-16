function generateRandomPixels(containerId) {
    const container = document.getElementById(containerId);
    const width = container.clientWidth;
    const height = container.clientHeight;
    
    for (let i = 0; i < 80; i++) {
        const x = Math.random() * width;
        const y = Math.random() * height;
        const pixel = document.createElement('div');
        pixel.className = 'pixel';
        pixel.style.left = x + 'px';
        pixel.style.top = y + 'px';
        pixel.style.animationDelay = (Math.random() * 2) + 's';
        container.appendChild(pixel);
    }
}

generateRandomPixels('left_pixels');
generateRandomPixels('right_pixels');