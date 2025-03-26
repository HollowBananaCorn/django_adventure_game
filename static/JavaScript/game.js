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