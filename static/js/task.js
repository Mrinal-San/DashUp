document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".task-check").forEach(function (checkbox) {
    const taskText = checkbox.closest("tr").querySelector(".task-text");

    // Apply initial style
    if (checkbox.checked) {
      taskText.style.textDecoration = "line-through";
      taskText.style.color = "#888";
    }

    checkbox.addEventListener("change", function () {
      const taskId = this.dataset.taskId;
      const isDone = this.checked ? 1 : 0;

      // Update text style
      taskText.style.textDecoration = this.checked ? "line-through" : "none";
      taskText.style.color = this.checked ? "#888" : "#222";

      // Send update to Flask
      fetch(`/task/done/${taskId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ is_done: isDone })
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(err => console.error(err));
    });
  });
});