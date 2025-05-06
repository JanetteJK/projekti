'use strict';

/* 1. show map using Leaflet library. (L comes from the Leaflet library) */

const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);




// global variables

// icons

// function to fetch data from API

// function to update game status

// function to check if any goals have been reached

// function to update moneybag



// function to check if game is over

// function to set up game
// this is the main function that creates the game and calls the other functions
async function gameSetup(){

}
// event listener to hide goal splash

async function startGame() {
  try {
    const response = await fetch('http://localhost/aloita_peli');
    const data = await response.json();

    console.log(data)
    asiakas = data;
    let puhe = document.createElement("li")
    let teksti = document.createTextNode(`${data}`);
    puhe.appendChild(teksti)
  }
  catch (error){
    console.error('Error fetching data', error)
  }
}