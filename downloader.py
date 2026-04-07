import requests  
from threading import Thread  
import os  

class NovelDownloader:  
    def __init__(self, base_url):  
        self.base_url = base_url  
        self.progress_callback = None  

    def set_progress_callback(self, callback):  
        self.progress_callback = callback  

    def get_download_url(self, chapter_id):  
        return f"{self.base_url}/chapter/{chapter_id}"  

    def get_chapter_content(self, chapter_id):  
        try:  
            url = self.get_download_url(chapter_id)  
            response = requests.get(url)  
            response.raise_for_status()  
            return response.text  
        except requests.exceptions.RequestException as e:  
            print(f"Error fetching chapter {chapter_id}: {e}")  
            return None  

    def write_to_file(self, chapter_id, content):  
        try:  
            with open(f"chapter_{chapter_id}.txt", 'w', encoding='utf-8') as file:  
                file.write(content)  
        except Exception as e:  
            print(f"Error writing chapter {chapter_id} to file: {e}")  

    def download_novel(self, chapter_ids):  
        threads = []  
        for chapter_id in chapter_ids:  
            thread = Thread(target=self.download_chapter, args=(chapter_id,))  
            threads.append(thread)  
            thread.start()  
        for thread in threads:  
            thread.join()  

    def download_chapter(self, chapter_id):  
        content = self.get_chapter_content(chapter_id)  
        if content:  
            self.write_to_file(chapter_id, content)  
            if self.progress_callback:  
                self.progress_callback(chapter_id)  

    def download_in_background(self, chapter_ids):  
        Thread(target=self.download_novel, args=(chapter_ids,)).start()  

# Usage example:  
# downloader = NovelDownloader('https://biqukan.com')  
# downloader.set_progress_callback(lambda chapter_id: print(f"Downloaded chapter {chapter_id}"))  
# downloader.download_in_background([1, 2, 3])  
