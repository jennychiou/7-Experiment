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
select * from tracks_recsysresults;

# 清除資料 
delete from tracks_recsysresults where user_id = 'lintimken' and recom_method = '2';

# 更新score欄位值
UPDATE tracks_recsysresults_a SET score = '';