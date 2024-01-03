


document.getElementById("login-form");


login-form.addEventListner("submit",(e) =>{
    e.preventDefault();

    let username = document.getElementById("c-name");
    let password = document.getElementById("c-pass");


    let n ="firas"
    let p = "1234"
    if(username.vlue == "firas" || password.value == "1234"){
        alert("تم ادخال البيانات بنجاح");
    }
    else{
        alert("فشل في ادخال البيانات");

    }
})
