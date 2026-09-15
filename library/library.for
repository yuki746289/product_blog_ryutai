c--------------------------------------------------------------
c
c      fortranによる数値計算ライブラリ
c
c      作成日:2011年6月1日
c      作成者:orange
c      HP    :有限要素法・流体力学による数値計算
c      URL   :http://ryutai.ninja-web.net/
c
c      内容
c
c        内積の計算
c        内積による角度計算
c        外積の計算
c        3元1次連立方程式の解
c        3角形の外心
c        4面体の外心
c        3角形の面積
c        4面体の体積
c        ガウスの消去法
c
c      ご使用について
c        ご自由にお使い下さい。商用・非商用問いません。
c        ご使用は自己責任でお願いします。
c
c      使用条件
c        このコメント部分を削除しないこと。
c
c--------------------------------------------------------------


c--------------------------------------------------------------
c
c      内積の計算
c
c      引数
c      v1x:ベクトルv1のx成分
c      v1y:ベクトルv1のy成分
c      v1z:ベクトルv1のz成分
c      v2x:ベクトルv1のx成分
c      v2y:ベクトルv1のy成分
c      v2z:ベクトルv1のz成分
c
c      戻り値
c      naiseki:内積の値
c
c--------------------------------------------------------------
       function naiseki(v1x, v1y, v1z, v2x, v2y, v2z)
       implicit double precision(a-h,o-z)
c
       naiseki=v1x*v2x+v1y*v2y+v1z*v2z
c
       return
       end
c--------------------------------------------------------------
c
c      内積による角度計算
c
c      引数
c      v1x:ベクトルv1のx成分
c      v1y:ベクトルv1のy成分
c      v1z:ベクトルv1のz成分
c      v2x:ベクトルv1のx成分
c      v2y:ベクトルv1のy成分
c      v2z:ベクトルv1のz成分
c
c      戻り値
c      kakudo:角度(°)
c
c--------------------------------------------------------------
       function kakudo(v1x, v1y, v1z, v2x, v2y, v2z)
       implicit double precision(a-h,o-z)
       data PI/3.1415926535d0/
c
       naiseki=v1x*v2x+v1y*v2y+v1z*v2z
       v1=dsqrt(v1x**2+v1y**2+v1z**2)
       v2=dsqrt(v2x**2+v2y**2+v2z**2)
c
       if(naiseki.lt.1d-7)then
         kakudo=dcos(0d0)		!誤差考慮
       else
         kakudo=dacos(naiseki/v1/v2)
         kakudo=kakudo/PI*180d0
       endif
c
       return
       end
c--------------------------------------------------------------
c
c      外積の計算
c
c      引数
c      v1x:ベクトルv1のx成分
c      v1y:ベクトルv1のy成分
c      v1z:ベクトルv1のz成分
c      v2x:ベクトルv2のx成分
c      v2y:ベクトルv2のy成分
c      v2z:ベクトルv2のz成分
c
c      dnx:外積ベクトルのx成分
c      dny:外積ベクトルのy成分
c      dnz:外積ベクトルのz成分
c
c--------------------------------------------------------------
       subroutine gaiseki(v1x,v1y,v1z,v2x,v2y,v2z,dnx,dny,dnz)
       implicit double precision(a-h,o-z)
c
       dnx=v1y*v2z-v1z*v2y
       dny=v1z*v2x-v1x*v2z
       dnz=v1x*v2y-v1y*v2x
       dn=dsqrt(dnx**2+dny**2+dnz**2)
c
       if(dn.lt.1d-5)write(*,*)"in gaiseki 外積:",dn
       if(dn.lt.1d-5)stop
c
       dnx=dnx/dn
       dny=dny/dn
       dnz=dnz/dn
c
c       検算
c       dd1=v1x*dnx+v1y*dny+v1z*dnz
c       dd2=v2x*dnx+v2y*dny+v2z*dnz
c       write(*,*)"dd1,dd2",dd1,dd2
c
        return
        end
c--------------------------------------------------------------
c
c      3元1次連立方程式の解
c      a1x+b1y+c1z=d1
c      a2x+b2y+c2z=d2
c      a3x+b3y+c3z=d3
c
c      引数
c      a1:式1の変数xの係数
c      b1:式1の変数yの係数
c      c1:式1の変数zの係数
c      d1:式1の右辺

c      a2:式2の変数xの係数
c      b2:式2の変数yの係数
c      c2:式2の変数zの係数
c      d2:式2の右辺

c      a3:式3の変数xの係数
c      b3:式3の変数yの係数
c      c3:式3の変数zの係数
c      d3:式3の右辺
c
c      x:変数xの解
c      y:変数yの解
c      z:変数zの解
c
c--------------------------------------------------------------
       subroutine eq3(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3,x,y,z)
       implicit double precision(a-h,o-z)
c
       xyz=a1*b2*c3+a2*b3*c1+a3*b1*c2
     &    -a3*b2*c1-a2*b1*c3-a1*b3*c2
c
       if(xyz.eq.0d0)then
         write(*,*)"解は存在しません"
         stop
       endif
c
       x=(b1*c2*d3+b2*c3*d1+b3*c1*d2-b3*c2*d1-b2*c1*d3-b1*c3*d2)/xyz
       y=(a1*d2*c3+a2*d3*c1+a3*d1*c2-a3*d2*c1-a2*d1*c3-a1*d3*c2)/xyz
       z=(a1*b2*d3+a2*b3*d1+a3*b1*d2-a3*b2*d1-a2*b1*d3-a1*b3*d2)/xyz
c
       return
       end
c--------------------------------------------------------------
c
c      3角形の外心と外接円の半径
c
c      引数
c      x1:頂点1のx座標
c      x2:頂点2のx座標
c      x3:頂点3のx座標
c
c      y1:頂点1のy座標
c      y2:頂点2のy座標
c      y3:頂点3のy座標
c
c      rr:外接円の半径
c      x:外心のx座標
c      y:外心のy座標
c
c--------------------------------------------------------------
       subroutine gaishin_tri(x1,x2,x3,y1,y2,y3,rr,x,y)
       implicit double precision(a-h,o-z)
c
c      辺の長さ
       a=dsqrt((x2-x3)**2+(y2-y3)**2)
       b=dsqrt((x3-x1)**2+(y3-y1)**2)
       c=dsqrt((x1-x2)**2+(y1-y2)**2)
c
c      面積
       ar=artri(x1,y1,0d0,x2,y2,0d0,x3,y3,0d0)
       if(ar.lt.1d-7)then
         rr=0d0
         return
       endif
c
c      外接円の中心
       x=a**2*(b**2+c**2-a**2)*x1
     &  +b**2*(c**2+a**2-b**2)*x2
     &  +c**2*(a**2+b**2-c**2)*x3
       x=x/16d0/ar**2
       y=a**2*(b**2+c**2-a**2)*y1
     &  +b**2*(c**2+a**2-b**2)*y2
     &  +c**2*(a**2+b**2-c**2)*y3
       y=y/16d0/ar**2
c
c      外接円の半径
       r1=dsqrt((x1-x)**2+(y1-y)**2)
       r2=dsqrt((x2-x)**2+(y2-y)**2)
       r3=dsqrt((x3-x)**2+(y3-y)**2)
       rr=(r1+r2+r3)/3d0
c
c      検算
       if(dabs(r1-rr).gt.1d-5 .or.
     &    dabs(r2-rr).gt.1d-5 .or. 
     &    dabs(r3-rr).gt.1d-5)then
          write(*,*)"circum"
          write(*,*)"radian is different"
          write(*,*)"r:",sngl(r1),sngl(r2),sngl(r3),sngl(rr)
          stop
        endif
c
       return
       end
c--------------------------------------------------------------
c
c      4面体の外心
c
c      引数
c      x1:頂点1のx座標
c      x2:頂点2のx座標
c      x3:頂点3のx座標
c      x4:頂点4のx座標
c
c      y1:頂点1のy座標
c      y2:頂点2のy座標
c      y3:頂点3のy座標
c      y4:頂点4のy座標
c
c      z1:頂点1のz座標
c      z2:頂点2のz座標
c      z3:頂点3のz座標
c      z4:頂点4のz座標
c
c      xc:外心のx座標
c      yc:外心のy座標
c      zc:外心のz座標
c      rr:外接球の半径
c
c--------------------------------------------------------------
        subroutine gaishin_tet(x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4
     &                                                   ,xc,yc,zc,rr)
        implicit double precision(a-h,o-z)
c
        a1=2d0*(x1-x2)
        a2=2d0*(x1-x3)
        a3=2d0*(x1-x4)
        b1=2d0*(y1-y2)
        b2=2d0*(y1-y3)
        b3=2d0*(y1-y4)
        c1=2d0*(z1-z2)
        c2=2d0*(z1-z3)
        c3=2d0*(z1-z4)
        d1=x1**2-x2**2+y1**2-y2**2+z1**2-z2**2
        d2=x1**2-x3**2+y1**2-y3**2+z1**2-z3**2
        d3=x1**2-x4**2+y1**2-y4**2+z1**2-z4**2
c       外心の座標
        xyz=a1*b2*c3+a2*b3*c1+a3*b1*c2-a3*b2*c1-a2*b1*c3-a1*b3*c2
        xc=(b1*c2*d3+b2*c3*d1+b3*c1*d2-b3*c2*d1-b2*c1*d3-b1*c3*d2)/xyz
        yc=(a1*d2*c3+a2*d3*c1+a3*d1*c2-a3*d2*c1-a2*d1*c3-a1*d3*c2)/xyz
        zc=(a1*b2*d3+a2*b3*d1+a3*b1*d2-a3*b2*d1-a2*b1*d3-a1*b3*d2)/xyz
c       外接球の半径
        r1=dsqrt((x1-xc)**2+(y1-yc)**2+(z1-zc)**2)
        r2=dsqrt((x2-xc)**2+(y2-yc)**2+(z2-zc)**2)
        r3=dsqrt((x3-xc)**2+(y3-yc)**2+(z3-zc)**2)
        r4=dsqrt((x4-xc)**2+(y4-yc)**2+(z4-zc)**2)
c       検算
        ifg=0
        if(dabs(r1-r2).gt.1d-7)ifg=1
        if(dabs(r2-r3).gt.1d-7)ifg=1
        if(dabs(r3-r4).gt.1d-7)ifg=1
        if(dabs(r4-r1).gt.1d-7)ifg=1
        if(ifg.eq.1)write(*,*)"in circumct3 ifg:",ifg
        if(ifg.eq.1)then
          write(*,*)"x1:",sngl(x1),sngl(y1),sngl(z1)
          write(*,*)"x2:",sngl(x2),sngl(y2),sngl(z2)
          write(*,*)"x3:",sngl(x3),sngl(y3),sngl(z3)
          write(*,*)"x4:",sngl(x4),sngl(y4),sngl(z4)
          write(*,*)"r1:",r1
          write(*,*)"r2:",r2
          write(*,*)"r3:",r3
          write(*,*)"r4:",r4
          write(*,*)"xc:",sngl(xc),sngl(yc),sngl(zc)
        endif
        if(ifg.eq.1)stop
        rr=(r1+r2+r3+r4)/4d0
c
        return
        end
c--------------------------------------------------------------
c
c      3角形の面積
c
c      引数
c      x1:頂点1のx座標
c      x2:頂点2のx座標
c      x3:頂点3のx座標
c
c      y1:頂点1のy座標
c      y2:頂点2のy座標
c      y3:頂点3のy座標
c
c      戻り値
c      atri:3角形の面積
c
c--------------------------------------------------------------
       function artri(x1,y1,z1,x2,y2,z2,x3,y3,z3)
       implicit double precision(a-h,o-z)
c
       vx=(y1-y3)*(z2-z3)-(z1-z3)*(y2-y3)
       vy=(z1-z3)*(x2-x3)-(x1-x3)*(z2-z3)
       vz=(x1-x3)*(y2-y3)-(y1-y3)*(x2-x3)
       artri=dsqrt(vx**2+vy**2+vz**2)/2d0
c
       return
       end
c--------------------------------------------------------------
c
c      4面体の体積
c
c      引数
c      x1:頂点1のx座標
c      x2:頂点2のx座標
c      x3:頂点3のx座標
c      x4:頂点4のx座標
c
c      y1:頂点1のy座標
c      y2:頂点2のy座標
c      y3:頂点3のy座標
c      y4:頂点4のy座標
c
c      z1:頂点1のz座標
c      z2:頂点2のz座標
c      z3:頂点3のz座標
c      z4:頂点4のz座標
c
c      戻り値
c      vltet:4面体の体積
c
c--------------------------------------------------------------
        function vltet(x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4)
        implicit double precision(a-h,o-z)
c
        a11=1d0
        a21=1d0
        a31=1d0
        a41=1d0
        a12=x1
        a22=x2
        a32=x3
        a42=x4
        a13=y1
        a23=y2
        a33=y3
        a43=y4
        a14=z1
        a24=z2
        a34=z3
        a44=z4
c
        det=a11*a22*a33*a44-a11*a22*a34*a43-a11*a23*a32*a44
     &      +a11*a23*a34*a42
     &      +a11*a24*a32*a43-a11*a24*a33*a42-a12*a21*a33*a44
     &      +a12*a21*a34*a43
     &      +a12*a23*a31*a44-a12*a23*a34*a41-a12*a24*a31*a43
     &      +a12*a24*a33*a41
     &      +a13*a21*a32*a44-a13*a21*a34*a42-a13*a22*a31*a44
     &      +a13*a22*a34*a41
     &      +a13*a24*a31*a42-a13*a24*a32*a41-a14*a21*a32*a43
     &      +a14*a21*a33*a42
     &      +a14*a22*a31*a43-a14*a22*a33*a41-a14*a23*a31*a42
     &      +a14*a23*a32*a41
        vltet=dabs(det)/6d0
c        vltet=det/6d0
c
        return
        end
c--------------------------------------------------------------
c
c      ガウスの消去法
c
c      引数
c      a:左辺の係数マトリックス
c      b:右辺の値のマトリックス
c      x:変数の解のマトリックス
c      m:項数の最大値
c
c--------------------------------------------------------------
       subroutine gauss(a,b,x,m)
       implicit double precision(a-h,o-z)
       dimension a(m,m),b(m)
c
c      前進消去
       do i=2,nn
         do j=i,nn
           dd=a(j,i-1)/a(i-1,i-1)
           a(j,i-1)=0
           b(j)=b(j)-dd*b(i-1)
           do k=i,nn
             a(j,k)=a(j,k)-dd*a(i-1,k)
           enddo
         enddo
       enddo
c
c      後退代入
       do i=nn,1,-1
         xx=0
         do j=i+1,nn
             xx=xx+x(j)*a(i,j)
         enddo
         x(i)=(b(i)-xx)/a(i,i)
       enddo
c
       return
       end



