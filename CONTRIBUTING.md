# Contributing to Hunt for your Python Job

歡迎提出 Issues and PRs！


# Write Commit message properly

請有結構的撰寫 Commit message，並且遵守 [Angular JS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.greljkmo14y0) 規範。

中文內容部分翻譯來自 : [WadeHuang 的學習迷航記](https://wadehuanglearning.blogspot.com/2019/05/commit-commit-commit-why-what-commit.html)

- ```<feat>``` : 新增 / 修改功能 (feature)。
- ```<fix>``` : 修補 bug (bug fix)。
- ```<docs>``` : 文件 (documentation)。
- ```<style>``` : 格式 (不影響程式碼運行的變動 white-space, formatting, missing semi-colons, etc)。
- ```<refactor>``` : 重構 (既不是新增功能，也不是修補 bug 的程式碼變動)。
- ```<perf>``` : 改善效能 (A code change that improves performance)。
- ```<test>``` : 增加測試 (when adding missing tests)。
- ```<chore>``` : 建構程序或輔助工具的變動 (maintain)。
- ```<revert>``` : 撤銷回覆先前的 commit 例如：revert: type (scope): subject (回覆版本：xxxx)。


## 一個良好的 commit message 應該要有以下幾個部分：

###  Header: 
```type + scope: subject```
 - type: 代表 commit 的類別：feat, fix, docs, style, refactor, test, chore，必要欄位。
 - scope 代表 commit 影響的範圍，例如資料庫、控制層、模板層等等，視專案不同而不同，為可選欄位。
 - subject 代表此 commit 的簡短描述，不要超過 50 個字元，結尾不要加句號，為必要欄位。

```Body: 72-character wrapped. This should answer:```
 * Body 部份是對本次 Commit 的詳細描述，可以分成多行，每一行不要超過 72 個字元。
 * 說明程式碼變動的項目與原因，還有與先前行為的對比。

```Footer: ```
 - 填寫任務編號（如果有的話）.
 - BREAKING CHANGE（可忽略），記錄不兼容的變動，
   以 BREAKING CHANGE: 開頭，後面是對變動的描述、以及變動原因和遷移方法。


## 前端開發環境與步驟

- 目前因為使用的是 vite3，所以需要 nodejs 14.18+ or 16+ 以上
- 如果你目前沒有 nodejs 版本的話，可以使用 nvm 來安裝 nodejs 來管理 nodejs 版本
- 詳見 Titangene 的[文章](https://titangene.github.io/article/nvm.html)

### 安裝相關套件

```bash
# 如果你是第一次使用，請先安裝相關套件

cd job-platform/frontend # 切換到前端資料夾
npm install # 安裝相關套件，如果你是使用 yarn，請使用 yarn install
npm run dev # 開發模式

```
### 如果成功的話，你會看到以下畫面
```bash
> hoobank@0.0.0 dev
> vite

  VITE v3.0.2  ready in * ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: http://192.168.84.14:5173/
  ➜  Network: http://172.21.0.1:5173/
  ➜  Network: http://100.98.138.12:5173/
```
## 後端開發步驟

### 安裝相關套件
  
```bash
# 如果你是第一次使用，請先安裝相關套件
# 建議使用虛擬環境來安裝相關套件

cd job-platform/backend # 切換到後端資料夾
pip install -r requirements.txt # 安裝相關套件
uvicorn main:app --host=0.0.0.0 --port=8000 --reload # 開發模式
```
#### Swagger API 文件
[http://localhost:8000/docs#/](http://localhost:8000/docs#/)

## Spider 開發步驟
### TBD 

## Airflow 開發步驟
### TBD
  
# Roadmap of Hunt for your Python Job

### 目前在著手的部分
- [ ] 創建 Discord 推播系統
- [ ] 前端介面優化
- [ ] 增加 [104人力銀行](https://www.104.com.tw/jobs/main/) 和 [Meet.jobs](https://meet.jobs/zh-TW) 求職網站的爬蟲

### 未來想發展的功能
- [ ] 利用 ML 去預測職缺的薪水，並分析職缺薪水走勢
- [ ] 職缺比較功能
- [ ] 統計職缺技能 Dashboard


### 歡迎所有人來參與開發，若有任何問題歡迎來信或是在 issue 提出
> E-mail: zxc123benny14159@gmail.com
