console.log("this is the saving script");

window.onload = function() {
    const nameInput = document.getElementById("name");
    const submitButton = document.getElementById("submit-button");

    submitButton.addEventListener("click", submit);

    function submit() {
        console.log("time to submit");
        // if does not exist exit
        if (!nameInput) {
            return;
        }
    
        const name = nameInput.value;
        const data = {
            "name": "name"
        };
    
        fetch(
            "/shoe/save",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        ).then(
            (response) => {
                return response.json();
            }
        ).then(
            (json) => {
                console.log("successfull post", json);
            }
        ).catch(
            (error) => {
                console.error("error", error);
            }
        )
    }
}