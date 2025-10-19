console.log("started")

document.addEventListener('DOMContentLoaded', function(){
    const form = document.getElementById("dspan");
    if (form) {
        form.addEventListener('keydown', function(e) {
            if (e.key == "Enter") {
                e.preventDefault()
            }
        });
    }

/*    const advanceButton = document.getElementById("advance-button");
    if (advanceButton) {
        console.log("Advance: Created");
        document.addEventListener("click", function(event) {
            console.log("I am listening")
            fetch("/finish", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    dspan: window.dSpan
                })
            }

            )
        })
    } */
});





