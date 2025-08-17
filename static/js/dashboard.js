document.addEventListener("DOMContentLoaded", function () {
    const progressBar = document.querySelector(".progress-bar");
    const width = progressBar.style.width;

    // Animate from 0 to desired width
    progressBar.style.width = "0";
    setTimeout(() => {
        progressBar.style.width = width;
    }, 100);
});
