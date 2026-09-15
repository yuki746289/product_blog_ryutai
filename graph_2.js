/////////////////////////////////////////////////////////////////////
//スクロールイベント

var vFlag = true;

window.onscroll = function(){

	//現在位置の取得
	var dElm = document.documentElement;
	var dBody = document.body;

	var nX = dElm.scrollLeft || dBody.scrollLeft ;	// 現在位置のX座標
	var nY = dElm.scrollTop  || dBody.scrollTop ;		// 現在位置のY座標

	document.form.pos.value = nX + ":" + nY;

	if(nY >= 3100 && vFlag == true){
		vFlag = false;
		view();
	}

}

/////////////////////////////////////////////////////////////////////
//タイマー処理

var vCount = 100;		//繰り返し回数[回]
var vInterval = 4;	//繰り返し間隔[msec]
var vTemp;

function view(){

	vTemp = 0;

	//繰り返し処理
	var onInterval = function(){
		graph(vTemp);
		vTemp += 1;
		if(vTemp > vCount)vTemp = vCount;	//増えすぎた時
	};

	var interval = setInterval(onInterval,vInterval);

	//終了処理
	var onTimeout = function(){
		clearInterval(interval);
		graph(vCount);	//処理:足りなかった時
	}
	setTimeout(onTimeout,vInterval * vCount); // <- 10秒より長く11秒より短い時間を指定

}


/////////////////////////////////////////////////////////////////////
//グラフ描画
function graph(vTemp){

	document.form.vTemp.value = vTemp;

	for(i=0;i<x_val.length;i++){
		context.beginPath();
		context.fillStyle = 'rgb(144, 198, 227)';
		context.fillRect(x_pos[i], y_pos[0], 10, -(y_pos[0] - y_pos[i]) * vTemp / vCount);
		context.stroke();
	}
}


/////////////////////////////////////////////////////////////////////
//window.onload
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


window.onload = function(){

	//描画コンテキストの取得
	canvas = document.getElementById('canvas_main');
	canvas_2 = document.getElementById('canvas_sub');

	if (!canvas.getContext)return;
	if (!canvas_2.getContext)return;

	//枠線
	canvas.style.border = "1px solid #000000";
	canvas_2.style.border = "1px solid #000000";

	//キャンバスサイズ
	canvas.width  = 800;
	canvas.height = 500;

	canvas_2.width  = 800;
	canvas_2.height = 500;

	//キャンバスの位置
	canvasPos = canvas.getBoundingClientRect();
	canvasPos_2 = canvas_2.getBoundingClientRect();

	//コンテキスト
	context = canvas.getContext('2d');
	context_2 = canvas_2.getContext('2d');


	xc_canvas = canvasPos.left;
	yc_canvas = canvasPos.top;


	xc =  50;	//原点x座標
	yc = 450;	//原点y座標

	x_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
	y_val = [101.0, 108.0, 127.0, 164.0, 225.0, 316.0, 443.0, 612.0, 829.0, 1100.0, 1431.0, 1828.0, 2297.0, 2844.0, 3475.0, 4196.0, 5013.0, 5932.0, 6959.0, 8100.0];


	y_min = 0;		//最小値
	y_max = 9000;	//最大値

	x_min = 0;		//最小値
	x_max = 20;		//最大値

	//軸長さ
	axis_x = 700;
	axis_y = 400;

	//x軸
	context.beginPath();
	context.moveTo(xc, yc);
	context.lineTo(xc+axis_x, yc);
	context.stroke();

	//y軸
	context.beginPath();
	context.moveTo(xc, yc);
	context.lineTo(xc, yc-axis_y);
	context.stroke();

	//データ
	for(i=0;i<x_val.length;i++){
		x_pos[i] = xc + x_val[i] / (x_max - x_min) * axis_x;
		y_pos[i] = yc - y_val[i] / (y_max - y_min) * axis_y;
//		alert(i + "(" + x_pos[i] + "," + y_pos[i] + ")" );
	}


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


//イベント処理:スマホ
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


//イベント処理:pc
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

	canvasRefresh(x, y);	//現在位置更新
}


//現在位置更新
function canvasRefresh(x, y){

	//キャンバス左上基準
	x2 = x - xc_canvas;
	y2 = y - yc_canvas;

	//x座標補正
	n = reset_x(x2, y2);


	//クリア
	context_2.clearRect(0, 0, canvas.width, canvas.height);

	//直線描画
	context_2.beginPath();
	context_2.moveTo(x_pos[n], yc);
	context_2.lineTo(x_pos[n], yc - axis_y);
	context_2.stroke();

	//円描画
	context_2.beginPath();
	context_2.arc(x_pos[n], y_pos[n], 5, 0, Math.PI*2, true);
	context_2.fill();

	//テキスト
	context_2.fillStyle = "black";
	context_2.font = "20px 'ＭＳ ゴシック'";
	context_2.textAlign = "left";
	context_2.textBaseline = "top";

	//塗りつぶしのテキストを、座標(20, 75)の位置に最大幅200で描画する
	context_2.fillText("値 "+y_val[n], x_pos[n]-20, y_pos[n]-30, 200);
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
