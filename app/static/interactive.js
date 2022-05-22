$(document).ready(function() {
    const settingsButton = document.getElementById("settingsButton");
    const statsButton = document.getElementById("statsButton");
    settingsButton.addEventListener('click', () => {
        $('#settingsModal').modal('show');
    });
    statsButton.addEventListener('click', () => {
        $('#statsModal').modal('show');
    });
});

