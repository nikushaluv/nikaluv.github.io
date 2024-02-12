function openBook() {
    const bookContent = document.getElementById('book-content');
    const bookCover = document.querySelector('.book-cover');
    const book = document.querySelector('.book');

    bookContent.classList.remove('hidden');
    bookCover.style.transform = 'scaleX(0)';
    book.style.transform = 'scaleX(1)';
}
