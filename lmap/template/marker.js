(function () {
    var marker = new AMap.Marker({
        position: [{% long %}, {% lat %}],
        map: map,
    });

    marker.content = "<h3> {% name %} </h3>";
    marker.content += `{% content %}`;

    marker.on("mouseover", infoOpen);
    // marker.emit('mouseover', {target: marker});
    marker.on("mouseout", infoClose);
    marker.on("click", newMAp);
})();
