$(document).ready(function() {
    const settingsButton = document.getElementById("settingsButton");
    settingsButton.addEventListener('click', () => {
        $('#settingsModal').modal('show');
    })
});

