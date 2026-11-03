document.addEventListener("DOMContentLoaded", function () {

    const boutonAleatoire = document.getElementById("bouton-aleatoire");
    const resultatAleatoire = document.getElementById("resultat-aleatoire");

    if (boutonAleatoire && resultatAleatoire) {

        boutonAleatoire.addEventListener("click", function () {

            fetch("/aleatoire")
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Aucun lien disponible");
                    }
                    return response.json();
                })
                .then(lien => {
                    resultatAleatoire.innerHTML = `
                        <h3>${lien.titre}</h3>
                        <a href="${lien.url}" target="_blank" rel="noopener noreferrer">
                            ${lien.url}
                        </a>
                        <p>Catégorie : ${lien.categorie}</p>
                    `;
                })
                .catch(() => {
                    resultatAleatoire.textContent =
                        "Aucun lien enregistré pour le moment.";
                });

        });
    }

});