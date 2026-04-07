from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class BiqukanDownloaderUI(BoxLayout):
    def __init__(self, **kwargs):
        super(BiqukanDownloaderUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Enter Novel URL:')
        self.add_widget(self.label)

        self.url_input = TextInput(hint_text='Novel URL', multiline=False)
        self.add_widget(self.url_input)

        self.download_button = Button(text='Download Novel')
        self.download_button.bind(on_press=self.download_novel)
        self.add_widget(self.download_button)

    def download_novel(self, instance):
        url = self.url_input.text
        if url:
            # Implement your downloader logic here
            print(f'Downloading novel from {url}')
        else:
            print('No URL provided')

class BiqukanDownloaderApp(App):
    def build(self):
        return BiqukanDownloaderUI()

if __name__ == '__main__':
    BiqukanDownloaderApp().run()