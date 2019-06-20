#show databases;
show tables from tracks;
use tracks;
select * from auth_user;
select * from tracks_album;
select * from tracks_artist;
select * from tracks_features;
select * from tracks_survey20tracks;
select * from tracks_usersurveycompleted;

SELECT COUNT(*) FROM tracks_features;  # 計算資料筆數

#DROP TABLE tracks_artist;
#DROP TABLE tracks_features;
#DROP TABLE tracks_survey20tracks;