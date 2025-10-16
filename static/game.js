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
});



