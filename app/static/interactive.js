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
            darkModeOn();
        }
        else {
            darkModeOff();
        }
    });

    function darkModeOn() {
        $('#bd').addClass('night');
        $('.timer').css("color", "#FAFAFA");
        $('.btn-close').addClass('btn-close-white');
        themeWord.innerHTML = 'Dark Mode';
        $('#playingvid').attr("src", "./static/images/howtodarkmode.gif");
        localStorage.setItem('darkMode', 'enabled');
    };

    function darkModeOff() {
        $('#bd').removeClass('night');
        $('.timer').css("color", "#121212");
        $('.btn-close').removeClass('btn-close-white');
        themeWord.innerHTML = 'Light Mode';
        $('#playingvid').attr("src", "./static/images/howto.gif");
        localStorage.setItem('darkMode', null);
    };

    //Save user's settings with local storage
    mode = localStorage.getItem('darkMode');
    if (mode == 'enabled') {
        darkModeOn();
        document.getElementById('darktheme').checked = true;
    }
    else {
        darkModeOff();
        document.getElementById('darktheme').checked = false;
    };
});

