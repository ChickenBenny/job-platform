# Job platform
### Hunt for your Python Job
這是一個針對 Python 語言所開發的整合求職平台，整合了Cakeresume和yourator等求職網站，並且每日會去各大求職網站爬取最新的資料，讓你找工作輕鬆自在，不必在各大平台流浪。

**服務架設網址 :** https://chickenbenny.com

### 網站功能
* 跨平台整合求職資訊
* 建立爬蟲pipline，每日定期爬取資料
* 點擊職缺公司名稱能轉跳到原始的求職網站刊登資訊

### 幫忙點個讚~
目前此網站是架在我實驗室的電腦上，網站十分的陽春。若大家喜歡可以幫我點個星星，我會持續更新網站功能，並美化網站頁面。

### 目前在著手的部分
* 新增104網站爬蟲api
* 創建Discrod推播系統
* 前端介面優化

### 未來想發展的功能
* 利用 ML 去預測職缺的薪水，並分析職缺薪水走勢
* 創建 Discrod 頻道，若有新的求職資訊，並會進行推播
* 優化網頁頁面，並架設 Nginx 優化網頁效能

### 快速開始(架設自己的server)
1. Clone the repository
```
$ git clone https://github.com/ChickenBenny/job-platform
$ cd job-platform
```
2. Use docker-compose up to build the server
```
$ docker-compose up --build
```
3. build the airflow server
```
$ cd airflow
$ docker-compose up
$ docker exec -it webserver airflow connections add 'job_database' --conn-type 'postgres' --conn-login '' --conn-password '' --conn-host 'job_database' --conn-port '5432' --conn-schema ''
```
### 開發手冊（for contribuer)
- 歡迎所有人來參與開發，若有任何問題歡迎來信或是在 issue 提出
    - E-mail: zxc123benny14159@gmail.com
- 開發手冊
    - https://hackmd.io/@nerohin/python-job-platform
---

![](https://i.imgur.com/29V1E2p.png)