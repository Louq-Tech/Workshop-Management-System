document.querySelector(".registration-form").addEventListener("submit", function(event) {
    var selectedRole = document.getElementById("roleSelect");
    if (selectedRole.selectedIndex === 0) {
        alert("Please choose a valid role.");
        event.preventDefault();
    }
});