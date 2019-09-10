$(".hosp-box").on("click",".hosp-wrapper", (e) => {
    let target = e.target
    if(target.className == "hosp-wrapper"){
       let hosp_name = $(".hosp-h3").text()
       $.ajax({
        url: "/appointment?hosp_name="+hosp_name,
        method: "GET",
        success:function(data){
            window.location = "/appointment?hosp_name="+hosp_name
        }
    })
    }

})