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
    # Every time user refresh page will get 30 different artists.
    sql = 'select * from tracks_artist order by rand() limit 30'
    dict_row = run_sql_cmd(sql)
    return render(request,'browserArtist.html',{
        'artist_list':dict_row,
    })

@login_required
def browser_artist_from_letter(request, letter):
    sql = "SELECT * from  tracks.tracks_artist where Name LIKE '" + letter +"%'"
    dict_row = run_sql_cmd(sql)
    return render(request,'selected_artist.html',{
        'artist_list':dict_row,
    })

@login_required
def artist_info(request, artist_id):
    sql = "select * from tracks_album where artist_id ='" + artist_id +"'ORDER BY release_date DESC;"
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
	where album.artist_id = artist.id) M \
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
                X left join tracks.tracks_artist as A on A.id = X.artist_id"
    dict_row = run_sql_cmd(sql)
    random.shuffle(dict_row)
    return render(request,'userPlaylist.html',{
        'playlist':dict_row,
    })


@login_required
def madeforyou_browser(request):
    playlist_name = ['LIST 1', 'LIST 2', 'LIST 3', 'LIST 4']
    return render(request,'madeForYou.html', {
        'numberoflist':playlist_name
    })

@login_required
def madeforyou_choosed_a_playlist(request, choosed_list_id):
    user = str(request.user)
    sql = "select * from tracks.tracks_recsysresults where recom_method ='" + choosed_list_id + "'"
    return render(request,'madeForYouChoose.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    
    return [dict(zip(columns, row))
        for row in cursor.fetchall()]

def run_sql_cmd(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)

