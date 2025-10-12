使用121mshop-old environment
檔案是由ch12 copy過來的，用原始requirement-origin.txt驗證功能ok
再用原檔案採用最新python & django版本，再安裝其他新版本套件，測試後沒有問題, 
存成requirements.txt，可用pip install -r requirements.txt安裝套件 
直接用pip install -r requirements.txt安裝套件有個問題是cart套件的問題，
但是要先pip install cart套件，再pip install -r requirements.txt安裝其他套件??
可用cart.zip檔安裝套件(直接解壓縮即可COPY)到C:\Users\USER\anaconda3\envs\(conda env name)\Lib\site-packages