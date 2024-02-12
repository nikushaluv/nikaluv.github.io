document.addEventListener("DOMContentLoaded", function() {
    // Получаем элементы
    var albumBtn = document.getElementById("albumBtn");
    var albumModal = document.getElementById("albumModal");
    var closeBtn = document.getElementById("closeBtn");
    var images = document.querySelectorAll("#albumModal .modal-content img");
    var albumText = document.getElementById("albumText");

    // Функция для закрытия оригинального изображения
    function closeOriginalImage() {
        resetAlbumContent();
    }
    // Обработчик события для закрытия альбома при клике на пустое место
    albumModal.onclick = function (event) {
        if (event.target === albumModal) {
            albumModal.style.display = "none";
            albumText.style.display = "none";
            resetAlbumContent(); // Сброс содержимого альбома
        }
    };

    // Добавляем обработчик события для кнопки закрытия оригинала
    var closeOriginalBtn = document.querySelector("#albumModal .close");
    if (closeOriginalBtn) {
        closeOriginalBtn.onclick = closeOriginalImage;
    }

    // Обработчик события для открытия альбома
    albumBtn.onclick = function() {
        albumModal.style.display = "block";
        albumText.style.display = "block";
    };

    // Обработчик события для закрытия альбома
    closeBtn.onclick = function() {
        albumModal.style.display = "none";
        albumText.style.display = "none";
        resetAlbumContent(); // Сброс содержимого альбома
    };

    // Сохраняем исходное содержимое всплывающего окна
    var originalContent;

    // Функция для сброса содержимого альбома
    function resetAlbumContent() {
        // Проверяем наличие оригинального содержимого
        if (originalContent) {
            albumModal.innerHTML = originalContent;
    
            // Привязываем обработчики событий для изображений
            images = document.querySelectorAll("#albumModal .modal-content img");
            images.forEach(function (newImage) {
                newImage.onclick = openOriginalImage;
            });
    
            // Добавляем обработчик события для кнопки закрытия альбома
            closeBtn = document.getElementById("closeBtn");
            closeBtn.onclick = function () {
                albumModal.style.display = "none";
                albumText.style.display = "none";
                resetAlbumContent(); // Сброс содержимого альбома
            };
    
            // Сбрасываем переменную originalContent после восстановления
            originalContent = null;
    
            // Проверяем наличие кнопки закрытия и добавляем обработчик события
            var closeOriginalBtn = document.querySelector("#albumModal .close");
            if (closeOriginalBtn) {
                closeOriginalBtn.onclick = function () {
                    // Сбрасываем содержимое альбома при закрытии оригинала
                    resetAlbumContent();
                };
            }
        }
    
        // Добавляем обработчик события для кнопки закрытия альбома
        closeBtn = document.getElementById("closeBtn");
        closeBtn.onclick = function () {
            albumModal.style.display = "none";
            albumText.style.display = "none";
            resetAlbumContent(); // Сброс содержимого альбома
        };
    
    

        // Добавляем обработчик события для кнопки закрытия альбома
        closeBtn.onclick = function () {
            albumModal.style.display = "none";
            albumText.style.display = "none";
            resetAlbumContent(); // Сброс содержимого альбома
        };
    }
    
    
    

    // Функция для открытия оригинального изображения
    // Функция для открытия оригинального изображения
    // Функция для открытия оригинального изображения
    function openOriginalImage() {
        var enlargedImageContainer = document.createElement("div");
        enlargedImageContainer.classList.add("enlarged-image-container");

        var originalImage = document.createElement("img");
        originalImage.src = this.src;
        originalImage.alt = this.alt;
        originalImage.classList.add("original-image");

        enlargedImageContainer.appendChild(originalImage);

        // Сохраняем исходное содержимое, если оно еще не сохранено
        if (!originalContent) {
            originalContent = albumModal.innerHTML;
        }

        // Добавляем оригинальное изображение во всплывающее окно
        albumModal.innerHTML = "";
        albumModal.appendChild(originalImage);

        

        // Добавляем кнопку закрытия оригинального изображения
        var closeOriginalBtn = document.createElement("span");
        closeOriginalBtn.innerHTML = "&times;";
        closeOriginalBtn.classList.add("close");
        closeOriginalBtn.onclick = function() {
            // Сбрасываем содержимое альбома при закрытии оригинала
            resetAlbumContent();
        };
        albumModal.appendChild(closeOriginalBtn);

        // Сохраняем кнопку закрытия для последующего использования
        closeBtn = closeOriginalBtn;
    }

    // Привязываем обработчики событий для изображений
    images.forEach(function(image) {
        image.onclick = openOriginalImage;
    });
});

