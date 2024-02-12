// Функция для проверки, долистал ли пользователь до элемента
function isElementInViewport(el) {
    if (!el) {
        return false;
    }
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Функция для обработки прокрутки
function handleScroll() {
    var animatedGif = document.getElementById("animatedGif");

    // Если элемент существует и виден в окне просмотра
    if (isElementInViewport(animatedGif)) {
        // Задаем стиль анимации, чтобы начать ее заново
        animatedGif.style.animation = 'none';
        animatedGif.offsetHeight; /* это требуется для того, чтобы браузер обновил стиль перед добавлением нового значения */
        animatedGif.style.animation = null;
    }
}

// Слушатель события прокрутки
window.addEventListener("scroll", handleScroll);

// Инициализация проверки при загрузке страницы
handleScroll();
