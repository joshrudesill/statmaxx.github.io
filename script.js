

function change(arr) {
    final = `<div class="titleLine">
            <div><strong>Symbol</strong></div>
            <div><strong>Performance</strong></div>
            <div><strong>Popularity</strong></div>
            </div>
                <div class="sidebarInfoLine">
                </div>`
    for (let i = 1; i < arr.length; i++) {
        let name = arr[i-1]["name"]
        let mentions = arr[i-1]["count"]
        final += `<div class="sidebarInfoLine" id="il${i}"><div id="ps1">${i}. ${name}</div>
                    <div class="green" id="pp1"> 0000 </div>
                    <div id="pm1">${mentions}</div></div>`
    }
    document.querySelector("aside").innerHTML = final;
}

