from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('album/info/logs', views.music_record_logs, name='music_record_logs'),

    # path('sql_example', views.sql_join_table_example, name="sql_join_table_example"),
    path('album/info/<slug:album_id>', views.ablum_info, name="album_info"),
    path('browser/artist/', views.browser_artist, name="browser_artist"),
    path('browser/artist/<slug:letter>', views.browser_artist_from_letter, name="browser_artist_from_letter"),
    path('artist/info/<slug:artist_id>', views.artist_info, name="artist_info"),
    path('add', views.add_to_playlist, name="add_playlist_from_id"),
    path('remove', views.remove_from_playlist, name="remove_from_playlist"),
    path('user/playlist/', views.user_playlist, name="user_playlist"),
    
    # questionnarire
    path('first/questionnarire', views.first_login_questionnarire, name="first_login_questionnarire"),
    path('finished/questionnarire',views.get_questionnarire, name="get_questionnarire"),

    # recommender
    path('browser/madeforyou/', views.madeforyou_browser, name="madeforyou_browser"),
    path('browser/madeforyou/list/<slug:choosed_list_id>', views.madeforyou_choosed_a_playlist, name="madeforyou_choosed_a_playlist"),
]
