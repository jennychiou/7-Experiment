# cl.lyrics

### Dependencies
Python3, Scrapy

### Clone
```
git clone ./lyricsCrawl/spiders/.env
```

### Install Requirement
```
pip install -r requirements.txt
```

### Configure Setting : 
Edit the file `./lyricsCrawl/spiders/.env.example`, save as `./lyricsCrawl/spiders/.env`.
```
cp ./lyricsCrawl/spiders/.env.example ./lyricsCrawl/spiders/.env
vim ./lyricsCrawl/spiders/.env
```
For example:
* Connect every singer with '`,`', do not use `' '`(sapce).
```
# .env
singers = troye sivan,lauv,birdy
``` 

### Run
```
scrapy crawl metrolyrics -o ./datasets/mydata_name.csv
```

### Results
Output file : at [datasets](./datasets/) dir.
