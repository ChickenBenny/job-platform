# Job platform
### Hunt for your Python Job
這是一個針對 Python 語言所開發的整合求職平台，整合了 [Cakeresume](https://www.cakeresume.com) 和 [Yourator](https://www.yourator.co/) 等求職網站，並且每日會去各大求職網站爬取最新的資料，讓你找工作輕鬆自在，不必在各大平台流浪。

**服務架設網址 :** https://chickenbenny.com

### 網站功能
- [x] 跨平台整合求職資訊
- [x] 建立爬蟲 pipeline，每日定期爬取資料
- [x] 點擊職缺公司名稱能轉跳到原始的求職網站刊登資訊

### 幫忙點個讚~
若大家喜歡可以幫我點個星星，我會持續更新網站功能，並美化網站頁面。

### 目前在著手的部分
- [ ] 創建 Discord 推播系統
- [ ] 前端介面優化
- [ ] 增加 [104人力銀行](https://www.104.com.tw/jobs/main/) 和 [Meet.jobs](https://meet.jobs/zh-TW) 求職網站的爬蟲

### 未來想發展的功能
- [ ] 利用 ML 去預測職缺的薪水，並分析職缺薪水走勢
- [ ] 職缺比較功能
- [ ] 統計職缺技能 Dashboard

### 架設自己的server
1. Clone the repo and go into the folder.
```
$ git clone https://github.com/ChickenBenny/job-platform.git
```
2. Go to the `.env` file and type in the `user`,`password` and `schema`.
3. Use docker compose build the frontend, backend and nginx.
```
$ docker-compose up
```
4. Go into the airflow folder and use docker compose build the airflow server
```
$ cd airflow
$ docker-compose up
```
5. Build the connection with airflow server and job_database, and remember to change the db information.
```
$ docker exec -it webserver airflow connections add 'job_database' --conn-type 'postgres' --conn-login `${user}` --conn-password `${password}` --conn-host `{ip or host.docker.internal}` --conn-port '5432' --conn-schema ${schema}
```

### 開發手冊（for contributor)
- 歡迎所有人來參與開發，若有任何問題歡迎來信或是在 issue 提出
    - E-mail: zxc123benny14159@gmail.com
- 開發手冊
    - TBD
---

![](https://i.imgur.com/29V1E2p.png)
