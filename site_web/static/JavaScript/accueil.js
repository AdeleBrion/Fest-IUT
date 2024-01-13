const img = document.getElementById('carousel');
const rightBtn = document.getElementById('right-btn');
const leftBtn = document.getElementById('left-btn');
const nom = document.getElementById('nom_carousel');
const description = document.getElementById('description_carousel');
const dateC = document.getElementById('date_carousel');
const heureC = document.getElementById('heure_carousel');
const style = document.getElementById('style_carousel');

// Images are from unsplash
let pictures = ['https://images.unsplash.com/photo-1537000092872-06bbf7b64f60?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=14d2fe1244b43a1841569da918066fc4&auto=format&fit=crop&w=1050&q=80',
    'https://images.unsplash.com/photo-1537005081207-04f90e3ba640?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=ffb71f2a2843e802e238c5ff8e4bbb8c&auto=format&fit=crop&w=764&q=80',
    'https://images.unsplash.com/photo-1536873602512-8e88cc8398b1?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=60a351868d0839e686c8c5a286265f8d&auto=format&fit=crop&w=1050&q=80'];
let informations = [
    {
        titre: "1",
        img: "https://images.unsplash.com/photo-1537000092872-06bbf7b64f60?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=14d2fe1244b43a1841569da918066fc4&auto=format&fit=crop&w=1050&q=80"
    },
    {
        titre: "2",
        img: "https://images.unsplash.com/photo-1537005081207-04f90e3ba640?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=ffb71f2a2843e802e238c5ff8e4bbb8c&auto=format&fit=crop&w=764&q=80"
    },
    {
        titre: "3",
        img: "https://images.unsplash.com/photo-1536873602512-8e88cc8398b1?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=60a351868d0839e686c8c5a286265f8d&auto=format&fit=crop&w=1050&q=80"

    }
]
// Effectuez une requête fetch
fetch('/groupes/liste')
    .then(response => response.json())
    .then(data => {
        sessionStorage.setItem('informations', JSON.stringify(data));
        const storedData = JSON.parse(sessionStorage.getItem('informations'));
        console.log(storedData);
        changeInfo(0);

    })
    .catch(error => console.error('Erreur lors de la récupération des informations:', error));

function afficherInformations(data) {
    console.log(data);
}

function changeInfo(indice) {
    let date = new Date(storedData[indice].concert.dateHeureDebut)
    let h = date.getUTCMinutes();
    let formate = h < 10 ? '0' + h : h;
    let heure = 'Heure : ' + date.getUTCHours() + 'h' + formate;
    if (storedData[indice].img == null) {
        storedData[indice].img = pictures[indice % 3];
    }
    img.src = storedData[indice].img;
    nom.textContent = storedData[indice].nomGroupe
    description.textContent = storedData[indice].descriptionGroupe;
    style.textContent = 'Style : ' + storedData[indice].style;
    dateC.textContent = 'Date : ' + date.toLocaleDateString();
    heureC.textContent = heure;
}

// Premier informations vu 

let position = 0;
const storedData = JSON.parse(sessionStorage.getItem('informations'));

const moveRight = () => {
    if (position >= storedData.length - 1) {
        position = 0
        changeInfo(position);
        return;
    }
    changeInfo(position + 1);
    position++;
}

const moveLeft = () => {
    if (position < 1) {
        position = storedData.length - 1;
        changeInfo(position);
        return;
    }
    changeInfo(position - 1);
    position--;
}

rightBtn.addEventListener("click", moveRight);
leftBtn.addEventListener("click", moveLeft);