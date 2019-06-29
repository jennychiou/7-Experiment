from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .Module.UseMongoDB import RecSysLogsToMongo
import json
import glob
from django.db import connection
from django.contrib.auth.decorators import login_required
from datetime import datetime
import random

db = RecSysLogsToMongo()
def check_ifcompleted_survey(user):
    '''
        驗證使用者是否填過調查表(第一次登入要填)
    '''
    sql = "select * from tracks.tracks_usersurveycompleted where user = '" + user + "' ORDER BY complete_date DESC LIMIT 1;"
    user_recod = run_sql_cmd(sql)
    if user_recod:
        return True
    else:
        return False

@login_required
def index(request):
    user = str(request.user)
    if check_ifcompleted_survey(user):
        print('User', user, 'Completed 20 tracks Survey!')
        return redirect('browser_artist')
    else:
        print('User', user, 'unCompleted 20 tracks Survey!')
        return redirect('first_login_questionnarire')

@login_required
def first_login_questionnarire(request):
    sql="select * from  tracks.tracks_survey20tracks"
    dict_row = run_sql_cmd(sql)
    return render(request,'loginQuestionnaire.html',{
        'questions':dict_row,
    })

@csrf_exempt
def get_questionnarire(request):
    if request.method == 'POST':
        user_name = str(request.user)
        rate_data = request.body.decode('utf-8')
        results = {}
        for item in rate_data.split('&'):
            key, value = item[:-2], item[-1]
            results[key] = value
        insert_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # store results to MySQL.
        insert_query = "INSERT INTO tracks.tracks_surveyresults(`user`, `results`, `date`) VALUES {values};".format(
            values = (user_name, str(results), insert_date)
        )
        with connection.cursor() as cursor: 
            cursor.execute(insert_query)

        # also backup at mongoDB.
        results['user'] = user_name 
        db.insert_servey_results_to_mongodb(results)

        # complete timestamp record (to mysql).
        insert_query = "INSERT INTO tracks.tracks_usersurveycompleted(`user`, `complete_date`) VALUES {values};".format(
            values  = (user_name, insert_date)
        )
        with connection.cursor() as cursor: 
            cursor.execute(insert_query)
        return redirect('index')

@csrf_exempt
def music_record_logs(request):
    if request.method == 'POST':
        db.insert_log_to_mongodb(request.body)
        return HttpResponse(request.body)

@csrf_exempt
def add_to_playlist(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = data['user']
        track_info = data['track'].split(':')
        print(track_info)
        ablum_id, track_id = track_info[0], track_info[1]
        row = (user, track_id, ablum_id)
        sql = "INSERT INTO tracks.tracks_userslike (`user`, `track`, `album`) VALUES "+ str(row) + ";"
        with connection.cursor() as cursor:
                cursor.execute(sql)
        return HttpResponse('Add')

@csrf_exempt
def remove_from_playlist(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = data['user']
        track_info = data['track'].split(':')
        ablum_id, track_id = track_info[0], track_info[1]
        sql = "delete from tracks_userslike where user ='" + user+ "' and track ='"+ track_id +"' and album ='" +ablum_id+ "';"
        with connection.cursor() as cursor:
                cursor.execute(sql)
        return HttpResponse('Remove')


@login_required
def browser_artist(request):
    user = str(request.user)
    # Every time user refresh page will get 30 different artists.
    if check_ifcompleted_survey(user):
        print('User', user, 'Completed 20 tracks Survey!')
        sql = 'select * from tracks_artist order by rand() limit 30'
        dict_row = run_sql_cmd(sql)
        return render(request,'browserArtist.html',{
            'artist_list':dict_row,
        })
    else:
        print('User', user, 'unCompleted 20 tracks Survey!')
        return redirect('first_login_questionnarire')
    

@login_required
def browser_artist_from_letter(request, letter):
    sql = "SELECT * from  tracks.tracks_artist where Name LIKE '" + letter +"%'"
    dict_row = run_sql_cmd(sql)
    return render(request,'selected_artist.html',{
        'artist_list':dict_row,
    })

@login_required
def artist_info(request, artist_id):
    sql = "select * from tracks_album where artist ='" + artist_id +"'ORDER BY release_date DESC;"
    dict_row = run_sql_cmd(sql)
    return render(request,'artistInfo.html',{
        'artist_album':dict_row,
    })

@login_required
def ablum_info(request, album_id):
    user_name = request.user    
    sql = "select track_id, artist, artist_id, album_name, album_id, img, name, preview_url, user  from ( \
	select  features.id as track_id, M.artist, M.artist_id, M.album_name, M.album_id,  M.img, features.id, features.name, features.preview_url \
	from tracks_features as features INNER JOIN  ( \
	SELECT artist.name as artist, artist.id as artist_id, album.name as album_name, \
	album.img_url as img, album.id as album_id \
	FROM tracks_artist as artist \
	INNER JOIN tracks_album as album \
	where album.artist = artist.id) M \
        where M.album_id = features.album_id and M.album_id = '" + album_id + "' ) Album \
	left Join tracks.tracks_userslike as L  on L.track = Album.id and L.user = '" + str(user_name) + "'"
    dict_row = run_sql_cmd(sql)
    
    for item in dict_row:
        if item['user'] == None:
            item['user'] = ''
    return render(request,'album.html',{
        'album':dict_row,
    })

@login_required
def user_playlist(request):
    user_name = request.user 
    sql = "select A.id as artist_id, X.p as preview_url, X.track_id, X.album_id, X.track_name, A.name as artist_name, X.user, X.img_url from ( \
                select * from ( select L.track as track_id, L.user, F.album_id, F.name as track_name, F.preview_url as p \
                from tracks.tracks_userslike as L \
	            INNER JOIN tracks.tracks_features as F \
                where L.track = F.id and L.user ='"+ str(user_name) + "') \
                List left join tracks.tracks_album as Album on List.album_id = Album.id )\
                X left join tracks.tracks_artist as A on A.id = X.artist"
    dict_row = run_sql_cmd(sql)
    random.shuffle(dict_row)
    return render(request,'userPlaylist.html',{
        'playlist':dict_row,
    })

'''
Made for you 頁面瀏覽, 分為四個播放清單分別用不同方法, 
分成兩個table : tracks_recsysresults, tracks_recfromrlresults
'''
@login_required
def madeforyou_browser(request):
    preview_img  = []
    
    '''
    兩次SQL分別撈不同內容資料 
    1. 撈取 tracks_recsysresults table 資料 判斷有哪些(推薦方法)清單有資料
    2. tracks_recfromrlresults 的資料 並且為最新 也就是number_of_rec_times 最大的
    '''
    for list_num in range(0, 3):
        sql = 'SELECT album_img_url from tracks.tracks_recsysresults where recom_method =' + str(list_num) + ' ORDER by recom_rank limit 1'
        with connection.cursor() as cursor:
            cursor.execute(sql)
            img = cursor.fetchone()
            if img:
                preview_img.append(img)
            else:
                preview_img.append('') 
    rl_sql = 'select album_img_url from tracks.tracks_recfromrlresults where number_of_rec_times =\
    (select max(number_of_rec_times) from tracks.tracks_recfromrlresults)'

    with connection.cursor() as cursor:
        cursor.execute(sql)
    rl_img = cursor.fetchone()
    return render(request,'madeForYou.html', {
        'numberoflist':preview_img,
        'rl_img_url':rl_img
    })

'''
選擇 0, 1, 2 類型推薦清單
'''
@login_required
def madeforyou_choosed_a_playlist(request, choosed_list_id):
    user = str(request.user)
    sql = "SELECT user_id, name, track_id, recom_rank, score, preview_url, album_id, artist_name, recom_method\
        FROM tracks.tracks_recsysresults as R \
        INNER JOIN tracks.tracks_features as F \
        ON R.track_id = F.id and R.user_id ='" + user +"'and R.score=0 and R.recom_method ='"+ choosed_list_id+ "'\
        ORDER by recom_rank"
    dict_row = run_sql_cmd(sql)
    return render(request,'madeForYouChoose.html',{
        'tracks':dict_row,
    })

'''
0, 1, 2 類型推薦清單提交評分結果, 更新MySQL, 存到MongoDB
MongoDB collectons 名稱為 recRatefromUser
'''
@csrf_exempt
def submit_rec_result_from_user(request):
    user = str(request.user)
    if request.method == 'POST':
        r = request.body.decode('utf-8')
        results = {}
        form_data = r.split('&')
        recom_method = form_data[-1].split('=')[1]
        for row in form_data[:-1]:
            row = row.split('=')
            key, value = row[0], row[1]  # track id , score  
            # update each track which Be rated
            sql = "UPDATE tracks.tracks_recsysresults SET score="+ value +" WHERE track_id = '"+ key +"'\
            and user_id='" + user + "' and recom_method='"+ recom_method + "';"
            results[key] = value
            with connection.cursor() as cursor:
                cursor.execute(sql)
           
        # update finidhed then return to madeforyou_browser page
        results['user_id'] = user
        results['recom_method'] = recom_method

        db.insert_rec_result_to_mongodb(results)  # 備份到mongodb
        
        return redirect('madeforyou_browser')
'''
選擇 RL (Weekly Update)推薦清單
'''
@login_required
def madeforyou_weeklyupdate(request):
    user = str(request.user)
    sql = "SELECT user_id, artist_name, track_id, recom_rank, score, album_img_url, number_of_rec_times, F.preview_url as preview_url\
           from tracks.tracks_recfromrlresults as RL\
           INNER JOIN tracks.tracks_features as F\
           ON RL.track_id = F.id and RL.user_id = '" +user +"'\
           and score=0 and number_of_rec_times = ( select max(number_of_rec_times) from tracks.tracks_recfromrlresults)\
           ORDER by recom_rank"
    
    dict_row = run_sql_cmd(sql)
    return render(request,'madeOfYouWeeklyUpdate.html',{
        'tracks':dict_row,
    })

'''
提交 RL (Weekly Update) 推薦評分結果, 更新MySQL, 存到MongoDB
MongoDB collection 名稱為 RLRatefromUser
'''
@csrf_exempt
def submit_weeklyrec_results_from_user(request):
    user = str(request.user)
    if request.method == 'POST':
        r = request.body.decode('utf-8')
        results = {}
        form_data = r.split('&')
        number_of_rec_times = form_data[-1].split('=')[1]
        for row in form_data[:-1]:
            row = row.split('=')
            key, value = row[0], row[1] # track id, scroe 

            # update each track which Be rated
            sql = "UPDATE tracks.tracks_recfromrlresults SET score="+ value +" WHERE track_id = '"+ key +"'\
            and user_id='" + user  +"' and number_of_rec_times= '" + number_of_rec_times +"'"
            results[key] = value

            with connection.cursor() as cursor:
                cursor.execute(sql)
        
        results['user_id'] = user # update finidhed then return to madeforyou_browser page
    
        db.insert_RL_rec_result_to_mongodb(results) # 備份到mongodb
        return redirect('madeforyou_browser')



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    
    return [dict(zip(columns, row))
        for row in cursor.fetchall()]

def run_sql_cmd(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)

