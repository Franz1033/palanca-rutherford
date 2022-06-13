document.addEventListener('DOMContentLoaded', () => {

    const select = document.getElementById('select');

    items = [{"name" :"Amores, Carl", "email" : "nikkoboyamoress@gmail.com"}, {"name" :"Bajo, Jake", "email" : "jakebajo21@gmail.com"},{"name" :"Bustaliño, Aidan", "email" : "SoheeGT0912@gmail.com"},
    {"name" :"Elumba, Lemuel", "email" : "lemuelelumba0729@gmail.com"}, {"name" :"Garcia, Rudz", "email" : "rudzcullin12@gmail.com"},{"name" :"Herrera, Germaine", "email" : "germaineconan24@gmail.com"},
    {"name" :"Locsin, Jojene", "email" : "ianlocsin70@gmail.com"}, {"name" :"Macatual, Cyril", "email" : "cyilmacatual14@gmail.com "}, {"name" :"Omaguing, Micole", "email" : "omaguing.nino007@gmail.com"},
    {"name" :"Orong, Marc", "email" : "marcorong.03@gmail.com "}, {"name" :"Vergara, Jon", "email" : "Vergarajon30@gmail.com"}, {"name" :"Villejo, Luigi", "email" : "villejolm@gmail.com"},
    {"name" :"Zapanta, Franz", "email" : "franzzapanta1033@gmail.com"}, {"name" :"Alicante, Justine", "email" : "mizukijustine@gmail.com"}, {"name" :"Banawan, Treshia", "email" : "treshiamae07@gmail.com"}, 
    {"name" :"Dengal, Arnee", "email" : "arneedengal4@gmail.com "}, {"name" :"Duhaylungsod, Mabel", "email" : "mabelduhaylungsod@gmail.com"}, {"name" :"Euhengco, Heart", "email" : ""},
    {"name" :"Luce, Kate", "email" : ""}, {"name" :"Mira, Keren", "email" : ""}, {"name" :"Morandarte, Sol", "email" : "morandartesol@gmail.com"}, {"name" :"Pacuyao, Ruth", "email" : "hisokagobrrt@gmail.com"},
    {"name" :"Panong, Kylla ", "email" : ""}, {"name" :"Salas, Marnie", "email" : ""}, {"name" :"Sinconiegue, Gale", "email" : ""}, {"name" :"Sorronda, Melanie", "email" : "sorrondamelanie@gmail.com"}, 
    {"name" :"Tabañag, Althea", "email" : "tabanagag@gmail.com"}, {"name" :"Villadarez, Niña", "email" : "villadareznn@gmail.com"}]

    items.forEach(item => {
    const option = document.createElement('option');
    option.value = item["name"];
    option.innerHTML = item["name"];
    
    select.appendChild(option)
    });

    document.querySelector('form').addEventListener('submit', () => {
        if (confirm("Are you sure?") == false) {
            window.location.reload();
       }    
    })
    
})

