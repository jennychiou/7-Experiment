#show databases;
set SQL_SAFE_UPDATES = 0;
show tables from tracks;
use tracks;
select * from auth_user;
select * from tracks_album;
select * from tracks_artist;
select * from tracks_features;
select * from tracks_lyrics;

select * from tracks_audiolyricsembedding;
select * from tracks_audiolyricstop20;

-- select * from tracks_survey20tracks;
select * from tracks_survey20tracksfeatures;
select * from tracks_survey20trackstop20;
select * from tracks_surveyresults;
select * from tracks_usersurveycompleted;
select * from tracks_dataforrec;

select * from tracks_recsysresults;  # 音頻推薦
-- select * from tracks_recsysresults2;
-- select * from tracks_recfromrlresults;

SELECT COUNT(*) FROM tracks_features;  # 計算資料筆數
SELECT COUNT(*) FROM tracks_dataforrec;

# 複製資料表
CREATE TABLE tracks_recsysresults LIKE tracks_recsysresults;
-- INSERT tracks_recsysresults2 SELECT * FROM tracks_recsysresults_a;

#DROP TABLE tracks_artist;
#DROP TABLE tracks_features;
#DROP TABLE tracks_survey20tracks;
#DROP TABLE tracks_recsysresults;