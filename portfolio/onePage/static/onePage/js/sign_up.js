
$(document).ready(function(){
    var checkId;
    $("#sign-modal").click(function(){
        checkId = false;
    })
    $("#id-check").click(function(){
        //alert($("#sign-id").val());
        if ($("#sign-id").val() != ""){

            $.ajax({
                url: '/onePage/checkId/',
                type: 'POST',
                dataType: "json",
                contentType: 'application/x-www-form-urlencoded; charest=utf-8',
                data: {"sign-id-val" : $("#sign-id").val()},
                success: function (str) {
                    if(str.result == true){
                        alert("사용 가능합니다.")
                        checkId = true;
                    }else{
                        alert("이미 사용중입니다.")
                        checkId = false;
                    }
                },error: function(){
                    alert('통신오류');
                }
            });

        }else{
            alert("아이디를 입력 해주세요.");
        }
    })

    $("#sign-up-btn").click(function(){
        if(checkId!=false){
            if($("#sign-pw").val()!=""){
                if($("#sign-email").val()!=""){
                    var id = $("#sign-id").val();
                    var pw = $("#sign-pw").val();
                    var email = $("#sign-email").val();
                    $.ajax({
                        url: '/onePage/signUp/',
                        type: 'POST',
                        dataType: "json",
                        contentType: 'application/x-www-form-urlencoded; charest=utf-8',
                        data: {"sign-id-val" : id, 
                               "sign-pw-val" : pw,
                               "sigh-email-val" : email                              
                              },
                        success:function(str){
                            if(str.result == true)
                            alert("회원가입을 축하드립니다.");
                            $(".modal").modal('hide');
                        },
                        error:function(){
                            alert("회원가입 실패");
                        }
                    })
                }else{
                    alert("이메일을 입력 해주세요.")
                }
            }else{
                alert("비밀번호르 입력 해주세요.")
            }
        }else{
            alert("아이디 중복체크를 해주세요.");
        }
    })


})