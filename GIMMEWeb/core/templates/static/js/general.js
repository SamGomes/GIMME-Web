﻿$(document).ready(function(){

    // modals
    var rootEl = document.documentElement;
    var allModals = getAll('.modal');
    var modalButtons = getAll('.modal-button');
    var modalCloses = getAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button');

    if (modalButtons.length > 0) {
        modalButtons.forEach(function (el) {
            el.addEventListener('click', function () {
                var target = document.getElementById(el.dataset.target);
                rootEl.classList.add('is-clipped');
                target.classList.add('is-active');
            });
        });
    }

    if (modalCloses.length > 0) {
        modalCloses.forEach(function (el) {
            el.addEventListener('click', function () {
                closeModals();
            });
        });
    }

    document.addEventListener('keydown', function (event) {
            var e = event || window.event;
            if (e.keyCode === 27) {
                closeModals();
        }
    });

    var closeModals = function() {
        rootEl.classList.remove('is-clipped');
        allModals.forEach(function (el) {
            el.classList.remove('is-active');
        });
    }

    // general animations and element functionalities
    $("#dashboard").hide();
    setTimeout(
    function()
    {
        $("#welcomeBanner").hide();
        $("#dashboard").show();
    }, 0);

    $(".minimizerButton").append("<i class=\"fa fa-window-minimize\"></i>").parent().parent().parent().parent().find(".panel-block").show();
    $(".minimizerButton").click(function(){
        $(this).empty();
        var content = $(this).parent().parent().parent().parent().find(".panel-block");
    	if(content.is(":hidden")){
            $(this).append("<i class=\"fa fa-window-minimize\"></i>");
            content.show(350);
        }else{
            $(this).append("<i class=\"fa fa-window-maximize\"></i>");
            content.hide(350);
        }
    });
});

var getAll = function(selector) {
    return Array.prototype.slice.call(document.querySelectorAll(selector), 0);
}

var parseUnformattedString = function(attributeStr){
    return attributeStr.replace(/&quot;/g,"\"").replace(/&#39;/g,"\"")
}

var parseSessionAttribute = function(attributeStr){
    return JSON.parse(parseUnformattedString(attributeStr))
}
