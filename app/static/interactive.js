//Modal Buttons on Front Page
$(document).ready(function() {
    const settingsButton = document.getElementById("settingsButton");
    const statsButton = document.getElementById("statsButton");
    const howtoButton = document.getElementById("howtoButton");

    settingsButton.addEventListener('click', () => {
        $('#settingsModal').modal('show');
    });
    statsButton.addEventListener('click', () => {
        $('#statsModal').modal('show');
    });
    howtoButton.addEventListener('click', () => {
        $('#howtoModal').modal('show');
    });
});

