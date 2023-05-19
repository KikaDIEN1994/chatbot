const element = document.getElementById("question1");
element.addEventListener("click", listener());

function listener(){
  document.getElementById("demo").innerHTML = "add listener recu";
}
function performPOST(){
    $.ajax({
        type:"POST",
        url: "/question",
        data:{data_question:"value"},
    })
}
