function aft_qr() {
    if (res.slice(3) == 'yz1') {
        loc = "304";
        document.getElementById('aft_scn').innerHTML = `<h2>You are at: </h2><p><h3>${loc}</a></h3></p>`;
        document.getElementById('prev_loc_lb').remove();
        document.getElementById('prev_loc').remove();
    }
    else if (res.slice(3) == 'zy2') {
        loc = "regal";
        document.getElementById('aft_scn').innerHTML = `<h2>You are at: </h2><p><h3>${loc}</a></h3></p>`;
    }
    else if (res.slice(3) == 'yb3') {
        loc = "bm";
        document.getElementById('aft_scn').innerHTML = `<h2>You are at: </h2><p><h3>${loc}</a></h3></p>`;
    }
    else if (res.slice(3) == 'ap4') {
        loc = "cm";
        document.getElementById('aft_scn').innerHTML = `<h2>You are at: </h2><p><h3>${loc}</a></h3></p>`;
    }
    else if (res.slice(3) == 'ba5') {
        loc = "gwoi";
        document.getElementById('aft_scn').innerHTML = `<h2>You are at: </h2><p><h3>${loc}</a></h3></p>`;
    }
    else {
        alert("Invalid QR");
    }
} 
