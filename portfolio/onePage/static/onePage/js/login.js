
$(document).ready(function () {
    $("#login-btn").click(function(){

        // userId = document.getElementById("loginId").attr('value');
        var userId = $('#login-id').val();
        var userPw = $("#login-pw").val();

        if(userId!=""){
            if(userPw!=""){
                //alert(userId);
                $("#login-form").submit();
            }else{
                alert("비밀번호를 입력하세요.")
            }
        }else{
            alert("아이디를 입력하세요.")
        }
    })
})