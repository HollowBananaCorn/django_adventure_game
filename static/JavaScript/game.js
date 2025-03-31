// Update health to database. Could use XMLHttpRequest, but fetch is easier.
function UpdateHealth(health)
{
    fetch("/rango/update_health/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({ "new_health": health })}
    );
}

function UpdateGold(gold)
{
    fetch("/rango/update_gold/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({ "new_gold": gold })}
    );
}

function UpdateAttack(attack)
{
    fetch("/rango/update_attack/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({ "new_attack": attack })}
    );
}

function UpdateDefense(defense)
{
    fetch("/rango/update_defense/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({ "new_defense": defense })}
    );
}

function UpdateAgility(agility)
{
    fetch("/rango/update_agility/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({ "new_agility": agility })}
    );
}

function UpdateKills()
{
    fetch("/rango/increase_kills/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({})}
    ).then(response => response.json())
    .then(data => {window.location.href = "/rango/play/";});
}

function QuitGame()
{
    // can't use "{% static 'JavaScript/game.js' %}" because not django template
    fetch("/rango/delete_character/", {method : 'POST',
        headers : {"X-CSRFToken": getCSRFToken()}}).then(response => {
            if(response.redirected){window.location.href = response.url;}
        })
}

function getCSRFToken() // need it for POST requests
{
    var name = "csrftoken=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookies = decodedCookie.split(';');
    for(var i = 0; i < cookies.length; i++)
    {
        var cookie = cookies[i].trim();
        if(cookie.indexOf(name) == 0) // for the one starting with 'csrftoken='
        {
            return cookie.substring(name.length, cookie.length); // return rest of the cookie(after csrftoken=)
        }
    }
    // if none found(will probably lead to a 403 error)
    return "";
}

function submitScores()
{
    var startTime = new Date("{{ player.start_time|date:'Y-m-d H:i:s' }} UTC");
    
    if (isNaN(startTime)) {
        alert("Invalid date format: " + "{{ player.start_time }}");
    } else {
        alert(startTime);
    }
    var endTime = new Date(); // now
    var passed_time = Math.floor((endTime - startTime) / 1000); // to seconds

    // alert('before fetch')
    fetch("/rango/update_score/", {method : "POST", 
        headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
    },
    body : JSON.stringify({ "passed_time" : passed_time })}
    ).then(response => response.json())
    .then(data => {
        alert("Score submitted! Your time: " + data.formatted_time);
        window.location.href = "{% url 'rango:index' %}";
    });
}

function calculateMostStats(x)
{
    return Math.floor(-Math.exp(-(x + 90) / 90) * 274 + 100);
}

function calculateAttackStat(x)
{
    return x**0.6 * 3;
}