// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// Display the modal with message
window.onload = function() {
    var message = document.getElementById("modal-message").innerText.trim();
    if (message !== "") {
        modal.style.display = "block";
    }
}