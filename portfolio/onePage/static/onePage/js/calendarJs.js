/* @author wookim
<<<<<<< HEAD
 */
dt = new Date();
//현재 달
nowMonth = dt.getMonth() + 1;
//오늘 요일
nowDay = dt.getDate();
//올해 년도 
nowYear = dt.getFullYear();
var userId = ""
$(document).ready(function () {
	//달력 계산
	calcCalendar(nowYear, nowMonth);
	//년도 올해로 설정
	selectYearList(nowYear);
	//달 현재 달로 설정
	selectMonthList(nowMonth);
	//달력 출력 함수
	printYearMonth(nowYear, nowMonth);
	//좋아요 버튼 숨기기
	hiddenAllBut();
	//좋아요 버튼 눌렀을 때 년도 저장 하기 이벤트
	clickBut();

	$("#userIdSave").click(function () {
		if ($("#userIdInput").val() != ""|| userId == '') {
			userId = $("#userIdInput").val();
		} else {
			alert("아이디를 입력하세요!")
		}
	})

	var year = String(nowYear).substring(2, 4);
	//좋아요 및 좋아요 누른 회원 아이디 출력 함수
	printSelectDateAjax(Number(year), nowMonth);
	//아이디 호버 이벤트 등록
	idHover();

	//팀장 + 부팀장만 보이는 저장하기 버튼 이벤트
	if ($("#save").length) {
		$("#save").click(function () {
			if ($("#save").val() == "일정확정") {
				$("#save").val("취소");

			} else {
				$("#save").val("일정확정");
				// $(".date").css("background-color", "white");
			}

			$(".date").hover(
				// 마우스 들어 왔을 떄
				function () {
					if ($("#save").val() == "취소") {
						// $(this).css("background-color", "green");
						var num = $(this).attr("value");
						$("#dateButton" + num).html("일정저장");
					}
				},
				// 마우스 나갈 때
				function () {
					if ($("#save").val() == "취소") {
						// $(this).css("background-color", "white");
						var num = $(this).attr("value");
						// console.log(num);
						$("#dateButton" + num).html("좋아요");

						//$(".date")
					}
				})
		})
	}

	/*
	 * 해당 문서 로딩 이후 ajax를 이용하여 mananagePlanController에 loadCalendar.manageplan로
	 * 맴핑되는 메소드가 실행되고 해당 메소드는 db에 접속하여 해당 일정에 날짜를 선택한 데이터를 가져와서 뿌려준다.
	 */
});
//좋아요 누른 회원 아이디 마우스 호버 이벤트
function idHover() {
	$(".date").hover(
		//마우스 들어올때
		function () {
			$(this).children(".viewSc").children(".bindD").children('.id').css('visibility', 'visible');
		},
		//마우스 나갈 때
		function () {
			$(this).children(".viewSc").children(".bindD").children(".id").css('visibility', 'hidden');
		})
}
//좋아요 누른 회원 아이디 감추기
function idHide() {
	$(".id").css('visibility', 'hidden');
}


//좋아요 누른 수 보여주는 메소드 + 누른 아이디 보여주는 메소드
function printSelectDateAjax(year, month) {
	//html 초기화
	$(".countDate").html("");
	$(".id").html("");
	//div 추가
	var output = "<div class = 'id'>";
	//배열 추가
	var dayList = new Array();

	//ajax 컨트롤러에서 데이터 받아와 아이디 뿌려주기
	$.ajax({
		url: '/onePage/getMemberId/',
		type: 'POST',
		dataType: "json",
		contentType: 'application/x-www-form-urlencoded; charest=utf-8',
		success: function (str) {
			$.each(str, function (index, item) {
				//디비에 저장된 selectDate 년도, 월 추출
				var yearSub = Number(item.selectDate.substring(0, 2));
				var monthSub = Number(item.selectDate.substring(3, 5));
				//화면에 선택된 년, 월  == 디비 selectDate 일치 할 때만 실
				if (yearSub == year && monthSub == Number(month)) {
					//selectDate 날짜 추출
					day = Number(item.selectDate.substring(6, 8));
					//처음 실행 될 때
					if (dayList.length == 0) {
						//배열에 날짜 삽입
						dayList.push(day);
						//태그에 id 삽입
						output += String(item.userId);
						output += "<br/>"
						//처음 실행이 아니고, 배열에 넣은 날짜와 지금 읽은 day값 비교하여 같을 때 (같은 날을 추가 한 유저가 아직 있을 때)
					} else if (day == dayList[dayList.length - 1]) {
						dayList.push(day);
						output += String(item.userId);
						output += "<br/>"
						//처음 실행이 아니고,배열에 넣은 날짜와 지금 읽은 day값 비교하여 다를 때(같은 날을 추가한 유저가 없을 때)
					} else if (day != dayList[dayList.length - 1]) {
						//td 태그에 아이디들 html 삽입하기
						output += "</div>"
						$("#bind" + dayList[dayList.length - 1]).append(output);
						dayList.push(day);
						output = "<div class = 'id'>"
						output += String(item.userId);
						output += "<br/>"
					}
				}
			})
			//마지막에 추가된 아이디 추가 해주기
			output += "</div>"
			$("#bind" + dayList[dayList.length - 1]).append(output);
			//아이디 숨기기
			$(".id").css('visibility', 'hidden');
		},
		error: function () {
			alert("통신실패");
		}
	})
	//디비에 저장된 좋아요 수 읽어와 태그에 +n 추가하기
	$.ajax({
		url: '/onePage/loadCalendar/',
		type: 'POST',
		dataType: "json",
		contentType: 'application/x-www-form-urlencoded; charest=utf-8',
		success: function (str) {
			$.each(str, function (index, item) {
				var yearSub = Number(item.selectDate.substring(0, 2));
				var monthSub = Number(item.selectDate.substring(3, 5));
				var day;
				var output = ""

				if (yearSub == year && monthSub == Number(month)) {
					day = Number(item.selectDate.substring(6, 8));
					output += '<div class = "countDate">';
					output += '+' + String(item.dateCount);
					output += '</div>';
					//해당 좋아요 수를 td태그에 삽입하기
					$('#bind' + day).append(output);
					//확정 일때 색 수정하기
					if (item.confirmIndicator == 1) {
						$("#bind" + day).css("background-color", "green");
					}
				}
			});
		},
		error: function () {

			alert("통신실패");
		}
	});
}


// 마우스가 밖으로 나갔을 때 좋아요 버튼 숨기기 이벤트
function hiddenBut(day) {
	$("#dateButton" + day).css('visibility', 'hidden');
}

// 모든 버튼 숨기기 이벤트
function hiddenAllBut() {
	$(".goodBut").css('visibility', 'hidden');
}

// 마우스 안으로 들어오묜 좋아요 버튼 보이기 이벤트
function showBut(day) {
	$("#dateButton" + day).css('visibility', 'visible');
}

// 좋아요 버튼 눌렀을 때 년도 저장 하기 이벤트
function clickBut() {
	$(".goodBut").on("click", function () {
		var yearSelect = $("#listYear").val();
		var monthSelect = $("#listMonth").val();
		var daySelect = $(this).val();
		var date;
		var year;
		//2100년보다 이전이면
		if (yearSelect < 2100) {
			date = yearSelect.substring(2, 4);
			year = date;
		} else {
			//이상이면 2글자가 아닌 3글자를 추출
			date = yearSelect.substring(1, 4);
			year = date;
		}
		//한자리 달이라면 0추가
		if (monthSelect < 10) {
			date = date + '/0' + String(monthSelect);
			//아니면 그냥 추가
		} else {
			date = date + '/' + String(monthSelect);
		}
		//날도 마찬가지
		if (daySelect < 10) {
			date = date + '/0' + String(daySelect);
		} else {
			date = date + '/' + String(daySelect);
		}

		//저장하기 버튼이 없거나, 저장하기 버튼이 있어도 눌르지 않았을 때
		if ((!$("#save").length || $("#save").val() == "일정확정") && userId != "") {
			//
			console.log(userId);
			var ID = userId;
			$.ajax({
				url: "/onePage/selectCalendar/",
				type: "POST",
				contentType: 'application/x-www-form-urlencoded; charsert=utf-8',
				dataType: "json",
				data: {
					"selectDate": date,
					"user_ID": ID
				},
				success: function (map) {
					//좋아요 누른 수 보여주는 메소드 + 누른 아이디 보여주는 메소드
					printSelectDateAjax(Number(year), Number(monthSelect));
				},
				erorr: function () {
					alert("출력실패");
				}
			})
			//저장하기 버튼이 있고, 한번 눌렀을 때
		} else if (userId != "") {
			//일정 확정하기 버튼을 눌렀을 때 해당 버튼의 번호 가져오기
			var num = $(this).attr("value");
			//만약 누른 버튼의 바탕 색이 초록색이 아니면 (일정확정 안한 날 -일정 저장)
			if ($("#bind" + num).css("background-color") != "rgb(0, 128, 0)") {
				//바탕색을 초록색으로 바꾸기
				$("#bind" + num).css("background-color", "green");
				//ajax로 선택한 날 서버로 전송하기
				$.ajax({
					url: "/onePage/fixcal/",
					type: "POST",
					contentType: 'application/x-www-form-urlencoded; charsert=utf-8',
					dataType: "json",
					data: {
						"selectDate": date,
						"userId ": userId
					},
					success: function (map) {
						// alert(map.res);
					},
					erorr: function () {
						alert("일정 확정 실패");
					}
				})
				//만약 누른 버튼의 바탕 색이 초록색이면 (이미 확정난 날이면 - 저장 취소)
			} else {
				//배경색 흰색으로 
				$("#bind" + num).css("background-color", "white");
				//ajax로 선택한 날 서버로 전송
				$.ajax({
					url: "/onePage/fixcal/",
					type: "POST",
					contentType: 'application/x-www-form-urlencoded; charsert=utf-8',
					dataType: "json",
					data: {
						"selectDate": date,
						"userId ": userId
					},
					success: function (map) {
						// alert(map.res);
					},
					erorr: function () {
						alert("일정 확정 실패");
					}
				})
			}
		} else {
			alert("아이디를 입력하세요!")
		}
	});
}

// 현재 날짜와 윤달, 해당 월의 일수 계산
function Calendar() {
	// 윤달 판단
	this.calYun = function (year) {
		var yun = false;
		if (year % 4 == 0 && year % 400)

			if (year % 4 == 0) {
				yun = true;
			} else if (year % 100 == 0) {
				if (year % 400 == 0) {
					yun = true;
				}
				yun = false;
			} else {
				yun = false;
			}
		return yun;
	}
	// 해당 월의 일수
	this.totMonthDay = function (mon, yun) {
		var days = 0;

		if (mon < 8 && mon % 2 == 1) {
			days = 31;
		} else if (mon == 2 && yun == true) {
			// console.log("day : " + days + " yun : " + yun);
			days = 29;
		} else if (mon == 2 && yun == false) {
			// console.log("day : " + days + " yun : " + yun);
			days = 28;
		} else if (mon > 7 && mon % 2 == 0) {
			days = 31;
		} else {
			days = 30;
		}
		return days;
	}
}

// 달력생성 및 비어있는 칸 생성
function calcCalendar(year, month) {
	var calendar = new Calendar();
	var calendarDiv = document.getElementById('calendar');
	var html =
		'<table class ="table" id="cal">' +
		'<thead>' +
		'<tr id = "calHead">' +
		'<th class =claTh id = "sun">Sun</th>' +
		'<th class =claTh>Mon</th>' +
		'<th class =claTh>Tue</th>' +
		'<th class =claTh>Wen</th>' +
		'<th class =claTh>Thu</th>' +
		'<th class =claTh>Fri</th>' +
		'<th class =claTh id = "sat">Sat</th>' +
		'</tr>' +
		'</thead>';
	// 계산하고자 하는 연도와 월을 날짜 객체에 지정
	dt.setYear(Number(year));
	dt.setMonth(Number(month) - 1);
	var totMonth = calendar.totMonthDay(month, calendar.calYun(year));
	// 날짜 표시 반복문
	html += '<tbody>'
	for (var day = 1; day <= totMonth; day++) {
		dt.setDate(day);

		// 달력 1주차 빈칸생성 로직
		if (day == 1) {
			for (var num = 0; num < dt.getDay(); num++) {
				html += '<td></td>';
			}
		}
		// 일요일이 아니라면 날짜를 표시하고 일요일이라면 날짜를 표시한 후 줄바꿈
		if (dt.getDay() != 6) {
			html += '<td class = "date" id = "dateTd' + String(day)
				+ '" value = ' + String(day) + ' onmouseover = "showBut('
				+ String(day) + ')" onmouseout = "hiddenBut(' + String(day)
				+ ')">' + '<div class =viewSc><div class = bindD id = bind' + String(day) + '>' + String(day) + '<br/>'
				+ '<button class= "goodBut btn btn-primary" id = "dateButton' + String(day)
				+ '" value =' + String(day) + '>' + "좋아요" + '</button></div></div>'
				+ '</td>';
		} else {
			html += '<td class = "date" id = "dateTd' + String(day)
				+ '" value = ' + String(day) + ' onmouseover = "showBut('
				+ String(day) + ')" onmouseout = "hiddenBut(' + String(day)
				+ ')">' + '<div class =viewSc><div class = bindD id = bind' + String(day) + '>' + String(day) + '<br/>'
				+ '<button class= "goodBut btn btn-primary" id = "dateButton' + String(day)
				+ '"  value =' + String(day) + '>' + '좋아요' + '</button></div></div>'
				+ '</td></tr>' + '<tr>';
		}
	}
	var addBoxNum = dt.getDay() - 1;
	if (addBoxNum == 6) {
		addBoxNum = 0;
	}
	if (addBoxNum != 5) {
		for (var i = addBoxNum; i < 5; i++) {
			html += '<td></td>';
		}
	}

	html += '</table>'

	calendarDiv.innerHTML = html;
}

// 현재 년도부터 10년치 년도 선택
function selectYearList(year) {
	// 현재 날짜 속성으로 지정
	var html = '<select class="form-control" id = "yearList" onchange="selectYearChange()">';
	//dt = new Date();
	year = year - 5;
	for (var i = 0; i < 10; i++) {
		if (i == 5) {
			html += '<option id = "listYear" value = ' + year + ' selected>'
				+ year + "년" + '</option>';
		} else {
			html += '<option value = ' + year + '>' + year + "년" + '</option>';
		}
		year++;
	}
	html += '</select>';
	document.getElementById('nowYear').innerHTML = html;
}

// 현재 월 부터 12월 까지
function selectMonthList(month) {
	var html = '<select class="form-control" id = "monthList" onchange="selectMonthChange()">';
	for (var i = 1; i <= 12; i++) {
		if (i != month) {
			html += '<option value = ' + i + '>' + i + '월' + '</option>';
		} else if (i == month) {

			html += '<option id = "listMonth" value = ' + i + ' selected>' + i
				+ '월' + '</option>';
		}
	}

	html += '</select>';
	document.getElementById('nowMonth').innerHTML = html;
}

// 셀렉트 년도 변경 이벤트
function selectYearChange() {

	var yearSelect = document.getElementById("yearList");
	var monthSelect = document.getElementById("monthList");
	// select element에서 선택된 option의 value가 저장된다.
	var yearVal = yearSelect.options[yearSelect.selectedIndex].value;
	var monthVal = monthSelect.options[monthSelect.selectedIndex].value;

	calcCalendar(yearVal, monthVal)
	selectYearList(yearVal);
	selectMonthList(monthVal);
	printYearMonth(yearVal, monthVal);
	hiddenAllBut();
	clickBut();
	var year = String(yearVal).substring(2, 4);
	printSelectDateAjax(year, monthVal);
	idHover()
}
// 셀렉트 월 변경 이벤트 '<select id = "monthList" onchange="selectMonthChange()">';

function selectMonthChange() {
	hiddenAllBut();
	var yearSelect = document.getElementById("yearList");
	var monthSelect = document.getElementById("monthList");
	// select element에서 선택된 option의 value가 저장된다.
	var yearVal = yearSelect.options[yearSelect.selectedIndex].value;
	var month = monthSelect.options[monthSelect.selectedIndex].value;

	// select element에서 선택된 option의 value가 저장된다.
	// console.log("change month _ year : " + year);
	// console.log("change month _ month : " + month);

	calcCalendar(yearVal, month);
	selectYearList(yearVal);
	selectMonthList(month);
	printYearMonth(yearVal, month);
	hiddenAllBut();
	clickBut();

	var year = String(yearVal).substring(2, 4);
	printSelectDateAjax(year, month);
	idHover();

}

// 달력 출력 함수
function printYearMonth(year, month) {
	// var html = '<h3>' + String(year) + '년 ' + String(month) + '월' + '</h3>';
	// // console.log(html);
	// document.getElementById('calendarDiv').innerHTML = html;
}