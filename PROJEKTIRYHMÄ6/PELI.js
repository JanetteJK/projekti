'use strict';

async function haeAsiakas() {
  try {
    const response = await fetch('http://localhost:3000/hae_nimi/1');
    console.log(response)
    const data = await response.json();
    console.log(data)


    let puhe = document.querySelector("#puhe")
    puhe.innerHTML = data.nimi


  }
  catch (error){
    console.error('Error fetching data', error)
  }
}
haeAsiakas()
/* async function haeKysymys() {
  try {
    const response = fetch('http://localhost:3000/');
    console.log(response)
    const data = await response.json();
    console.log(data)

    let kys = document.querySelector('#kysymys')
    kys.innerHTML = data.kysymys
  } catch (error) {
    console.error('Error fetching data', error)
  }
} /*



/* hae ensin asiakkaan numero (aloitus 1), hae sitten asiakkaan numeron perusteella
kysymys. tuo inputin vastaus htmlästä ja tarkista onko se oikein. jos ei ole
kaiva kysymys nro +1. jos on oikein asiakas nro +1. jos vääriä vastauksia 3 vaihda
peliruutu game overiin.
 */





