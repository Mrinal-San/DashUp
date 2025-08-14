document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".task-check").forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            let taskText = this.closest("tr").querySelector(".task-text");
            if (this.checked) {
                taskText.style.textDecoration = "line-through";
                taskText.style.color = "#888";
            } else {
                taskText.style.textDecoration = "none";
                taskText.style.color = "#222";
            }
        });
    });
});
