
$(document).ready(function () {
    $("#logInBtn").click(function(){

        // userId = document.getElementById("loginId").attr('value');
        var userId = $('#loginId').val();
        var userPw = $("#loginPw").val();

        if(userId!=""){
            if(userPw!=""){
                alert(userId);
                $("#loginForm").submit();
            }else{
                alert("비밀번호를 입력하세요.")
            }
        }else{
            alert("아이디를 입력하세요.")
        }
       
       
    })
})