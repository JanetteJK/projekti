document.addEventListener('DOMContentLoaded', function() {
    const karttaElementti = document.getElementById('kartta');
    if (karttaElementti) {
        const kartta = L.map('kartta').setView([20, 0], 2);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(kartta);
    }

    const vastausKentta = document.getElementById('vastaus');
    if (vastausKentta) {
        vastausKentta.focus();
    }

    const viestiElementti = document.querySelector('.asiakas-viesti');
    if (viestiElementti) {
        const alkuperainenViesti = viestiElementti.textContent;
        viestiElementti.textContent = '';

        setTimeout(() => {
            kirjoitaViesti(viestiElementti, alkuperainenViesti);
        }, 300);
    }


    const onnistumisviesti = document.querySelector('.viesti-ilmoitus.onnistui');
    if (onnistumisviesti) {

        const rahapussiElementti = document.querySelector('.rahapussi');
        if (rahapussiElementti) {
            const rahapussiTeksti = rahapussiElementti.textContent;
            const numeroArvo = rahapussiTeksti.match(/\d+/);

            if (numeroArvo) {
                const nykyinenRaha = parseInt(numeroArvo[0]);
                // Jos pelaaja vastasi heti oikein, lisätään 15€
                if (onnistumisviesti.textContent.includes('tippiä')) {
                    animoiRahanLisays(nykyinenRaha - 15, nykyinenRaha);
                }
                // Muuten lisätään vain 5€
                else {
                    animoiRahanLisays(nykyinenRaha - 5, nykyinenRaha);
                }
            }
        }
    }
});

function kirjoitaViesti(elementti, teksti, nopeus = 25) {
    let i = 0;

    function kirjoita() {
        if (i < teksti.length) {
            elementti.textContent += teksti.charAt(i);
            i++;
            setTimeout(kirjoita, nopeus);
        }
    }

    kirjoita();
}

function animoiRahanLisays(alkuRaha, loppuRaha) {
    const rahapussiElementti = document.querySelector('.rahapussi');
    if (!rahapussiElementti) return;

    let nykyinenRaha = alkuRaha;
    rahapussiElementti.textContent = `Rahapussi: ${nykyinenRaha}€`;

    const interval = setInterval(() => {
        nykyinenRaha += 1;
        rahapussiElementti.textContent = `Rahapussi: ${nykyinenRaha}€`;

        if (nykyinenRaha >= loppuRaha) {
            clearInterval(interval);
        }
    }, 100);
}