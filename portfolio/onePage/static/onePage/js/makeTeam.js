var teamNameCheckVal = false
$(document).ready(function () {

    loadTeamList();
    teamNameCheck();
    makeTeam();
    
})
function makeTeam(){
    $("#make-tema-name-btn").click(function(){
        if(teamNameCheckVal==true){
            $.ajax({
                url: '/onePage/makeTeam/',
                type: 'POST',
                dataType: "json",
                contentType: 'application/x-www-form-urlencoded; charest=utf-8',
                data: { 'teamName': $('#make-team-name-input').val(),
                        'userId': $('#hiddenUserId').val() },
                success: function (str) {
                    if (str.result==true){
                        alert("축하합니다. 팀을 만들었습니다.");
                        $(".teamModal").modal('hide')
                        $("#tema-list-dropdown").empty();
                        loadTeamList();
                    }else if(str.result=="teamNumOutOfRange"){
                        alert("팀은 최대 3개만 가입 할 수 있습니다.");
                    }else{
                        alert("통신 실패");
                    }
                    
                },
                error: function(str){
                    alert("통신 실패")
                }
            })
        }
       
    });
}


function teamNameCheck() {
    $("#team-check").click(function () {
        if($("#make-team-name-input").val()!=""){
            $.ajax({
                url: '/onePage/checkTeamName/',
                type: 'POST',
                dataType: "json",
                contentType: 'application/x-www-form-urlencoded; charest=utf-8',
                data: { 'teamName': $('#make-team-name-input').val() },
                success: function (str) {
                    if (str.result == true) {
                        console.log('ok');
                        alert('사용 가능한 이름입니다.');
                        teamNameCheckVal = true;
                    } else if (str.result == false){
                        alert('팀 이름이 중복 됩니다.');
                        teamNameCheckVal = false;
                    } else{
                        alert("통신실패")
                        teamNameCheckVal = false;
                    }
                },
                error: function () {
                    alert("통신 실패");
                    teamNameCheckVal = false;
                }
            })
        }else{
            alert("팀 이름을 입력 해주세요.")
            teamNameCheckVal = false;
        }
        
    })
}


function loadTeamList() {
    console.log($("#hiddenUserId").val())
    $.ajax({
        url: '/onePage/loadTeamNameList/',
        type: 'POST',
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charest=utf-8',
        data: {
                'userId': $("#hiddenUserId").val()
              },
        success: function (str) {
            console.log("json data loaded")
            var j = 0;
            $.each(str, function (index, item) {
                $("#tema-list-dropdown").append('<li><a class ="team-list-li" href="#">' + item.teamName + '</a></li>')
            });
            makePlanBoard();
        },
        error: function () {
            console.log("json data load fail")
        }
    });
}
