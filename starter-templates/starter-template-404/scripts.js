document.addEventListener('DOMContentLoaded', () => {
  const bubbles = document.querySelectorAll('.bubble');
  
  bubbles.forEach(bubble => {
    // Generate random values for the bubbles
    const floatAmount = Math.random() * 30 + 20; // Random value between 20 and 50 pixels
    const duration = Math.random() * 15 + 10; // Random duration between 10 and 25 seconds

    // Apply random movement to each bubble
    bubble.style.setProperty('--float-amount', `${floatAmount}px`);
    bubble.style.setProperty('--duration', `${duration}s`);
  });
});
