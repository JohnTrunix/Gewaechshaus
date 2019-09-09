<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="einstellungen.css">
        <script src="js/jquery.min.js"></script>
    </head>
    <body style="background-color:white;">
        <div class="menu_rahmen">
            <div class="icon top" onclick="window.location='/';">
                <img src="img/house.svg" class="menubild">
            </div>
            <div class="icon middle" onclick="window.location='/statistik.php';">
                <img src="img/pie-chart.svg" class="menubild">
            </div>
            <div class="icon bottom aktiv" onclick="window.location='/einstellungen.php';">
                <img src="img/settings.svg" class="menubild">
            </div>
            <div class="icon shutdown" onclick="window.location='/herunterfahren.php';">
                <img src="img/logout.svg" class="menubild">
            </div>
        </div>
        <form class="form" action="parameter-update.php">
            <input type="text" name="name" placeholder="Name">
            <br>
            <a>Slot: </a>
            <select name="slot" onchange="getComboA(this)">
                <option value="" disabled selected>Nr.</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
            </select>
            <div class="container">
                <div class="range-slider">
                    <span id="rs-bullet1" class="rs-label">0</span>
                    <input id="rs-range-line1" class="rs-range" type="range" value="0" min="0" max="200">
                </div>
                <div class="box-minmax">
                </div>
                <script>
                    var rangeSlider1 = document.getElementById("rs-range-line1");
                    var rangeBullet1 = document.getElementById("rs-bullet1");
                    
                    rangeSlider1.addEventListener("input", showSliderValue1, false);
                    
                    function showSliderValue1() {
                      rangeBullet1.innerHTML = rangeSlider1.value;
                    var bulletPosition1 = (rangeSlider1.value /rangeSlider1.max);
                    rangeBullet1.style.left = (bulletPosition1 * 578) + "px";
                    }
                </script>
            </div>
            <br>
            <div class="container">
                <div class="range-slider">
                    <span id="rs-bullet2" class="rs-label">0</span>
                    <input id="rs-range-line2" class="rs-range" type="range" value="0" min="0" max="200">
                </div>
                <div class="box-minmax">
                </div>
                <script>
                    var rangeSlider2 = document.getElementById("rs-range-line2");
                    var rangeBullet2 = document.getElementById("rs-bullet2");
                    
                    rangeSlider2.addEventListener("input", showSliderValue2, false);
                    
                    function showSliderValue2() {
                    rangeBullet2.innerHTML = rangeSlider2.value;
                    var bulletPosition2 = (rangeSlider2.value /rangeSlider2.max);
                    rangeBullet2.style.left = (bulletPosition2 * 578) + "px";
                    }
                </script>
            </div>
            <br>
            <div class="container">
                <div class="range-slider">
                    <span id="rs-bullet3" class="rs-label">0</span>
                    <input id="rs-range-line3" class="rs-range" type="range" value="0" min="0" max="200">
                </div>
                <div class="box-minmax">
                </div>
                <script>
                    var rangeSlider3 = document.getElementById("rs-range-line3");
                    var rangeBullet3 = document.getElementById("rs-bullet3");
                    
                    rangeSlider3.addEventListener("input", showSliderValue3, false);
                    
                    function showSliderValue3() {
                    rangeBullet3.innerHTML = rangeSlider3.value;
                    var bulletPosition3 = (rangeSlider3.value /rangeSlider3.max);
                    rangeBullet3.style.left = (bulletPosition3 * 578) + "px";
                    }
                </script>
            </div>
            <br>
            <div class="container">
                <div class="range-slider">
                    <span id="rs-bullet4" class="rs-label">0</span>
                    <input id="rs-range-line4" class="rs-range" type="range" value="0" min="0" max="200">
                </div>
                <div class="box-minmax">
                </div>
                <script>
                    var rangeSlider4 = document.getElementById("rs-range-line4");
                    var rangeBullet4 = document.getElementById("rs-bullet4");
                    
                    rangeSlider4.addEventListener("input", showSliderValue4, false);
                    
                    function showSliderValue4() {
                    rangeBullet4.innerHTML = rangeSlider4.value;
                    var bulletPosition4 = (rangeSlider4.value /rangeSlider4.max);
                    rangeBullet4.style.left = (bulletPosition4 * 578) + "px";
                    }
                </script>
            </div>
            <br>
            <input type="submit" value="Speichern">
            <div id="error_div">Fehler!</div>
            <div id="success_div">Erfolgreich!</div>
        </form>
        <script type="text/javascript">
            var url = window.location.href;
            var error_msg = document.getElementById('error_div');
            var success_msg = document.getElementById('success_div');
            
            if ( url.search( 'fehler' ) > 0 ) {
              error_msg.style.display = "flex";
              success_msg.style.display = "none";
            } else if ( url.search( 'erfolgreich' ) > 0 ) {
                success_msg.style.display = "flex";
                error_msg.style.display = "none";
            }
        </script>
    </body>
</html>