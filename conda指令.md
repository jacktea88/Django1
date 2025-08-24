指令	說明
conda env list 或 conda info --envs	列出所有已安裝的環境。
conda create --name <env_name>	建立一個新的環境，不指定 Python 版本。
例：conda create --name 12mshop python
conda create --name <env_name> python=<version>	建立一個指定 Python 版本的環境。
conda activate <env_name>	啟用指定的環境。
conda deactivate	關閉目前的環境。
conda env remove --name <env_name>	移除指定的環境。
conda create --name <new_env> --clone <old_env>	複製一個現有的環境。
conda update --all	更新目前環境中的所有套件。

套件管理

指令	說明
conda list	列出目前環境中所有已安裝的套件。
conda search <package_name>	搜尋 Conda 儲存庫中的套件。
conda install <package_name>	安裝套件到目前環境。
conda install <package_name>=<version>	安裝指定版本的套件。
conda install --name <env_name> <package_name>	安裝套件到指定的環境。
conda update <package_name>	更新指定的套件。
conda remove <package_name>	移除指定的套件。
conda clean --all	清理快取檔案以釋放空間。

環境匯出與分享

指令	說明
conda env export > environment.yml	將目前環境的套件列表匯出為 YAML 檔案。
conda env create -f environment.yml	從 YAML 檔案建立一個新的環境。