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
    themeWord = document.getElementById('themeword');
    $('#darktheme').change(function() {
        if(this.checked) {
            $('#bd').addClass('night');
            $('.timer').css("color", "#FAFAFA");
            $('.btn-close').addClass('btn-close-white');
            themeWord.innerHTML = 'Dark Mode';
        }
        else {
            $('#bd').removeClass('night');
            $('.timer').css("color", "#121212");
            $('.btn-close').removeClass('btn-close-white');
            themeWord.innerHTML = 'Light Mode';
        }
    });
});

