$(document).ready(function(){
    $(".hosp-box").on("click",".hosp-wrapper", ({target}) => {
        // let target = e.target
        // if(target.className == "hosp-wrapper"){
           let hosp_name = target.innerText
           let name = hosp_name.split("\n")
           console.log(name[0])
           $.ajax({
            url: "/appointment?hosp_name="+name[0],
            method: "GET",
            success:function(data){
                window.location = "/appointment?hosp_name="+name[0]
            }
        })
        })
    
    
    $(".fas").on("click", (e) => {
        e.stopPropagation()
    
    })

    $(".place").on("click", (e) => {
        e.stopPropagation()
    
    })

    $(".add1").on("click", (e) => {
        e.stopPropagation()
    
    })
});


