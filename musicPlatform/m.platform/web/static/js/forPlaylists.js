
// var lastClickTime = new Date();
// var listenTime;
// var currentTime;
// var player_detial = {};

// function change() {
//     $('#player').attr('src', "{% static 'music/' %}" +event.target.innerHTML + '.mp3');
    
//     // 總共聽的時間
//     listenTime = computeListenTime(new Date())
//     console.log(listenTime)

//     // 切歌時判斷 currentTime 超過30秒
//     if (currentTime >30){
//         var xhr = new XMLHttpRequest();
//         xhr.open('POST', url= 'logs');
//         xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
//         xhr.send(JSON.stringify(player_detial));
//         player_detial['ended'] == false
//     }
//     $('#song_name').text(event.target.innerHTML);
// }

// function computeListenTime(switchTime){
//     listenTime = switchTime - lastClickTime;
//     lastClickTime = switchTime
//     return (listenTime/1000)
// }

// (function (window, undefined) {
//     var player = document.getElementById('player')
//     map = ['error', 'src', 'currentSrc', 'readyState', 'preload', 'seeking', 'seeked',
//         'currentTime', 'duration', 'paused', 'playbackRate','loop', 'controls', 'volume','ended',];
//     window.setInterval(function () {
//         for (var i = 0, j = map.length; i < j; i++) {
//             player_detial[map[i]] = player[map[i]];
//             player_detial['played'] = { "start": player.played.start(0), "end": player.played.end(0) }
//             player_detial['seekable'] = { "Start": player.seekable.start(0), "End": player.seekable.end(0) }
//             var xhr = new XMLHttpRequest();

//             ifEnded = player_detial['ended']
//             currentTime = player_detial['currentTime']
//         }
//         if ((ifEnded == true))
//             {
//                 player.currentTime = 0;
//                 xhr.open('POST', url= 'logs');
//                 xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
//                 xhr.send(JSON.stringify(player_detial));
//                 player_detial['ended'] == false
//             }
//     }, 1000);
// }
// )(window);