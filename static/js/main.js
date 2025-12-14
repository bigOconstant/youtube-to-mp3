
const myForm = document.getElementById("myForm");
myForm.addEventListener("submit", function(event) {
    const loadingBar = document.getElementById("progress-2");
    const submitButton = document.getElementById("submitButton");
    loadingBar.classList.remove("hidden");
    submitButton.disabled = true;
});