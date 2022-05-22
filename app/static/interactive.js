//Modal Buttons on Front Page
$(document).ready(function() {
    //open modals
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

    //toggle dark mode
    $('#darktheme').change(function() {
        if(this.checked) {
            $('#bd').addClass('night');
            $('i').css("color", "white");
        }
        else {
            $('#bd').removeClass('night');
            $('i').css('color', 'black');
        }
    });
});

