$(document).ready(function () {
    printPlanBoard();
    attrPlan();
    addPlan();
    $("#plan-board-div").hide();
    delPlan();

})

function delPlan(){
    //동적 태그의 동적 이벤트 바인딩 하기
    $(document).on("click",".plan-delete-btn",function(){
        var planNo = $(this).attr("value");
        var result = confirm("플랜을 삭제하시 겠습니까?");
        if(result){
            $.ajax({
                url: '/onePage/delPlan/',
                type: 'POST',
                dataType: "json",
                contentType: 'application/x-www-form-urlencoded; charest=utf-8',
                data: { "planNo": planNo },
                success:function(str){
                    if(str.result==true){
                        $("#plan-list-board").empty();
                        printPlanFunctuon($("#h1-teamName").text());
                    }
                },error:function(){
                    alert("플랜 삭제 실패")
                }
            });
        }
    })
}

//plan modal창에서 ok버튼을 눌러 플랜을 추가했을 때
function addPlan() {
    $("#plan-name-submit").click(function () {
        if ($("#plan-name-text").val() != "") {
            var planName = $("#plan-name-text").val();
            var teamName = $("#team-name-plan").attr("placeholder");
            console.log(planName);
            console.log(teamName);
            $.ajax({
                url: '/onePage/planNameAdd/',
                type: 'POST',
                dataType: "json",
                contentType: 'application/x-www-form-urlencoded; charest=utf-8',
                data: {
                    "teamName": teamName,
                    "planName": planName
                },
                success: function (str) {
                    if (str.result == true) {
                        $('#team-list-'+teamName).trigger('click'); 
                        // $("#plan-list-board").empty();
                        // printPlanBoard();
                    } else {
                        alert("데이터 저장 실패");
                    }
                    $("#layerpop-plan").modal('hide');
                },
                error: function () {
                    alert("데이터 저장 실패");
                }
            })
        }
    })
}
// add plan 버튼을 클릭 시 placeholder에 팀 이름 넣기
function attrPlan() {
    $("#add-plan-btn").click(function () {
        var teamName = $("#plan-name-head").text();
        $("#team-name-plan").attr('placeholder', teamName);
        $("#team-name-plan").attr('value', teamName);
    });
}
function printPlanBoard() {
    $(".team-list-li").on("click", function () {
        printPlanFunctuon($(this).text());
    });
}

function printPlanFunctuon(teamName) {
    $("#plan-name-head").empty();
    $("#plan-name-head").append($(this).text());
    $("#plan-board-div").show();
    $("#plan-list-board").empty();
    //console.log($(this).text());
    $.ajax({
        url: '/onePage/planListClick/',
        type: 'POST',
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charest=utf-8',
        data: {
            "teamName": teamName,
            "userId": $("#hiddenUserId").val()
        },
        success: function (str) {
            console.log("플랜 데이터 가져오기 성공");
            var html =
                '<tr>' +
                '<td id="plan-board-no">No.</td>' +
                '<td id="plan-board-name">Plan Name</td>' +
                '<td id="plan-board-del-btn">Delete Plan</td>' +
                '</tr>';
            var jsonData = JSON.parse(str);
            $.each(jsonData, function (index, item) {
                html +=
                    '<tr>' +
                    '<th scope="row" id = plan-board-no-' + item.pk + '>' + item.pk + '</th>' +
                    '<td id = plan-board-name-content-' + item.pk + '>' + item.fields.teamPlanName + '</td>' +
                    '<td><button class ="btn btn-primary plan-delete-btn"  id = "plan-board-del-btn-' + item.pk + '" value = "' + item.pk + '">Delete Plan</button></td>' +
                    '</tr>';
            });
            $("#plan-name-head").append("<h1 id = 'h1-teamName'>" + teamName + "</h1>");
            //$("#plan-table-tr").append(html);

            $("#plan-list-board").append(html);
            if ($("#hiddenUserLeader").val() != "1") {
                $(".plan-delete-btn").attr("disabled", "disabled");
            }
        },
        error: function (str) {
            alert("플랜이 없습니다.");
        }
    });
}