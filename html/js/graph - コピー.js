
var xc, yc;								//原点位置
var xc_canvas, yc_canvas;	//キャンバス左上座標
var axis_x, axis_y;				//軸長さ

var x_val = [];	//x座標
var y_val = [];	//y座標

var x_pos = [];	//x座標_位置
var y_pos = [];	//y座標_位置

var context_2;

var canvas_2;


function graph() {


	//描画コンテキストの取得
	canvas_2 = document.getElementById('canvas_sub');

	if (!canvas_2.getContext)return;

	//枠線
	canvas_2.style.border = "1px solid #000000";


	//キャンバスサイズ
	graph_01 = document.getElementById('graph_01');

//	canvas_2.width  = 786;
//	canvas_2.height = 592;

//	canvas_2.width = graph_01.style.width;
//	canvas_2.width = graph_01.outerWidth(true);
//	canvas_2.width = graph_01.outerWidth;
//	canvas_2.width = graph_01.innerWidth;
//	canvas_2.width = graph_01.clientWidth;
	canvas_2.width = graph_01.offsetWidth;

//	canvas_2.height = graph_01.style.height;
//	canvas_2.width = graph_01.outerHeight(true);
//	canvas_2.width = graph_01.outerHeight;
//	canvas_2.height = graph_01.innerHeight;
//	canvas_2.height = graph_01.clientHeight;
	canvas_2.height = graph_01.offsetHeight;

	//キャンバスの位置オブジェクト
	canvasPos_2 = canvas_2.getBoundingClientRect();

	//コンテキスト
	context_2 = canvas_2.getContext('2d');

	//キャンバス左上座標
	xc_canvas = canvasPos_2.left;
	yc_canvas = canvasPos_2.top;

	//原点
	xc = canvas_2.width  * 0.0712;	//原点x座標:56
	yc = canvas_2.height * 0.8716;	//原点y座標:516


	//座標
				//		1			2			3				4			5				6			7			8				9			10			11		12			13
	x_val = [ 0.76,  0.75, 5.15,  5.26,  8.00, 13.95, 15.94, 17.48, 17.80, 18.95, 19.42, 20.95, 22.98];
	y_val = [17.75, 11.40, 6.80, 16.27, 10.95, 10.48, 14.70, 14.30,  7.85, 15.50, 22.38, 15.20, 16.34];

	y_min = 2;
	y_max = 26;

	x_min = 0;
	x_max = 23;

	//軸長さ
	axis_x = canvas_2.width  * 0.8473;	//666
	axis_y = canvas_2.height * 0.7939;	//470

	//x軸
//	context_2.beginPath();
//	context_2.strokeStyle = "rgb(255, 0, 0)";
//	context_2.moveTo(xc, yc);
//	context_2.lineTo(xc+axis_x, yc);
//	context_2.stroke();

	//y軸
//	context_2.beginPath();
//	context_2.strokeStyle = "rgb(255, 0, 0)";
//	context_2.moveTo(xc, yc);
//	context_2.lineTo(xc, yc-axis_y);
//	context_2.stroke();

	//座標
	for(i=0;i<x_val.length;i++){
		x_pos[i] = xc + x_val[i] / (x_max - x_min) * axis_x;
		y_pos[i] = yc - y_val[i] / (y_max - y_min) * axis_y;
//		alert(i + "(" + x_pos[i] + "," + y_pos[i] + ")" );
	}


	//表示
	canvasRefresh(xc, yc);	//左上座標




//////////////////////////////////////////////////////////////////////////////////////
//	テーブル

	var context_3;
	var canvas_3;


	//描画コンテキストの取得
	canvas_3 = document.getElementById('canvas_table');

	if (!canvas_3.getContext)return;

	//枠線
	canvas_3.style.border = "1px solid #000000";

	//キャンバスサイズ
	table_01 = document.getElementById('table_01');

	canvas_3.width  = table_01.offsetWidth;
	canvas_3.height = table_01.offsetHeight;

	//キャンバスの位置オブジェクト
	canvasPos_3 = canvas_3.getBoundingClientRect();

	//コンテキスト
	context_3 = canvas_3.getContext('2d');

	//キャンバス左上座標
	xt_canvas = canvasPos_3.left;
	yt_canvas = canvasPos_3.top;

	//原点
	xt = canvas_3.width  * 0.0712;	//原点x座標:56
	yt = canvas_3.height * 0.8716;	//原点y座標:516


alert(xt + ":" + yt);



	/////////////////////////////////////////////////////////////////////////////
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


		/////////////////////////////////////////////

		//touchstart
		var event = "touchstart";
		if(canvas_3.addEventListener){
			canvas_3.addEventListener(event, function(event) {
				event.preventDefault();
			});
		}else if(canvas_3.attachEvent){
			canvas_3.attachEvent("on" + event, function(event) {
				event.preventDefault();
			});
		}

		//touchmove
		var event = "touchmove";
		if(canvas_3.addEventListener){
			canvas_3.addEventListener('touchmove', alert("pass"));
		}else if(canvas_3.attachEvent){
			canvas_3.addEventListener('touchmove', alert("pass"));
		}


	/////////////////////////////////////////////////////////////////////////////
	//pc
	} else {
		var event = "mousemove";
		if(canvas_2.addEventListener){
			canvas_2.addEventListener(event , clickPosition);
		}else if(canvas_2.attachEvent){
			canvas_2.attachEvent("on" + event, clickPosition);
		}

		/////////////////////////////////////////////
		var event = "mousemove";
		if(canvas_3.addEventListener){
			canvas_3.addEventListener(event , alert("p"));
		}else if(canvas_3.attachEvent){
			canvas_3.attachEvent("on" + event, alert("p"));
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

//	document.form.t1.value=px+","+py;
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

	//クリア
	context_2.clearRect(0, 0, canvas_2.width, canvas_2.height);

	//直線
	context_2.beginPath();
	context_2.lineWidth = 2;
	context_2.strokeStyle = "rgb(181, 181, 181)";
	context_2.moveTo(x_pos[n], yc);
	context_2.lineTo(x_pos[n], yc - axis_y);
	context_2.stroke();

	//値
	for(i=0;i<x_val.length;i++){
		context_2.beginPath();
		context_2.fillStyle = 'rgb(0, 0, 0)';
		context_2.arc(x_pos[i], y_pos[i], 5, 0, Math.PI*2, true);
		context_2.fill();
	}

	//画像
	if(n==0){

		xp = x_pos[0]-15;
		yp = y_pos[0]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 195, 43, 8, 30);

		//テキスト描画
		t1 = 'オプショアファンドC';
		t2 = 'リスク１.４４％　リターン１３.７％';
		drowText_1(t1, t2, xp+40, yp-h+18, xp+5, yp-h+33);

	}else if(n==1){

		xp = x_pos[1]-15;
		yp = y_pos[1]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 195, 43, 8, 30);

		//テキスト描画
		t1 = 'オプショアファンドA';
		t2 = 'リスク１.０２％　リターン８.００％';
		drowText_1(t1, t2, xp+40, yp-h+18, xp+5, yp-h+33);

	}else if(n==2){

		xp = x_pos[2]-15;
		yp = y_pos[2]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 195, 43, 8, 30);

		//テキスト描画
		t1 = '米国債';
		t2 = 'リスク５.０７％　リターン５.５２％';
		drowText_1(t1, t2, xp+80, yp-h+18, xp+5, yp-h+33);

	}else if(n==3){

		xp = x_pos[3]-15;
		yp = y_pos[3]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 30);

		//テキスト描画
		t1 = 'オプショアファンドB';
		t2 = 'リスク５.１６％　リターン１１.２１％';
		drowText_1(t1, t2, xp+50, yp-h+18, xp+5, yp-h+33);

	}else if(n==4){

		xp = x_pos[4]-15;
		yp = y_pos[4]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 198, 43, 8, 30);

		//テキスト描画
		t1 = '米国ハイイールド債';
		t2 = 'リスク７.２１％　リターン７.１０％';
		drowText_1(t1, t2, xp+50, yp-h+18, xp+5, yp-h+33);

	}else if(n==5){

		xp = x_pos[5]-15;
		yp = y_pos[5]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 30);

		//テキスト描画
		t1 = 'REIT';
		t2 = 'リスク１４.１０％　リターン７.５５％';
		drowText_1(t1, t2, xp+85, yp-h+18, xp+5, yp-h+33);

	}else if(n==6){

		xp = x_pos[6]-15;
		yp = y_pos[6]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 30);

		//テキスト描画
		t1 = '米国大型株';
		t2 = 'リスク１６.１２％　リターン９.０６％';
		drowText_1(t1, t2, xp+70, yp-h+18, xp+5, yp-h+33);

	}else if(n==7){

		xp = x_pos[7]-15;
		yp = y_pos[7]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 30);

		//テキスト描画
		t1 = '世界株';
		t2 = 'リスク１７.５７％　リターン９.０３％';
		drowText_1(t1, t2, xp+80, yp-h+18, xp+5, yp-h+33);

	}else if(n==8){

		xp = x_pos[8]-15;
		yp = y_pos[8]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 30);

		//テキスト描画
		t1 = 'コモディティ（商品）';
		t2 = 'リスク１７.８９％　リターン６.２４％';
		drowText_1(t1, t2, xp+50, yp-h+18, xp+5, yp-h+33);

	}else if(n==9){

		xp = x_pos[9]-30;
		yp = y_pos[9]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 45);

		//テキスト描画
		t1 = '米国中型株';
		t2 = 'リスク１９.０９％　リターン９.５４％';
		drowText_1(t1, t2, xp+75, yp-h+18, xp+5, yp-h+33);

	}else if(n==10){

		xp = x_pos[10]-60;
		yp = y_pos[10]+60;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_2(xp, yp, 215, 43, 8, 75);

		//テキスト描画
		t1 = 'オフショアファンドD';
		t2 = 'リスク１９.４４％　リターン２５.４０％';
		drowText_1(t1, t2, xp+60, yp-h+18, xp+5, yp-h+33);

	}else if(n==11){

		xp = x_pos[11]-100;
		yp = y_pos[11]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 205, 43, 8, 115);

		//テキスト描画
		t1 = '米国小型株';
		t2 = 'リスク２１.０７％　リターン９.４７％';
		drowText_1(t1, t2, xp+75, yp-h+18, xp+5, yp-h+33);

	}else if(n==12){

		xp = x_pos[12]-160;
		yp = y_pos[12]-18;
		h = 43;

		//drowHukidashi_1(xp, yp, w, h, dx, p)
		//w:幅, h:高さ, dx:矢印幅, p:矢印位置
		drowHukidashi_1(xp, yp, 215, 43, 8, 175);

		//テキスト描画
		t1 = '新興国株';
		t2 = 'リスク２２.５３％　リターン１０.５７％';
		drowText_1(t1, t2, xp+90, yp-h+18, xp+5, yp-h+33);

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


//吹き出し描画
function drowHukidashi_1(xp, yp, w, h, dx, p){
		context_2.beginPath();
		context_2.fillStyle = 'rgb(63, 63, 63)';
		context_2.moveTo(xp  , yp);
		context_2.lineTo(xp  , yp-h);
		context_2.lineTo(xp+w, yp-h);
		context_2.lineTo(xp+w, yp  );
		context_2.lineTo(xp+p   ,yp  );		//矢印
		context_2.lineTo(xp+p-15,yp+15);	//矢印
		context_2.lineTo(xp+p-dx,yp);			//矢印
		context_2.fill();
}


//吹き出し描画
function drowHukidashi_2(xp, yp, w, h, dx, p){
		context_2.beginPath();
		context_2.fillStyle = 'rgb(63, 63, 63)';
		context_2.moveTo(xp  , yp);
		context_2.lineTo(xp  , yp-h);
		context_2.lineTo(xp+p   ,yp-h  );		//矢印
		context_2.lineTo(xp+p-15,yp-h-15);	//矢印
		context_2.lineTo(xp+p-dx,yp-h);			//矢印
		context_2.lineTo(xp+w, yp-h);
		context_2.lineTo(xp+w, yp  );
		context_2.fill();
}


//テキスト秒描画
function drowText_1(t1, t2, t1x, t1y, t2x, t2y){
		context_2.font = "11px 'メイリオ'";
		context_2.fillStyle = "rgb(200, 200, 200)";
		context_2.fillText(t1,t1x,t1y);
		context_2.fillText(t2,t2x,t2y);
}
