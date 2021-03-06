console.log("this is the index page whooo")

function getShoes() {
    // farms.school, farms.shchool/shoe-api
    return fetch("/shoe-api")
        .then(
            (response) => {
                return response.json();
            }
        ).then(
            (json) => {
                console.log("YOU GOT MAIL MOTHER FUCKER: \n", json);
            }
        )
}

function createShoe() {
    const data = {
        "brand": "uggs"
    };
    // farms.school, farms.shchool/shoe-api
    return fetch("/shoe-api", 
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    )
    .then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("YOU GOT MAIL MOTHER FUCKER: \n", json);
        }
    )
}

function deleteShoe() {
    // farms.school, farms.shchool/shoe-api
    return fetch("/shoe-api/1", 
        {
            method: "DELETE"
        }
    )
    .then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("YOU GOT MAIL MOTHER FUCKER: \n", json);
        }
    )
};

window.onload = function() {
    const saveButton =  document.getElementById("save-button");
    const getButton =  document.getElementById("get-button");
    const deleteButton =  document.getElementById("delete-button");

    saveButton.addEventListener("click", createShoe);
    getButton.addEventListener("click", getShoes);
    deleteButton.addEventListener("click", deleteShoe);

}