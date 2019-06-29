#show databases;
show tables from tracks;
use tracks;
select * from auth_user;
select * from tracks_album;
select * from tracks_artist;
select * from tracks_features;

-- select * from tracks_audiolyricsembedding;
-- select * from tracks_audiolyricstop20;

-- select * from tracks_survey20tracks;
-- select * from tracks_survey20tracksfeatures;
-- select * from tracks_surveyresults;
-- select * from tracks_usersurveycompleted;

-- select * from tracks_recsysresults;
select * from tracks_recsysresults2;
-- select * from tracks_recfromrlresults;

SELECT COUNT(*) FROM tracks_features;  # 計算資料筆數

# 複製資料表
CREATE TABLE tracks_recsysresults2 LIKE tracks_recsysresults;
INSERT tracks_recsysresults2 SELECT * FROM tracks_recsysresults;

#DROP TABLE tracks_artist;
#DROP TABLE tracks_features;
#DROP TABLE tracks_survey20tracks;