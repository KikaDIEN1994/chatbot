function performPOST(){
    $.ajax({
        type:"POST",
        url: "/question",
        data:{"question":"data_question"},
    })
}