
var xc, yc;								//原点位置
var xc_canvas, yc_canvas;	//キャンバス左上座標
var axis_x, axis_y;				//軸長さ

var x_val = [];	//x座標
var y_val = [];	//y座標

var x_pos = [];	//x座標_位置
var y_pos = [];	//y座標_位置

var context;
var context_2;

var canvas;
var canvas_2;

var img_temp = -999;	//現在描画しているラベル


function graph2() {
alert("p");
	//描画コンテキストの取得
	canvas = document.getElementById('canvas_main');
	canvas_2 = document.getElementById('canvas_sub');

	if (!canvas.getContext)return;
	if (!canvas_2.getContext)return;

	//枠線
	canvas.style.border = "1px solid #000000";
	canvas_2.style.border = "1px solid #000000";

	//キャンバスサイズ
	canvas.width  = 786;
	canvas.height = 592;

	canvas_2.width  = 786;
	canvas_2.height = 592;

	//キャンバスの位置
	canvasPos = canvas.getBoundingClientRect();
	canvasPos_2 = canvas_2.getBoundingClientRect();

	//コンテキスト
	context = canvas.getContext('2d');
	context_2 = canvas_2.getContext('2d');


	xc_canvas = canvasPos.left;
	yc_canvas = canvasPos.top;


	xc =  56;	//原点x座標
	yc = 516;	//原点y座標

				//		1			2			3				4			5				6			7			8				9			10			11		12			13
	x_val = [ 0.76,  0.76, 5.15,  5.26,  8.00, 13.95, 15.94, 17.48, 17.80, 18.95, 19.42, 20.95, 22.98];
	y_val = [17.75, 11.40, 6.80, 16.27, 10.95, 10.48, 14.70, 14.30,  7.85, 15.50, 22.38, 15.20, 16.34];

	y_min = 2;
	y_max = 26;

	x_min = 0;
	x_max = 23;

	//軸長さ
	axis_x = 666;
	axis_y = 470;

	//x軸
	context.beginPath();
	context.strokeStyle = "rgb(255, 0, 0)";
	context.moveTo(xc, yc);
	context.lineTo(xc+axis_x, yc);
	context.stroke();

	//y軸
	context.beginPath();
	context.strokeStyle = "rgb(255, 0, 0)";
	context.moveTo(xc, yc);
	context.lineTo(xc, yc-axis_y);
	context.stroke();

	//データ
	for(i=0;i<x_val.length;i++){
		x_pos[i] = xc + x_val[i] / (x_max - x_min) * axis_x;
		y_pos[i] = yc - y_val[i] / (y_max - y_min) * axis_y;
//		alert(i + "(" + x_pos[i] + "," + y_pos[i] + ")" );
	}

//	for(i=0;i<x_val.length;i++){
//		context_2.beginPath();
//		context_2.fillStyle = 'rgb(192, 80, 77)'; // 赤
//		context_2.arc(x_pos[i], y_pos[i], 5, 0, Math.PI*2, true);
//		context_2.fill();
//	}


	// イベントの登録

	//phone
	if ((navigator.userAgent.indexOf('iPhone') > 0 && navigator.userAgent.indexOf( 'iPad') == -1) ||
			 navigator.userAgent.indexOf('iPod')   > 0 || navigator.userAgent.indexOf('Android') > 0) {

		//touchstart
		var event = "touchstart";
		if(canvas_2.addEventListener){
			canvas_2.addEventListener(event, function(event) {
				event.preventDefault();
			});
		}else if(canvas_2.attachEvent){
			canvas_2.attachEvent("on" + event, function(event) {
				event.preventDefault();
			});
		}

		//touchmove
		var event = "touchmove";
		if(canvas_2.addEventListener){
			canvas_2.addEventListener('touchmove', touchPosition);
		}else if(canvas_2.attachEvent){
			canvas_2.addEventListener('touchmove', touchPosition);
		}

	//pc
	} else {
		var event = "mousemove";
		if(canvas_2.addEventListener){
			canvas_2.addEventListener(event , clickPosition);
		}else if(canvas_2.attachEvent){
			canvas_2.attachEvent("on" + event, clickPosition);
		}
	}

}

///////////////////////////////////////////////////////
//イベント処理

//スマホ
function touchPosition( e ){

	touches = event.touches;	//マルチタッチの場合、タッチ箇所がリストで取得されます。
	var i, len = touches.length;
	for (i = 0; i < len; i++) {
		var touch = touches[i];
		var px = touch.pageX;
		var py = touch.pageY;
	}

	document.form.t1.value=px+","+py;
	canvasRefresh(px, py);	//グラフ更新
}

//マウス
function clickPosition( e ){

	// イベントオブジェクトの判定
	var e = ( e || window.event.e ) ;

	// 一般的なブラウザ
	if( e.pageX || e.pageX ){
		var x = e.pageX;
		var y = e.pageY;
	}
	// 古いブラウザ(Ie9以下)
	else if( e.clientX || e.clientY ){
		var dElm = document.documentElement , dBody = document.body ;
		var x = e.clientX + dBody.scrollLeft + dElm.scrollLeft ;
		var y = e.clientY + dBody.scrollTop + dElm.scrollTop ;
	}
	// それでもダメな場合
	else{
		return false ;
	}

	canvasRefresh(x, y);	//グラフ更新
}


//グラフ更新
function canvasRefresh(x, y){

	//キャンバス左上基準
	x2 = x - xc_canvas;
	y2 = y - yc_canvas;

	//最寄りの座標
	n = reset_x(x2, y2);
/*
	if(img_temp ==  0 && (n==0 || n==1))return;
	if(img_temp ==  2 && (n==2 || n==3))return;
	if(img_temp ==  n && (n>=4 && n<9))return;
	if(img_temp ==  9 && (n==9))return;
	if(img_temp == 10 && (n==10))return;
	if(img_temp == 11 && (n==11))return;
	if(img_temp == 12 && (n>=12))return;
*/

	//クリア
	context_2.clearRect(0, 0, canvas.width, canvas.height);

	//直線
	context_2.beginPath();
	context_2.moveTo(x_pos[n], yc);
	context_2.lineTo(x_pos[n], yc - axis_y);
	context_2.stroke();

	var img_1 = new Image();
	var img_2 = new Image();

	//画像
/*
	if(n==0 || n==1){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[0]-12, y_pos[0]-60);
		};
		img_2.onload = function() {
			context_2.drawImage(img_2, x_pos[1]-12, y_pos[1]-60);
		};
		img_1.src = "images/graph_01_1.png";
		img_2.src = "images/graph_01_2.png";
		img_temp = 0;
	}else if(n==2 || n==3){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[2]-12, y_pos[2]-60);
		};
		img_2.onload = function() {
			context_2.drawImage(img_2, x_pos[3]-12, y_pos[3]-60);
		};
		img_1.src = "images/graph_01_3.png";
		img_2.src = "images/graph_01_4.png";
		img_temp = 2;
	}else if(n>=4 && n<9){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[n]-12, y_pos[n]-60);
		};
		img_1.src = "images/graph_01_" + (n+1) + ".png";
		img_temp = n;
	}else if(n==9){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[n]-30, y_pos[n]-60);
		};
		img_1.src = "images/graph_01_" + (n+1) + ".png";
		img_temp = 9;
	}else if(n==10){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[n]-34, y_pos[n]+3);
		};
		img_1.src = "images/graph_01_" + (n+1) + ".png";
		img_temp = 10;
	}else if(n==11){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[n]-90, y_pos[n]-60);
		};
		img_1.src = "images/graph_01_" + (n+1) + ".png";
		img_temp = 11;
	}else if(n>=12){
		img_1.onload = function() {
			context_2.drawImage(img_1, x_pos[n]-150, y_pos[n]-60);
		};
		img_1.src = "images/graph_01_" + (n+1) + ".png";
		img_temp = 12;
	}

	img_1 = null;
	img_2 = null;
*/


	if(n==0 || n==1){
		img_1.src = "images/graph_01_1.png?" + new Date().getTime();
		img_2.src = "images/graph_01_2.png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[0]-12, y_pos[0]-60);
		context_2.drawImage(img_2, x_pos[1]-12, y_pos[1]-60);
		img_temp = 0;
	}else if(n==2 || n==3){
		img_1.src = "images/graph_01_3.png?" + new Date().getTime();
		img_2.src = "images/graph_01_4.png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[2]-12, y_pos[2]-60);
		context_2.drawImage(img_2, x_pos[3]-12, y_pos[3]-60);
		img_temp = 2;
	}else if(n>=4 && n<9){
		img_1.src = "images/graph_01_" + (n+1) + ".png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[n]-12, y_pos[n]-60);
		img_temp = n;
	}else if(n==9){
		img_1.src = "images/graph_01_" + (n+1) + ".png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[n]-30, y_pos[n]-60);
		img_temp = 9;
	}else if(n==10){
		img_1.src = "images/graph_01_" + (n+1) + ".png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[n]-34, y_pos[n]+3);
		img_temp = 10;
	}else if(n==11){
		img_1.src = "images/graph_01_" + (n+1) + ".png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[n]-90, y_pos[n]-60);
		img_temp = 11;
	}else if(n>=12){
		img_1.src = "images/graph_01_" + (n+1) + ".png?" + new Date().getTime();
		context_2.drawImage(img_1, x_pos[n]-150, y_pos[n]-60);
		img_temp = 12;
	}


}


//最寄りのx座標を探す
function reset_x(x, y){

	n=-1;
	dx_max = 9999;
	for(i=0;i<x_pos.length;i++){
		dx = Math.abs(x - x_pos[i]);
		if(dx < dx_max){
			n = i;
			dx_max = dx;
		}
	}
	return n;
}

/*
function gHover(id){

	for(i=1;i<=25;i++)
		document.getElementById(("g2_" + i)).style.opacity = "0.0";

	document.getElementById(id).style.opacity = "1.0";
}

*/
