document.addEventListener("DOMContentLoaded", function () {
    function validateLetters(input) {
        input.addEventListener("input", function () {
            this.value = this.value.replace(/[^а-яА-Я, -]/g, "");
        });
    }

    function validatePhoneNumber(input) {
        input.addEventListener("input", function () {
            this.value = this.value.replace(/[^\d\+]/g, "");
            
        });
    }

    const surnameInput = document.getElementById("id_surname");
    const nameInput = document.getElementById("id_name");
    const patronymicInput = document.getElementById("id_patronymic");
    const cityInput = document.getElementById("id_city");
    const phoneInput = document.getElementById("id_phone_number");

    if (surnameInput) validateLetters(surnameInput);
    if (nameInput) validateLetters(nameInput);
    if (patronymicInput) validateLetters(patronymicInput);
    if (cityInput) validateLetters(cityInput);
    if (phoneInput) validatePhoneNumber(phoneInput);
});