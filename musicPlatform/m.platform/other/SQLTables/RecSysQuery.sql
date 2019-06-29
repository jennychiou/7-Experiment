use tracks;

-- content base推薦方法
-- 用戶id

-- 專輯圖片album_img_url
set @id = '000xQL6tZNLJzIrtIgxqSl';
set @album_id = (select album_id from tracks_features where id = @id);
set @album_img_url = (select img_url from tracks_album where id = @album_id);

-- 歌曲ID track_id

-- 歌手名稱 artist_name
set @id = '000xQL6tZNLJzIrtIgxqSl';
set @artist_id = (select artist_id from tracks_features where id = @id);
set @artist_name = (select artist_name from tracks_artist where id = @artist_id);

-- 推薦方法 recom_method
-- 推薦排序 recom_rank
-- 分數 score
set @user_id = 'chiouchingyi';
set @recom_method = '0';
set @recom_rank = '1';
set @score = '5';
insert into tracks_recsysresults2 (user_id, album_img_url, track_id, artist_name, recom_method, recom_rank, score) values (@user_id, @album_img_url, @id, @artist_name, @recom_method, @recom_rank, @score);
select * from tracks_recsysresults2;