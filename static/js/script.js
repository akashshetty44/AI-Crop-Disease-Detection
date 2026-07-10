// static/js/script.js

document.addEventListener("DOMContentLoaded", () => {

    const fileInput = document.querySelector(
        'input[name="leaf_image"]'
    );

    const form = document.querySelector("form");

    // ---------- Image Preview ----------

    if (fileInput) {

        const preview = document.createElement("img");

        preview.id = "preview";

        preview.style.display = "none";
        preview.style.width = "250px";
        preview.style.marginTop = "20px";
        preview.style.borderRadius = "10px";
        preview.style.border = "2px solid #4CAF50";

        fileInput.parentNode.appendChild(preview);

        fileInput.addEventListener("change", function () {

            const file = this.files[0];

            if (!file) {
                preview.style.display = "none";
                return;
            }

            const allowed = [
                "image/jpeg",
                "image/jpg",
                "image/png"
            ];

            if (!allowed.includes(file.type)) {

                alert("Please upload a JPG or PNG image.");

                this.value = "";

                preview.style.display = "none";

                return;
            }

            const reader = new FileReader();

            reader.onload = function (e) {

                preview.src = e.target.result;
                preview.style.display = "block";

            };

           
