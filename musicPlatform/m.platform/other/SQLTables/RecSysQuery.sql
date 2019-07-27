set SQL_SAFE_UPDATES = 0; # 解除輸入的安全模式
use tracks;
# content base推薦方法
# 用戶id
set @user_id = (select user from tracks_surveyresults);

# 歌曲ID track_id
set @track_id = '000xQL6tZNLJzIrtIgxqSl';

# 專輯圖片album_img_url
set @album_id = (select album_id from tracks_features where id = @track_id);
set @album_img_url = (select img_url from tracks_album where id = @album_id);

# 歌手名稱 artist_name
set @artist_id = (select artist_id from tracks_features where id = @track_id);
set @artist_name = (select artist_name from tracks_artist where id = @artist_id);

# 推薦方法 recom_method
set @recom_method = '0';

# 推薦排序 recom_rank
set @results = (select results from tracks_surveyresults);
set @recom_rank = '1';

# 分數 score
set @score = '4';

# 寫入資料表
insert into tracks_recsysresults (user_id, album_img_url, track_id, artist_name, recom_method, recom_rank, score) values (@user_id, @album_img_url, @track_id, @artist_name, @recom_method, @recom_rank, @score);

# 清除資料 
delete from tracks_recsysresults where user_id = 'chiouzihling' and recom_method = 1;
delete from tracks_recfromrlresults where user_id = 'vivian' and number_of_rec_times = 10;

# 推薦結果 / 計算資料筆數
select * from tracks_recsysresults;
SELECT COUNT(*) FROM tracks_recsysresults;

select * from tracks_recfromrlresults; # RL推薦
SELECT COUNT(*) FROM tracks_recfromrlresults;

#啟動編輯模式
set SQL_SAFE_UPDATES = 0;

# 更新score欄位值
UPDATE tracks_recsysresults SET score = '5' where user_id = 'smallhsu' and recom_method = 2 and recom_rank = 2;
UPDATE tracks_recfromrlresults SET number_of_rec_times = 1 where user_id = 'chiouchingyi' and recom_rank = 20;
UPDATE tracks_recfromrlresults SET score = '1' where user_id = 'alex' and track_id = '1lPaNFyURi7x5McVUZrlzI' and number_of_rec_times = 18; #更改後另一個帳號可顯示