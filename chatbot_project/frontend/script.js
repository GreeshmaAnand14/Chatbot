
const themeToggle = document.getElementById("themeToggle");

themeToggle.addEventListener("click", function () {
    document.body.classList.toggle("light-mode");

    if (document.body.classList.contains("light-mode")) {
        themeToggle.textContent = "☀️";
    } else {
        themeToggle.textContent = "🌙";
    }
});

// Display current date and time
function updateDateTime() {
    const now = new Date();

    document.getElementById("currentDate").textContent =
        now.toLocaleDateString("en-IN", {
            weekday: "long",
            day: "numeric",
            month: "long",
            year: "numeric"
        });

    document.getElementById("currentTime").textContent =
        now.toLocaleTimeString("en-IN");
}

// Update every second
updateDateTime();
setInterval(updateDateTime, 1000);
