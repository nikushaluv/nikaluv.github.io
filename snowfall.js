document.addEventListener("DOMContentLoaded", function() {
    const numberOfSnowflakes = 50;
    const snowfallContainer = document.body;

    for (let i = 0; i < numberOfSnowflakes; i++) {
        createSnowflake();
    }

    function createSnowflake() {
        const snowflake = document.createElement("div");
        snowflake.className = "snowflake";
        snowfallContainer.appendChild(snowflake);

        const randomSize = Math.random() * 3 + 1;
        snowflake.style.width = `${randomSize}px`;
        snowflake.style.height = `${randomSize}px`;

        const startPosition = Math.random() * window.innerWidth;
        snowflake.style.left = `${startPosition}px`;

        const animationDuration = Math.random() * 3 + 2;
        snowflake.style.animation = `fall ${animationDuration}s linear infinite`;

        // Опционально: установите начальные координаты по вертикали
        const startVerticalPosition = Math.random() * window.innerHeight;
        snowflake.style.top = `${startVerticalPosition}px`;

        // snowflake.style.position = "fixed"; // Уберем это свойство
    }
});
