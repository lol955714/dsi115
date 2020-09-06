var abcwin = new ABCwin();
var abcshow = new ABCshow();


function nuevoAjax(){ 
	var xmlhttp=false; 
	try { 
		xmlhttp=new ActiveXObject("Msxml2.XMLHTTP"); 
	}
	catch(e){ 
		try	{ 
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); 
		} 
		catch(E) { 
			xmlhttp=false; 
		}
	}
	if (!xmlhttp && typeof XMLHttpRequest!="undefined") {
		xmlhttp=new XMLHttpRequest(); 
	} 
	return xmlhttp; 
}

function ABCwin(){
	this.ajax = nuevoAjax();
	this.ajax_method = "POST";
	this.statusclose = false;
	this.statusshow = true;
	this.abc_container = document.createElement('div');
	this.abc_container.setAttribute('id','box_msg');
	this.abc_black = document.createElement('div');
	this.abc_content = document.createElement('div');
	this.abc_content.setAttribute('id','box_content');
	this.abc_center = document.createElement('div');
	this.abc_center.setAttribute('id','box_content_center');
	this.abc_close = document.createElement('a');
	this.abc_close.setAttribute('id','box_close');
	this.abc_close.setAttribute('href','javascript:;');
	this.abc_content.appendChild(this.abc_center);
	this.abc_container.appendChild(this.abc_black);
	this.abc_container.appendChild(this.abc_content);
	this.abc_bodynode;
	this.abc_htmlnode;
	this.abc_blockone;
	this.abc_blockimg;
	this.abc_blocktwo;
	this.abc_p;
	this.status_scroll = false;
	this.statusfade = true;
	this.statusalert = true;
	
	this.abc_container.style.width = "100%";
	this.abc_container.style.height = "100%";
	this.abc_container.style.position = "absolute";
	this.abc_container.style.zIndex = "99";
	this.abc_container.style.display = "none";
	this.abc_container.style.verticalAlign = "middle";
	this.abc_container.style.left = this.abc_black.style.left = this.abc_content.style.left = 0;
	this.abc_container.style.top = this.abc_black.style.left = this.abc_content.style.top = 0;
	
	this.abc_black.style.width = "100%";
	this.abc_black.style.height = "100%";
	this.abc_black.style.background = "black";
	this.abc_black.style.position = "absolute";
	this.abc_black.style.zIndex = "100";
	this.abc_content.style.width = "100%";
	this.abc_content.style.height = "100%";
	this.abc_content.style.textAlign = "center";
	this.abc_content.style.position = "absolute";
	this.abc_content.style.verticalAlign = "middle";
	this.abc_content.style.zIndex = "101";
	this.abc_center.style.width = "100%";
	this.abc_center.style.textAlign = "left";
	this.abc_center.style.position = "relative";
	this.abc_close.style.position = "absolute";
	this.abc_close.style.display = "block";
	this.abc_close.style.width = "40px";
	this.abc_close.style.height = "40px";
	this.abc_close.style.marginTop = "-30px";
	this.abc_close.style.backgroundPosition = "center center";
	this.abc_close.style.backgroundRepeat = "no-repeat";
	this.abc_close.style.backgroundImage = "url(img/close.png)";
	
	this.abc_center.style.verticalAlign = "middle";
	if(document.all && !window.addEventListener){
		this.abc_content.style.display = "block";
		this.abc_center.style.display = "block";
		this.abc_center.style.position = "absolute";
		this.abc_center.style.top = "50%";
		this.abc_center.style.left = "0";
	}else{
		this.abc_content.style.display = "table";
		this.abc_center.style.display = "table-cell";
	}
	
	this.onFinishFade = function(e){};
	this.onFinishAjax = function(e){
		abcshow.loadBody();
		loadBody();
	}
	this.confirmResult = function(e){};
	this.ready = function(){};
	
	var object = this;
	function loadBody(){
		object.setElements();
		object.ready();
	}
	
	try{
		window.attachEvent("onload",loadBody);
	}
	catch(e){ 
		try {
			window.addEventListener("DOMContentLoaded",loadBody, false);
		}
		catch(e){
			window.onload = loadBody;
		}
	}
	
	this.setElements = function(){
		this.abc_htmlnode = document.getElementsByTagName("html")[0];
		this.abc_bodynode = document.getElementsByTagName("body")[0];
		this.abc_bodynode.style.margin = 0;
		if(document.all){
			if(!window.addEventListener){
				this.abc_bodynode.style.height = this.abc_htmlnode.style.height = "100%";
			}
		}
		this.abc_bodynode.insertBefore(this.abc_container,this.abc_bodynode.firstChild);
		var root = this;
		
		try {
			var links = document.getElementsByTagName("body")[0].getElementsByTagName("a");
			for(var i=0;i<links.length;i++){
				if(links[i].rev.substr(0,6) == "abcwin"){
					links[i].onclick = function(){
						var point = this.rel.indexOf(":");
						root.ajax_method = this.rel.substring(0,point);
						var data = this.rel.substring(point + 1);
						var w = 400;
						var h = "auto";
						if(this.rev.indexOf("[")){
							var w_ini = Number(this.rev.indexOf("[")) + 1;
							var w_end = Number(this.rev.indexOf(","));
							var h_ini = Number(this.rev.indexOf(",")) + 1;
							var h_end = Number(this.rev.indexOf("]"));
							w = this.rev.substring(w_ini,w_end);
							h = this.rev.substring(h_ini,h_end);
						}
						root.ABCalert(data,this.href,w,h);
						return false;
					}
				}
				
			}
		}catch(e){}
		
		this.abc_close.onmouseup = function(){
			if(root.statusalert){
				root.ABChide();
			}
			return false;
		}
		
		this.abc_center.onmouseup = function(){
			if(root.statusalert){
				root.ABChide();
			}
		}
		
	}
	
	this.keyFunction = function(){
		var root = this;
		document.getElementsByTagName("body")[0].onkeydown = function(e){
			var keycode;
			if(window.event){
				keycode = window.event.keyCode;
			}else{
				keycode = e.which;
			}
			if(keycode == 0 || keycode == 27){
				root.ABChide();
			}
			return true;
		}
		return false;
	}
	
	
	this.getSize = function(element){
		var w = element.scrollWidth;
		var h = element.scrollHeight;
		return { _w: w, _h: h }
	}
	
	
	this.getMeasures = function(){
		var myWidth;
		var myHeight;
		if(typeof( window.innerWidth ) == 'number') { 
			//Non-IE 
			myWidth = window.innerWidth;
			myHeight = window.innerHeight; 
		}else if( document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)){ 
			myWidth = document.documentElement.clientWidth; 
			myHeight = document.documentElement.clientHeight; 
		}else if( document.body && (document.body.clientWidth || document.body.clientHeight)){ 
			//IE 4 compatible 
			myWidth = document.body.clientWidth; 
			myHeight = document.body.clientHeight; 
		}
		return { _w: myWidth, _h: myHeight }
	}
	
	
	this.setContent = function(w,h){
		var root = this;
		var element_h;
		if(this.getSize(this.abc_htmlnode)._h == 0){
			element_h = this.getSize(this.abc_bodynode)._h;
		}else{
			element_h = this.getSize(this.abc_htmlnode)._h;
		}
		if(this.getMeasures()._h <= element_h){
			this.abc_black.style.height = element_h + "px";
		}else{
			this.abc_black.style.height = "100%";
		}
		if(document.all){
			this.abc_black.style.top = window.document.documentElement.scrollTop * -1 + "px";
		}else{
			this.abc_black.style.top = window.pageYOffset * -1 + "px";
		}
		window.onresize = function(){
			if(root.getMeasures()._h <= element_h){
				root.abc_black.style.height = element_h + "px";
			}else{
				root.abc_black.style.height = "100%";
			}
			if(document.all){
				root.abc_black.style.top = window.document.documentElement.scrollTop * -1 + "px";
			}else{
				root.abc_black.style.top = window.pageYOffset * -1 + "px";
			}
			abcshow.ABChide();
			root.ABChide();
		}
		var root = this;
		this.abc_blockone = document.createElement('div');
		this.abc_blocktwo = document.createElement('div');
		this.abc_blocktwo.setAttribute('id','abc_win');
		this.abc_blocktwo.onmouseup = function(){
			root.statusalert = false;
		}
		this.abc_blocktwo.onclick = function(){
			root.statusalert = true;
		}
		this.abc_blocktwo.style.textAlign = "left";
		this.abc_blocktwo.style.backgroundImage = "url(img/loader_content.gif)";
		this.abc_blocktwo.style.backgroundPosition = "center center";
		this.abc_blocktwo.style.backgroundRepeat = "no-repeat";
		this.abc_blocktwo.style.margin = "0 auto";
		
		this.abc_blockone.style.width = "100%";
		this.abc_blocktwo.style.width = w + "px";
		this.abc_blocktwo.style.height = "40px";
		
		if(document.all && !window.addEventListener){
			this.abc_center.style.top = "50%";
			if(h == "inherit" || h == "auto"){
				this.abc_center.style.marginTop = "-200px";
			}else{
				this.abc_center.style.marginTop = h / -2 + "px";
			}
		}
		
		this.abc_blockone.appendChild(this.abc_blocktwo);
		this.abc_center.appendChild(this.abc_blockone);
		this.statusclose = true;
		
		this.keyFunction();	
	}

	
	this.ABCalert = function(rel,url,w,h){
		this.ABChide();
		var root = this;
		this.showBlack();
		this.setContent(w,h);
		this.ajax.open(this.ajax_method, url, true);
		this.ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		this.ajax.onreadystatechange = function(){
			if(root.ajax.readyState == 4){
				var datos = root.ajax.responseText;

				root.abc_blocktwo.innerHTML = datos;
				if(h == "inherit" || h == "auto"){
					root.abc_blocktwo.style.height = "auto";
				}else{
					root.abc_blocktwo.style.height = h + "px";
				}
				var box = root.abc_blocktwo.getElementsByTagName("div")[0];
				if(box){
					root.fadeElement(box,0,100,true);
				}
				
				root.abc_blocktwo.insertBefore(root.abc_close,root.abc_blocktwo.firstChild);
				root.abc_close.style.marginLeft = w - 10 + "px";
				root.abc_blocktwo.style.backgroundPosition = "10000px center";
				
				return root.onFinishAjax(rel);
			}
		}
		this.ajax.send(rel);
		
	}
	
	this.showBlack = function(){
		this.statusfade = false;
		if(document.all){
			this.abc_container.style.marginTop = window.document.documentElement.scrollTop + "px";
		}else{
			this.abc_container.style.marginTop = window.pageYOffset + "px";
		}
		this.abc_black.style.marginTop = "0";
		this.fadeElement(this.abc_black,0,50,true);
		this.abc_container.style.display = "block";
		
		this.statusshow = false;
	}


	this.ABChide = function(){
		var root = this;
		this.scrolling_status = false;
		this.statusfade = true;
		if(this.statusclose){
			if(this.abc_blockimg){
				root.leftstatus = false;
				root.rightstatus = false;
				this.abc_blockimg.removeChild(this.img);
			}
			this.abc_center.removeChild(this.abc_blockone);
			this.fadeElement(this.abc_black,50,0,false);
			this.statusshow = true;
			this.statusclose = false;
			this.onFinishFade = function(e){
				if(!e){
					if(root.statusfade == true){
						root.abc_container.style.display = "none";
					}else{
						root.abc_container.style.display = "block";
					}
				}
			}
		}
	}
	
	this.fadeElement = function(element,start,total,type){
		var root = this;
		var start_one = start / 100;
		var total_one = total / 100;
		var fadenumber = start;
		var fadeopacity;
		element.style.opacity = start_one;
		element.style.filter = 'alpha(opacity='+ start +')';
		element.style.MozOpacity = start_one;
		var showcontainer = setInterval(fade,50);
		
		function fade(){
			if(type){
				fadenumber+= 20;
			}else{
				fadenumber-= 20;
			}
			fadeopacity = fadenumber / 100;
			if(type){
				if(fadenumber >= total){
					clearInterval(showcontainer);
					element.style.opacity = total_one;
					element.style.filter = 'alpha(opacity='+ total +')';
					element.style.MozOpacity = total_one;
					root.statusalert = true;
					return root.onFinishFade(type);
				}else{
					element.style.opacity = fadeopacity;
					element.style.filter = 'alpha(opacity='+ fadenumber +')';
					element.style.MozOpacity = fadeopacity;
					return false;
				}
			}else{
				if(fadenumber <= total){
					clearInterval(showcontainer);
					element.style.opacity = total_one;
					element.style.filter = 'alpha(opacity='+ total +')';
					element.style.MozOpacity = total_one;
					root.statusalert = true;
					return root.onFinishFade(type);
				}else{
					element.style.opacity = fadeopacity;
					element.style.filter = 'alpha(opacity='+ fadenumber +')';
					element.style.MozOpacity = fadeopacity;
					return false;
				}
			}
		}
	}		
	
}

/* --------------------------------- ABC show --------------------------------------- */

function ABCshow(){
	
	this.statusclose = false;
	this.statusshow = true;
	this.abc_container = document.createElement('div');
	this.abc_black = document.createElement('div');
	this.abc_black.setAttribute('id','box_black');
	this.abc_content = document.createElement('div');
	this.abc_content.setAttribute('id','box_content');
	this.abc_center = document.createElement('div');
	this.abc_center.setAttribute('id','box_content_center');
	this.abc_content.appendChild(this.abc_center);
	this.abc_container.appendChild(this.abc_black);
	this.abc_container.appendChild(this.abc_content);
	this.abc_htmlnode
	this.abc_bodynode;
	this.abc_blockone;
	this.abc_blockimg;
	this.img;
	this.iframevideo;
	this.contenttype;
	
	this.prel;
	this.ptitle;
	this.pnums;
	this.totalgroup;
	this.totalgroupvideos;
	this.arrow_left;
	this.arrow_right;
	this.btclose;
	this.leftstatus;
	this.rightstatus;
	this.statuspicture = true;
	this.statusfade = true;
	this.statusload = true;
	this.iniw = 30;
	this.inih = 30;
	this.coefficient = 0.3;
	this.margin_title = 20;
	
	this.abc_container.style.width = "100%";
	this.abc_container.style.height = "100%";
	this.abc_container.style.position = "absolute";
	this.abc_container.style.display = "none";
	this.abc_container.style.zIndex = "199";
	this.abc_container.style.verticalAlign = "middle";
	this.abc_container.style.left = this.abc_black.style.left = this.abc_content.style.left = 0;
	
	this.abc_black.style.width = "100%";
	this.abc_black.style.height = "100%";
	this.abc_black.style.background = "black";
	
	this.abc_black.style.position = "absolute";
	this.abc_black.style.zIndex = "200";
	this.abc_content.style.width = "100%";
	this.abc_content.style.height = "100%";
	this.abc_content.style.textAlign = "center";
	this.abc_content.style.position = "absolute";
	this.abc_content.style.verticalAlign = "middle";
	this.abc_content.style.zIndex = "201";
	this.abc_center.style.width = "100%";
	this.abc_center.style.textAlign = "center";
	this.abc_center.style.position = "relative";
	
	this.group_images = new Array();
	this.group_videos = new Array();
	
	this.current_group = new Array();
	this.current_group_videos = new Array();
	
	this.current_index;
	this.current_groupname;
	
	this.current_index_video;
	this.current_groupname_video;
	
	this.abc_center.style.verticalAlign = "middle";
	if(document.all){
		this.abc_content.style.display = "block";
		this.abc_center.style.display = "block";
		this.abc_center.style.position = "absolute";
		this.abc_center.style.top = "50%";
		this.abc_center.style.left = "0";
	}else{
		this.abc_content.style.display = "table";
		this.abc_center.style.display = "table-cell";
	}
	//----------------------------------------------
	
	this.onFinishFade = function(e){};
	this.confirmResult = function(e){};
	
	var object = this;
	this.loadBody = function(){
		object.setElements();
	}
	
	try{
		window.attachEvent("onload",this.loadBody);
	}
	catch(e){ 
		try {
			document.addEventListener("DOMContentLoaded", this.loadBody, false);
		}
		catch(e){
			window.onload = this.loadBody;
		}
	}
	
	this.setElements = function(){
		this.abc_htmlnode = document.getElementsByTagName("html")[0];
		this.abc_bodynode = document.getElementsByTagName("body")[0];
		this.abc_bodynode.style.margin = 0;
		if(document.all){
			if(!window.addEventListener){
				this.abc_bodynode.style.height = this.abc_htmlnode.style.height = "100%";
			}
		}
		this.abc_bodynode.insertBefore(this.abc_container,this.abc_bodynode.firstChild);
		this.abc_container.style.background = "url(img/left.png) 10000px 10000px no-repeat";
		this.abc_black.style.background = "black url(img/loader.gif) 10000px 10000px no-repeat";
		this.abc_content.style.background = "url(img/arrows.png) 10000px 10000px no-repeat";
		this.abc_center.style.background = "url(img/right.png) 10000px 10000px no-repeat";
		
		this.group_images = new Array();
		this.group_videos = new Array();
		
		var root = this;
		this.abc_center.onclick = function(){
			if(root.statuspicture){
				root.ABChide();
			}
		}
		
		for(var i=0; i< document.links.length; i++){
			var node = document.links[i];
			if(node.rel.substr(0,7) == "abcshow" || node.rel == "null"){
				var ini = node.rel.indexOf("[") + 1;
				var end = node.rel.indexOf("]");
				var image = new Image();
				image.url = document.links[i].href;
				image.rel = document.links[i].title;
				image.group = node.rel.substring(ini,end);
				image.num = i;
				if(node.getElementsByTagName("img")[0]){
					image.src = node.getElementsByTagName("img")[0].src;
					image.img = node.getElementsByTagName("img")[0];
					node.getElementsByTagName("img")[0].group = image.group;
				}
				this.group_images.push(image);
				
				if(node.className == "abc" && node.getElementsByTagName("img")[0]){
					if(document.all){
						if(image.img.complete){
							if(image.img.style.visibility != "visible"){
								image.img.style.filter = "alpha(opacity=0)";
								image.img.style.opacity = "0";
								image.img.style.MozOpacity = "0";
								root.fadeElement(image.img,0,100,true);
							}
						}
						image.img.style.visibility = "visible";
					}
					
					image.onload = function(){
						if(!document.all){
							if(this.img.style.visibility != "visible"){
								this.img.style.filter = "alpha(opacity=0)";
								this.img.style.opacity = "0";
								this.img.style.MozOpacity = "0";
								root.fadeElement(this.img,0,100,true);
							}
							this.img.style.visibility = "visible";
						}
					}
				}
				if(node.rel != "null"){
					node.onclick = function(){
						root.contenttype = "image";
						var current = "";
						if(this.getElementsByTagName("img")[0]){
							current = this.getElementsByTagName("img")[0].group;
						}else{
							var ini = this.rel.indexOf("[") + 1;
							var end = this.rel.indexOf("]");
							current = this.rel.substring(ini,end);
						}
						root.current_groupname = current;
						root.current_group = new Array();
						var index = 0;
						for(var i=0; i<root.group_images.length; i++){
							if(root.group_images[i].group == current && current != ""){
								root.current_group.push(root.group_images[i]);
								root.group_images[i].index = index;
								if(this.getElementsByTagName("img")[0]){
									if(root.group_images[i].src == this.getElementsByTagName("img")[0].src){
										root.current_index = index;
										this.index = index;
									}
								}else{
									if(root.group_images[i].url == this.href){
										root.current_index = index;
										this.index = index;
									}
								}
								index++;
							}
						}
						root.totalgroup = index;
						var h = this.href;
						if(root.current_group.length > 1){
							root.setBoxes(h,this.title,root.current_index + 1,this.index + 1,root.totalgroup);
						}else{
							root.setBoxes(h,this.title,false,0,0);
						}
						
						return false;
					}
				}
			}else if(node.rel.substr(0,8) == "abcvideo" || node.rel == "null"){

				var char1 = node.rel.indexOf("[") + 1;
				var char2 = node.rel.indexOf("|");
				var char3;
				var char4;
				var w;
				var h;
				var videogroup;
				if(node.rel.indexOf(",") != -1){
					char3 = node.rel.indexOf(",") + 1;
					char4 = node.rel.indexOf("]");
					w = node.rel.substring(char1,char2);
					h = node.rel.substring(char2 + 1,char3 - 1);
				    videogroup = node.rel.substring(char3,char4);
				}else{
					char3 = node.rel.indexOf("]");
					w = node.rel.substring(char1,char2);
					h = node.rel.substring(char2 + 1,char3);
					videogroup = "";
				}
				
				var imagevideo = new Image();
				imagevideo.url = document.links[i].href;
				imagevideo.rel = document.links[i].title;
				imagevideo.w = w;
				imagevideo.h = h;
				imagevideo.group = videogroup;
				if(node.getElementsByTagName("img")[0]){
					imagevideo.src = node.getElementsByTagName("img")[0].src;
					imagevideo.img = node.getElementsByTagName("img")[0];
					node.getElementsByTagName("img")[0].group = imagevideo.group;
				}
				this.group_videos.push(imagevideo);
				
				if(node.className == "abc" && node.getElementsByTagName("img")[0]){
					if(document.all){
						if(imagevideo.img.complete){
							if(imagevideo.img.style.visibility != "visible"){
								imagevideo.img.style.filter = "alpha(opacity=0)";
								imagevideo.img.style.opacity = "0";
								imagevideo.img.style.MozOpacity = "0";
								root.fadeElement(imagevideo.img,0,100,true);
							}
						}
						imagevideo.img.style.visibility = "visible";
					}
					
					imagevideo.onload = function(){
						if(!document.all){
							if(this.img.style.visibility != "visible"){
								this.img.style.filter = "alpha(opacity=0)";
								this.img.style.opacity = "0";
								this.img.style.MozOpacity = "0";
								root.fadeElement(this.img,0,100,true);
							}
							this.img.style.visibility = "visible";
						}
					}
				}
				if(node.rel != "null"){
					node.onclick = function(){
						root.contenttype = "video";
						var current = "";
						if(this.getElementsByTagName("img")[0]){
							current = this.getElementsByTagName("img")[0].group;
						}else{
							var char1 = this.rel.indexOf("[") + 1;
							var char2 = this.rel.indexOf("|");
							var char3;
							var char4;
							var videogroup;
							if(this.rel.indexOf(",") != -1){
								char3 = this.rel.indexOf(",") + 1;
								char4 = this.rel.indexOf("]");
								videogroup = this.rel.substring(char3,char4);
							}else{
								char3 = this.rel.indexOf("]");
								videogroup = "";
							}
							current = videogroup;
						}
						root.current_groupname_video = current;
						root.current_group_videos = new Array();
						var index = 0;
						for(var i=0; i<root.group_videos.length; i++){
							if(root.group_videos[i].group == current && current != ""){
								root.current_group_videos.push(root.group_videos[i]);
								root.group_videos[i].index = index;
								if(this.getElementsByTagName("img")[0]){
									if(root.group_videos[i].src == this.getElementsByTagName("img")[0].src){
										root.current_index_video = index;
										this.index = index;
									}
								}else{
									if(root.group_videos[i].url == this.href){
										root.current_index_video = index;
										this.index = index;
									}
								}
								index++;
							}else{
								if(this.getElementsByTagName("img")[0]){
									if(root.group_videos[i].src == this.getElementsByTagName("img")[0].src){
										this.index = i;
									}
								}else{
									if(root.group_videos[i].url == this.href){
										this.index = i;
									}
								}
							}
						}
						root.totalgroupvideos = index;
						var h = this.href;
						if(root.current_group_videos.length > 1){
							root.setBoxes(h,this.title,root.current_index_video + 1,this.index + 1,root.totalgroupvideos);
						}else{
							root.setBoxes(h,this.title,false,this.index,0);
						}
						
						return false;
					}
				}
			}
		}
	}
	
	
	this.keyFunction = function(b1,b2){
		var root = this;
		document.getElementsByTagName("body")[0].onkeydown = function(e){
			var keycode;
			if(window.event){
				keycode = window.event.keyCode;
			}else{
				keycode = e.which;
			}
			if(keycode == 0 || keycode == 27){
				root.ABChide();
				return false;
			}else if(keycode == 37 && root.leftstatus){
				root.startPictures(b1,b2,"left");
				return false;
			}else if(keycode == 39 && root.rightstatus){
				root.startPictures(b1,b2,"right");
				return false;
			}else{
				return true;
			}
		}
	}
	
	
	this.showBlack = function(){
		var root = this;
		this.statusfade = false;
		if(document.all){
			this.abc_container.style.width = "100%";
			this.abc_container.style.marginTop = window.document.documentElement.scrollTop + "px";
		}else{
			this.abc_container.style.marginTop = window.pageYOffset + "px";
		}
		this.abc_black.style.marginTop = "0";
		this.fadeElement(this.abc_black,0,50,true);
		this.abc_container.style.display = "block";
		this.statusshow = false;
	}

	this.ABChide = function(){
		var root = this;
		this.statusfade = true;
		if(this.statusclose){
			if(this.abc_blockimg){
				root.leftstatus = false;
				root.rightstatus = false;
				if(this.img){;
					this.abc_blockimg.removeChild(this.img);
					this.img = null;
				}
				if(this.iframevideo){
					this.iframevideo.src = "";
					this.abc_blockimg.removeChild(this.iframevideo);
					this.iframevideo = null;
				}
			}
			this.abc_center.removeChild(this.abc_blockone);
			this.fadeElement(this.abc_black,50,0,false);
			this.statusshow = true;
			this.statusclose = false;
			this.onFinishFade = function(e){
				if(!e){
					if(root.statusfade == true){
						if(document.all){
							root.abc_container.style.width = 0;
						}else{
							root.abc_container.style.display = "none";
						}
					}
				}
			}
		}
		
		abcwin.keyFunction();
		
	}
	
	this.fadeElement = function(element,start,total,type){
		var root = this;
		var start_one = start / 100;
		var total_one = total / 100;
		var fadenumber = start;
		var fadeopacity;
		element.style.opacity = start_one;
		element.style.filter = 'alpha(opacity='+ start +')';
		element.style.MozOpacity = start_one;
		var showcontainer = setInterval(fade,50);
		
		function fade(){
			fadenumber+= (total - fadenumber) * root.coefficient;
			fadeopacity = fadenumber / 100;
			if(type){
				element.style.visibility = "visible";
				if(Math.round(fadenumber) == total){
					clearInterval(showcontainer);
					element.style.opacity = total_one;
					element.style.filter = 'alpha(opacity='+ total +')';
					element.style.MozOpacity = total_one;
					return root.onFinishFade(type);
				}else{
					element.style.opacity = fadeopacity;
					element.style.filter = 'alpha(opacity='+ fadenumber +')';
					element.style.MozOpacity = fadeopacity;
					return false;
				}
			}else{
				if(Math.round(fadenumber) == total){
					element.style.visibility = "hidden";
					clearInterval(showcontainer);
					element.style.opacity = total_one;
					element.style.filter = 'alpha(opacity='+ total +')';
					element.style.MozOpacity = total_one;
					return root.onFinishFade(type);
				}else{
					element.style.opacity = fadeopacity;
					element.style.filter = 'alpha(opacity='+ fadenumber +')';
					element.style.MozOpacity = fadeopacity;
					return false;
				}
			}
		}
	}
	
	
	this.getSize = function(element){
		var w = element.scrollWidth;
		var h = element.scrollHeight;
		return { _w: w, _h: h }
	}
	
	
	this.getMeasures = function(){
		var myWidth;
		var myHeight;
		if(typeof( window.innerWidth ) == 'number') { 
			//Non-IE 
			myWidth = window.innerWidth;
			myHeight = window.innerHeight; 
		}else if( document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)){ 
			//IE 6+ in 'standards compliant mode' 
			myWidth = document.documentElement.clientWidth; 
			myHeight = document.documentElement.clientHeight; 
		}else if( document.body && (document.body.clientWidth || document.body.clientHeight)){ 
			//IE 4 compatible 
			myWidth = document.body.clientWidth; 
			myHeight = document.body.clientHeight; 
		}
		return { _w: myWidth, _h: myHeight }
	}
	
	
	this.setBoxes = function(url,rel,group,current,total){
		var root = this;
		var element_h;
		if(this.getSize(this.abc_htmlnode)._h == 0){
			element_h = this.getSize(this.abc_bodynode)._h;
		}else{
			element_h = this.getSize(this.abc_htmlnode)._h;
		}
		if(this.getMeasures()._h <= element_h){
			this.abc_black.style.height = element_h + "px";
		}else{
			this.abc_black.style.height = "100%";
		}
		if(document.all){
			this.abc_black.style.top = window.document.documentElement.scrollTop * -1 + "px";
		}else{
			this.abc_black.style.top = window.pageYOffset * -1 + "px";
		}
		window.onresize = function(){
			if(root.getMeasures()._h <= element_h){
				root.abc_black.style.height = element_h + "px";
			}else{
				root.abc_black.style.height = "100%";
			}
			if(document.all){
				root.abc_black.style.top = window.document.documentElement.scrollTop * -1 + "px";
			}else{
				root.abc_black.style.top = window.pageYOffset * -1 + "px";
			}
			root.ABChide();
			abcwin.ABChide();
		}
		if(this.statusshow){
			this.iniw = 30;
			this.inih = 30;
			var root = this;
			this.showBlack();
			this.abc_blockone = document.createElement('div');
			this.abc_blockone.setAttribute('id','abc_show');
			this.abc_blockimg = document.createElement('div');
			if(this.contenttype == "image"){
				this.img = new Image();
				this.img.setAttribute('src',url);
			}else if(this.contenttype == "video"){
				this.iframevideo = document.createElement('div');
				var w;
				var h;
				if(group){
					w = root.current_group_videos[current - 1].w;
					h = root.current_group_videos[current - 1].h;
				}else{
					w = root.group_videos[current].w;
					h = root.group_videos[current].h;
				}
				var iframe = "<iframe src='' height='" + h + "' width='" + w + "' style='background: black url(img/loader.gif) center center no-repeat' scrolling='no' frameborder=0 webkitAllowFullScreen mozallowfullscreen allowfullscreen></iframe>";
			}
			this.abc_blockone.style.width = "30px";
			this.abc_blockone.style.height = "30px";
			this.abc_blockone.style.margin = "0 auto";
			this.abc_blockone.style.textAlign = "left";
			this.abc_blockone.style.backgroundImage = "url(img/loader.gif)";
			this.abc_blockone.style.backgroundPosition = "center center";
			this.abc_blockone.style.backgroundRepeat = "no-repeat";
			this.abc_blockimg.style.width = "30px";
			this.abc_blockimg.style.height = "30px";
			this.abc_blockimg.style.display = "none";
			this.abc_blockimg.style.textAlign = "center";
			this.abc_blockimg.style.background = "url(img/arrows.png) 10000px 10000px no-repeat";
			this.abc_blockimg.style.filter = "alpha(opacity=0)";
			this.abc_blockimg.style.opacity = "0";
			this.abc_blockimg.style.MozOpacity = "0";
			this.abc_center.appendChild(this.abc_blockone);
			this.abc_blockone.appendChild(this.abc_blockimg);
			if(this.contenttype == "image"){
				this.abc_blockimg.appendChild(this.img);
			}else if(this.contenttype == "video"){
				this.abc_blockimg.appendChild(this.iframevideo);
				this.iframevideo.innerHTML = iframe;
				this.iframevideo.getElementsByTagName("iframe")[0].src = url + "?wmode=opaque";
			}
			if(document.all){
				root.abc_center.style.marginTop = "-15px";
			}
			
			this.prel = document.createElement('div');
			this.prel.setAttribute('id','abc_picture');
			this.prel.style.margin = "4px 10px 0 10px";
			this.prel.style.overflow = "hidden";
			this.ptitle = document.createElement('div');
			this.ptitle.style.float = "left";
			this.ptitle.style.width = "90%";
			this.ptitle.style.textAlign = "left";
			this.pnums = document.createElement('div');
			this.pnums.style.float = "right";
			this.pnums.style.width = "10%";
			this.pnums.style.textAlign = "center";
			this.prel.appendChild(this.ptitle);
			this.prel.appendChild(this.pnums);
			this.ptitle.style.display = this.pnums.style.display = "inline-block";
			if(group){
				if(rel == "") rel = "&nbsp;";
				if(this.contenttype == "image"){
					if(this.current_groupname != "null"){
						this.ptitle.innerHTML = rel + " (" + this.current_groupname + ")";
					}else{
						this.ptitle.innerHTML = rel;
					}
				}else if(this.contenttype == "video"){
					if(this.current_groupname_video != "null"){
						this.ptitle.innerHTML = rel + " (" + this.current_groupname_video + ")";
					}else{
						this.ptitle.innerHTML = rel;
					}
				}
				this.pnums.innerHTML = current + "/" + total;
			}else{
				this.ptitle.innerHTML = rel;
			}
			
			this.prel.onmousedown = function(){
				root.statuspicture = false;
			}
			this.prel.onmouseout = function(){
				root.statuspicture = true;
			}
			
			
			if(this.contenttype == "image"){
				if(this.img.complete && document.all){
					this.abc_blockone.style.backgroundPosition = "center 10000px";
					this.abc_blockimg.insertBefore(this.prel,this.img);
					if(rel && rel != ''){
						this.createBlock(this.img,this.img.width + 20,this.img.height + 32,group);
						this.prel.style.height = "18px";
					}else{
						if(group){
							this.createBlock(this.img,this.img.width + 20,this.img.height + 32,group);
							this.prel.style.height = "18px";
						}else{
							this.createBlock(this.img,this.img.width + 20,this.img.height + 22,group);
							this.prel.style.height = "8px";
						}
						this.ptitle.innerHTML = "";
					}
				}
				this.img.onload = function(){
					var w_final = 0;
					var h_final = 0;
					w_final = this.width;
					h_final = this.height;
					/*
					
					var w_final = 0;
					var h_final = 0;
					w_final = this.width;
					h_final = this.height;
				
					if(this.width > root.getMeasures()._w){
						w_final = root.getMeasures()._w - root.margin_title * 2;
						h_final = Math.round((w_final * this.height / this.width) - (root.margin_title * 2));
					}else{
						w_final = this.width;
						h_final = this.height; 
					}
					
					*/
					root.abc_blockone.style.backgroundPosition = "center 10000px";
					root.abc_blockimg.insertBefore(root.prel,this);
					if(rel && rel != ''){
						root.createBlock(root.img,w_final + 20,h_final + 32,group);
						root.prel.style.height = "18px";
					}else{
						if(group){
							root.createBlock(root.img,w_final + 20,h_final + 32,group);
							root.prel.style.height = "18px";
						}else{
							root.createBlock(root.img,w_final + 20,h_final + 22,group);
							root.prel.style.height = "8px";
						}
						root.ptitle.innerHTML = "";
					}
				}
			}else if(this.contenttype == "video"){
				this.abc_blockimg.insertBefore(this.prel,this.iframevideo);
				if(rel && rel != ''){
					this.createBlock(this.iframevideo,Number(w) + 20,Number(h) + 32,group);
					this.prel.style.height = "18px";
				}else{
					if(group){
						this.createBlock(this.iframevideo,Number(w) + 20,Number(h) + 32,group);
						this.prel.style.height = "18px";
					}else{
						this.createBlock(this.iframevideo,Number(w) + 20,Number(h) + 22,group);
						this.prel.style.height = "8px";
					}
					this.ptitle.innerHTML = "";
				}
			}
		}
	}
	
	
	this.createBlock = function(image,w,h,group){
		var root = this;
		var movew = this.iniw;
		var moveh = this.inih;
		var zoomblock = setInterval(zoom,50);
		
		if(group){
			this.arrow_left = document.createElement('div');
			this.arrow_right = document.createElement('div');
			if(root.contenttype == "image"){
				this.arrow_left.style.width = this.arrow_right.style.width = "60px";
				this.arrow_left.style.marginTop = this.arrow_right.style.marginTop = this.margin_title + "px";
			}else if(root.contenttype == "video"){
				this.arrow_left.style.width = this.arrow_right.style.width = "60px";
				this.arrow_left.style.marginLeft = "-60px";
			}
			this.arrow_left.style.height = this.arrow_right.style.height = "60px";
			this.arrow_left.style.position = this.arrow_right.style.position = "absolute";
			this.arrow_left.style.textAlign = this.arrow_right.style.textAlign = "center";
			
			var aleft = document.createElement('a');
			aleft.setAttribute('href','javascript:;');
			this.arrow_left.appendChild(aleft);
			if(this.contenttype == "video"){
				var left = new Image();
				//left.src = "img/left.gif";
				left.style.border = "none";
				aleft.appendChild(left);
				left.style.display = "none";
				aleft.style.background = "url(img/left.png) center center no-repeat";
			}
			
			var aright = document.createElement('a');
			aright.setAttribute('href','javascript:;');
			this.arrow_right.appendChild(aright);
			if(this.contenttype == "video"){
				var right = new Image();
				right.style.border = "none";
				aright.appendChild(right);
				right.style.display = "none";
				aright.style.background = "url(img/right.png) center center no-repeat";
			}
			
			aright.style.display = aleft.style.display = "block";
			aright.style.outline = aleft.style.outline = "0";
			
			var grouplenght;
			if(this.contenttype == "image"){
				aleft.style.width = "60px";
				aright.style.width = "60px";
				grouplenght = this.current_group.length;
			}else if(this.contenttype == "video"){
				aleft.style.width = "60px";
				aright.style.width = "60px";
				grouplenght = this.current_group_videos.length;
			}
			if(group <= 1){
				if(this.contenttype == "video"){
					aleft.style.visibility = "hidden";
				}
				this.arrow_left.style.visibility = "hidden";
				
				this.leftstatus = false;
				this.rightstatus = true;
			}else if(group >= grouplenght){
				if(this.contenttype == "video"){
					aright.style.visibility = "hidden";
				}
				this.arrow_right.style.visibility = "hidden";
				
				this.leftstatus = true;
				this.rightstatus = false;
			}else{
				if(this.contenttype == "video"){
					aleft.style.visibility = "visible";
					aright.style.visibility = "visible";
				}
				this.arrow_left.style.visibility = "visible";
				this.arrow_right.style.visibility = "visible";
				
				this.leftstatus = this.rightstatus = true;
			}
				
			
			aleft.onclick = function(){
				root.startPictures(aleft,aright,"left");
				return false;
			}
			
			aright.onclick = function(){
				root.startPictures(aleft,aright,"right");
				return false;
			}
			
			if(this.contenttype == "image"){
				aleft.onmouseover = function(){
					root.img.style.filter = "alpha(opacity=50)";
					root.img.style.opacity = "0.5";
					root.img.style.MozOpacity = "0.5";
					root.abc_blockimg.style.backgroundPosition = "left center";
				}
				aleft.onmouseout = function(){
					root.img.style.filter = "alpha(opacity=100)";
					root.img.style.opacity = "1";
					root.img.style.MozOpacity = "1";
					root.abc_blockimg.style.backgroundPosition = "10000px 10000px";
				}
				aright.onmouseover = function(){
					root.img.style.filter = "alpha(opacity=50)";
					root.img.style.opacity = "0.5";
					root.img.style.MozOpacity = "0.5";
					root.abc_blockimg.style.backgroundPosition = "right center";
				}
				aright.onmouseout = function(){
					root.img.style.filter = "alpha(opacity=100)";
					root.img.style.opacity = "1";
					root.img.style.MozOpacity = "1";
					root.abc_blockimg.style.backgroundPosition = "10000px 10000px";
				}
			}
			
			this.keyFunction(aleft,aright);
			this.statuspicture = false;
			
		}else{
			this.keyFunction(null,null);
		}
		
		
		this.btclose = document.createElement('a');
		this.btclose.setAttribute('href','javascript:;');
		this.btclose.style.display = "block";
		this.btclose.style.width = "40px";
		this.btclose.style.height = "40px";
		this.btclose.style.marginTop = "-20px";
		this.btclose.style.background = "url(img/close.png) center center no-repeat";
		this.btclose.style.outline ="0";
		this.btclose.style.position ="absolute";
		this.btclose.style.zIndex = "202";
		this.abc_blockone.appendChild(this.btclose);
		this.btclose.onclick = function(){
			root.ABChide();
		}
		
		
		if(this.contenttype == "image"){
			this.btclose.onmouseover = function(){
				root.img.style.filter = "alpha(opacity=50)";
				root.img.style.opacity = "0.5";
				root.img.style.MozOpacity = "0.5";
				root.abc_blockimg.style.backgroundPosition = "center center";
			}
			
			this.btclose.onmouseout = function(){
				root.img.style.filter = "alpha(opacity=100)";
				root.img.style.opacity = "1";
				root.img.style.MozOpacity = "1";
				root.abc_blockimg.style.backgroundPosition = "10000px 10000px";
			}
		}
		
		function zoom(){
			movew+= (w - movew) * root.coefficient;
			moveh+= (h - moveh) * root.coefficient;
			if(Math.round(movew) == w && Math.round(moveh) == h){
				clearInterval(zoomblock);
				root.abc_blockone.style.width = w + "px";
				root.abc_blockone.style.height = h + "px";
				root.abc_blockimg.style.width = w + "px";
				root.abc_blockimg.style.height = h + "px";
				if(document.all){
					root.abc_center.style.marginTop = h / -2 + "px";
				}
				root.abc_blockimg.style.display = "block";
				root.abc_blockimg.style.position = "absolute";
				root.fadeElement(root.abc_blockimg,0,100,true);
				root.onFinishFade = function(e){
					if(e){
						root.statuspicture = true;
					}
				}
				
				root.statusclose = true;
				if(group){
					if(root.contenttype == "image"){
						root.arrow_right.style.marginLeft = (w/2) + "px";
						root.arrow_right.style.width = root.arrow_left.style.width = (w/2) + "px";
						root.arrow_left.childNodes[0].style.width = root.arrow_right.childNodes[0].style.width = (w/2) + "px";
						root.arrow_left.childNodes[0].style.height = root.arrow_right.childNodes[0].style.height = h + "px";
					}else if(root.contenttype == "video"){
						root.arrow_right.style.marginLeft = w + "px";
					}
					root.arrow_left.style.height = root.arrow_right.style.height = h - root.margin_title + "px";
					aleft.style.height = aright.style.height = h - root.margin_title + "px";
					if(root.contenttype == "video"){
						var himg = root.arrow_left.getElementsByTagName("img")[0].height / 2;
						root.arrow_left.getElementsByTagName("img")[0].style.marginTop = root.arrow_right.getElementsByTagName("img")[0].style.marginTop = ((h / 2) - himg) + "px";
					}
					root.abc_blockone.appendChild(root.arrow_left);
					root.abc_blockone.appendChild(root.arrow_right);
				}
				root.btclose.style.marginLeft = (w - 20) + "px";
				root.iniw = w;
				root.inih = h;
				
				return false;
				
			}else{
				root.abc_blockone.style.width = movew + "px";
				root.abc_blockone.style.height = moveh + "px";
				root.abc_blockimg.style.width = movew + "px";
				root.abc_blockimg.style.height = moveh + "px";
				if(document.all){
					root.abc_center.style.marginTop = moveh / -2 + "px";
				}
				if(group){
					if(root.contenttype == "image"){
						root.arrow_right.style.marginLeft = (movew / 2) + "px";
						root.arrow_right.style.width = root.arrow_left.style.width = (movew / 2) + "px";
						root.arrow_left.childNodes[0].style.width = root.arrow_right.childNodes[0].style.width = (movew/2) + "px";
						root.arrow_left.childNodes[0].style.height = root.arrow_right.childNodes[0].style.height = moveh + "px";
					}else if(root.contenttype == "video"){
						root.arrow_right.style.marginLeft = movew + "px";
					}
					root.arrow_left.style.height = root.arrow_right.style.height = moveh - root.margin_title + "px";
					aleft.style.height = aright.style.height = moveh - root.margin_title + "px";
				}
				root.btclose.style.marginLeft = (movew - 20) + "px";
				
				return false;
			}
		}
		
	}
	
	this.startPictures = function(left,right,type){
		if(this.statuspicture){
			this.statuspicture = false;
			var root = this;
			if(type == "left"){
				if(this.contenttype == "image"){
					this.current_index--;
					if(this.current_index > 0){
						this.arrow_right.style.visibility = "visible";
						
						this.rightstatus = true;
					}else{
						this.current_index = 0;
						this.arrow_left.style.visibility = "hidden";
						this.arrow_right.style.visibility = "visible";
						this.rightstatus = true;
						this.leftstatus = false;
					}
					this.showNewImage(type,this.current_group[this.current_index].rel);
				}else if(this.contenttype == "video"){
					this.current_index_video--;
					if(this.current_index_video > 0){
						right.style.visibility = "visible";
						this.arrow_right.style.visibility = "visible";
						
						this.rightstatus = true;
					}else{
						this.current_index_video = 0;
						right.style.visibility = "visible";
						left.style.visibility = "hidden";
						this.arrow_left.style.visibility = "hidden";
						
						this.rightstatus = true;
						this.leftstatus = false;
					}
					this.showNewImage(type,this.current_group_videos[this.current_index_video].rel);
				}
			}else if(type == "right"){
				if(this.contenttype == "image"){
					this.current_index++;
					if(this.current_index < this.current_group.length - 1){
						this.arrow_left.style.visibility = "visible";
						
						this.leftstatus = true;
					}else{
						this.current_index = this.current_group.length - 1;
						this.arrow_right.style.visibility = "hidden";
						this.arrow_left.style.visibility = "visible";
						this.leftstatus = true;
						this.rightstatus = false;
					}
					this.showNewImage(type,this.current_group[this.current_index].rel);
				}else if(this.contenttype == "video"){
					this.current_index_video++;
					if(this.current_index_video < this.current_group_videos.length - 1){
						left.style.visibility = "visible";
						this.arrow_left.style.visibility = "visible";
						
						this.leftstatus = true;
					}else{
						this.current_index_video = this.current_group_videos.length - 1;
						left.style.visibility = "visible";
						right.style.visibility = "hidden";
						this.arrow_right.style.visibility = "hidden";
						
						this.leftstatus = true;
						this.rightstatus = false;
					}
					this.showNewImage(type,this.current_group_videos[this.current_index_video].rel);
				}
			}
		}
	}
	
	
	this.showNewImage = function(direction,rel){
		var root = this;
		this.statusclose = false;
		this.statusload = true;
		
		if(rel == "") rel = "&nbsp;";
		if(this.contenttype == "image"){
			if(rel != ''){
				if(this.current_groupname != "null"){
					this.ptitle.innerHTML = rel + " (" + this.current_groupname + ")";
				}else{
					this.ptitle.innerHTML = rel;
				}
			}else{
				this.ptitle.innerHTML = "";
			}
			this.pnums.innerHTML = this.current_group[this.current_index].index + 1 + "/" + this.totalgroup;
		}else if(this.contenttype == "video"){
			if(rel != ''){
				if(this.current_groupname_video != "null"){
					this.ptitle.innerHTML = rel + " (" + this.current_groupname_video + ")";
				}else{
					this.ptitle.innerHTML = rel;
				}
			}else{
				this.ptitle.innerHTML = "";
			}
			this.pnums.innerHTML = this.current_group_videos[this.current_index_video].index + 1 + "/" + this.totalgroupvideos;
		}
		this.abc_blockimg.style.display = "none";
		
		
		if(this.contenttype == "image"){
			this.abc_blockimg.removeChild(this.img);
			this.img = null;
			this.img = new Image();
			this.abc_blockimg.appendChild(this.img);
			this.img.setAttribute('src',this.current_group[this.current_index].url);
			this.abc_blockone.style.backgroundPosition = "center center";
		}else if(this.contenttype == "video"){
			this.abc_blockimg.removeChild(this.iframevideo);
			this.iframevideo = document.createElement('div');
			this.abc_blockimg.appendChild(this.iframevideo);
			var w = this.current_group_videos[this.current_index_video].w;
			var h = this.current_group_videos[this.current_index_video].h;
			var iframe = "<iframe src='' height='" + h + "' width='" + w + "' style='background: black url(img/loader.gif) center center no-repeat' scrolling='no' frameborder=0 allowfullscreen></iframe>";
			this.iframevideo.innerHTML = iframe;
			this.iframevideo.getElementsByTagName("iframe")[0].src = this.current_group_videos[this.current_index_video].url + "?wmode=opaque";
		}
		
		
		if(this.contenttype == "image"){
			if(this.img.complete && document.all){
				if(this.statusload){
					this.statusload = false;
					if(!rel && rel == ''){
						this.ptitle.innerHTML = "";
					}
					this.moveBlock(this.img,this.img.width + 20,this.img.height + 32);
					this.prel.style.height = "18px";
					this.abc_blockone.style.backgroundPosition = "center 10000px";
				}
			}
			this.img.onload = function(){
				root.img.width_new = 100;
				if(root.statusload){
					root.statusload = false;
					if(!rel && rel == ''){
						root.ptitle.innerHTML = "";
					}
					root.moveBlock(root.img,root.img.width + 20,root.img.height + 32);
					root.prel.style.height = "18px";
					root.abc_blockone.style.backgroundPosition = "center 10000px";
				}
			}
			
		}else if(this.contenttype == "video"){ 
			if(!rel && rel == ''){
				this.ptitle.innerHTML = "";
			}
			this.moveBlock(this.iframevideo,Number(w) + 20,Number(h) + 32);
			this.prel.style.height = "18px";
		}
			
	}
	
	
	this.moveBlock = function(image,w,h){
		this.statuspicture = false;
		var root = this;
		var movew = this.iniw;
		var moveh = this.inih;
		var zoomblock = setInterval(zoom,50);
		
		
		function zoom(){
			movew+= (w - movew) * root.coefficient;
			moveh+= (h - moveh) * root.coefficient;
			if(Math.round(movew) == w && Math.round(moveh) == h){
				clearInterval(zoomblock);
				root.abc_blockone.style.width = w + "px";
				root.abc_blockone.style.height = h + "px";
				root.abc_blockimg.style.width = w + "px";
				root.abc_blockimg.style.height = h + "px";
				if(document.all){
					root.abc_center.style.marginTop = h / -2 + "px";
				}

				root.arrow_left.style.height = h + "px";
				root.arrow_right.style.height = h + "px";

				root.abc_blockimg.style.display = "block";
				root.fadeElement(root.abc_blockimg,0,100,true);
				root.onFinishFade = function(e){
					if(e){
						root.statuspicture = true;
					}
				}

				root.statusclose = true;
				
				root.arrow_left.style.height = root.arrow_right.style.height = h + "px";
				if(root.contenttype == "video"){
					var himg = root.arrow_left.getElementsByTagName("img")[0].height / 2;
					root.arrow_left.getElementsByTagName("img")[0].style.marginTop = root.arrow_right.getElementsByTagName("img")[0].style.marginTop = ((h / 2) - himg) + "px";
				}
				if(root.contenttype == "image"){
					root.arrow_right.style.marginLeft = w / 2 + "px";
					root.arrow_right.style.width = root.arrow_left.style.width = w / 2 + "px";
					root.arrow_left.childNodes[0].style.width = root.arrow_right.childNodes[0].style.width = (w/2) + "px";
					root.arrow_left.childNodes[0].style.height = root.arrow_right.childNodes[0].style.height = h + "px";
				}else if(root.contenttype == "video"){
					root.arrow_right.style.marginLeft = w + "px";
					
				}
				root.btclose.style.marginLeft = (w - 20) + "px";
				if(root.contenttype == "video"){
					root.arrow_left.getElementsByTagName("a")[0].style.height = root.arrow_right.getElementsByTagName("a")[0].style.height = h + "px";
				}
				root.iniw = w;
				root.inih = h;
				
				return false;
			}else{
				root.abc_blockone.style.width = movew + "px";
				root.abc_blockone.style.height = moveh + "px";
				root.abc_blockimg.style.width = movew + "px";
				root.abc_blockimg.style.height = moveh + "px";
				if(document.all){
					root.abc_center.style.marginTop = moveh / -2 + "px";
					root.arrow_left.style.height = root.arrow_right.style.height = moveh + "px";
				}
				
				root.arrow_left.style.height = moveh + "px";
				root.arrow_right.style.height = moveh + "px";
				if(root.contenttype == "video"){
					var himg = root.arrow_left.getElementsByTagName("img")[0].height / 2;
					root.arrow_left.getElementsByTagName("img")[0].style.marginTop = root.arrow_right.getElementsByTagName("img")[0].style.marginTop = ((moveh / 2) - himg) + "px";
					root.arrow_left.getElementsByTagName("a")[0].style.height = root.arrow_right.getElementsByTagName("a")[0].style.height = moveh + "px";
				}
				
				if(root.contenttype == "image"){
					root.arrow_right.style.marginLeft = (movew / 2) + "px";
					root.arrow_right.style.width = root.arrow_left.style.width = movew / 2 + "px";
					root.arrow_left.childNodes[0].style.width = root.arrow_right.childNodes[0].style.width = (movew/2) + "px";
					root.arrow_left.childNodes[0].style.height = root.arrow_right.childNodes[0].style.height = moveh + "px";
				}else if(root.contenttype == "video"){
					root.arrow_right.style.marginLeft = movew + "px";
				}
				root.btclose.style.marginLeft = (movew - 20) + "px";
				return false;
			}
		}
	}
	
}