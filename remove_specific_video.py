import os

def remove_video_file_from_directories(directories, file_prefix):
    """
    從多個指定的資料夾中移除以特定前綴開頭的影片檔案。
    
    :param directories: 資料夾路徑的列表
    :param file_prefix: 要移除的影片檔案名稱的前兩或前三個字母
    """
    for directory in directories:
        # 確保目錄存在
        if not os.path.isdir(directory):
            print(f"目錄 '{directory}' 不存在。")
            continue

        # 列出目錄中的所有檔案
        files = os.listdir(directory)
        
        # 過濾出符合前綴的檔案
        target_files = [file for file in files if file.startswith(file_prefix)]
        
        # 移除符合前綴的檔案
        for file in target_files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"檔案 '{file_path}' 已成功移除。")
                except Exception as e:
                    print(f"移除檔案 '{file_path}' 時發生錯誤: {e}")

if __name__ == "__main__":
    # 設定固定的資料夾路徑列表
    current_directory = os.getcwd()
    directories = [os.path.join(current_directory, f"{i}{sign}") for i in range(7) for sign in ("+", "-")]
    
    # 輸入要移除的影片檔案名稱的前兩或前三個字母
    file_prefix = input("請輸入要移除的影片檔案名稱的前兩或前三個字母: ")
    
    # 移除指定資料夾中的影片檔案
    remove_video_file_from_directories(directories, file_prefix)
