﻿// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

$(document).ready(function(){
    $("#dashboard").hide();
    setTimeout(
    function()
    {
        $("#welcomeBanner").hide();
        $("#dashboard").show();
    }, 2000);

    $(".minimizerButton").click(function(){
    	
    });
});
