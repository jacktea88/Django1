使用09chart environment
檔案是由ch09??忘了 copy過來的，逐步修改成有chart的功能
09-vote-utf8.csv是用UTF-8編碼的，可正常顯示中文，但匯入也要用UTF-8
09-vote.csv是用system or BIG5編碼的，無法正常顯示中文
匯出注意：
sqlite studio匯出選項三個都要勾選(default)，分隔符號要用逗號(csv)
匯入注意：
一、匯入時要注意字形編碼，要選和csv檔的一樣，不然會亂碼，匯出也要用和csv檔的一樣
二、也要注意分隔符號要用逗號(csv)，不然匯入時會報錯，資料格式不對，或欄位數不對
三、sqlite studio要用管理員權限開啟，不然無法匯入，顯示read only