document.getElementById('modoBlackBtn').addEventListener('click', function() {
    // Obtén el elemento <body>
    var body = document.body;

    // Toggle entre las clases de Bootstrap para tema claro y oscuro
    body.classList.toggle('bg-light');
    body.classList.toggle('bg-dark');
    body.classList.toggle('text-light');

    // Toggle entre la clase específica para el modo oscuro en los botones
    var buttons = document.querySelectorAll('.btn-light-mode');
    buttons.forEach(function(button) {
        button.classList.toggle('btn-dark');
    });

    // Toggle entre las clases específicas para el modo oscuro en el nav
    var nav = document.querySelector('.navbar');
    nav.classList.toggle('navbar-dark');
    nav.classList.toggle('navbar-light');
    nav.classList.toggle('bg-dark');
    nav.classList.toggle('bg-light');

    // Toggle entre la clase específica para el modo oscuro en el footer
    var footer = document.querySelector('.footer');
    footer.classList.toggle('bg-dark');
    footer.classList.toggle('bg-light');
    footer.classList.toggle('text-light');

    // Toggle entre la clase específica para el modo oscuro en el div card
    var card = document.querySelector('.card');
    if (card) {
        card.classList.toggle('bg-dark');
        card.classList.toggle('bg-light');
        card.classList.toggle('text-light');

        // Verificar si hay listas ul dentro del div card
        var lists = card.querySelectorAll('ul');
        lists.forEach(function(list) {
            list.classList.toggle('bg-dark');
            list.classList.toggle('bg-light');
            list.classList.toggle('text-light');
        });
    }

    // Cambia el texto del botón según el modo actual
    var modoActual = body.classList.contains('bg-dark') ? 'Modo Claro' : 'Modo Black';
    this.innerText = modoActual;
});



