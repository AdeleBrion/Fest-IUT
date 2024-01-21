function ajouterALaListe() {
    // Récupérer la valeur de l'input
    var inputValue = document.getElementById("Personne").value;

    var ul = document.getElementById("list_personne");

    // Vérifier si la valeur n'est pas vide
    if (inputValue.trim() !== "") {
        var newItem = document.createElement("li");
        var newp = document.createElement("p");
        newp.innerHTML = inputValue;
        newItem.appendChild(newp);
        ul.appendChild(newItem);
        document.getElementById("Personne").value = "";
    }

    var listePersonnes = [];
    var ulListePersonne = document.getElementById("list_personne");
    var items = ulListePersonne.getElementsByTagName("li");

    for (var i = 0; i < items.length; i++) {
        listePersonnes.push(items[i].innerText.trim());
    }
    document.getElementById("listePersonnes").value = JSON.stringify(listePersonnes);
}
