document.addEventListener("DOMContentLoaded", function() {
    const loader = document.getElementById("loader");

    // Show loader on all link clicks
    document.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", function(e) {
            if (link.target !== "_blank" && link.href) {
                loader.style.display = "flex";
            }
        });
    });

    // Show loader on all form submissions
    document.querySelectorAll("form").forEach(form => {
        form.addEventListener("submit", function() {
            loader.style.display = "flex";
        });
    });
});
