<<<<<<< HEAD
import speech_recognition as sr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from threading import Thread
from kivy.core.window import Window

# Configure the window to allow transparency and overlay
Window.clearcolor = (0, 0, 0, 0)  # Set the background color to transparent
Window.borderless = True          # Remove window borders for overlay effect


class SpeechToTextApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Set a semi-transparent background for the app layout
        self.opacity = 0.8

        self.text_display = TextInput(
            multiline=True,
            readonly=True,
            font_size=18,
            size_hint=(1, 0.8),
            background_color=(0, 0, 0, 0.5),  # Semi-transparent background
            foreground_color=(1, 1, 1, 1),   # White text
        )
        self.add_widget(self.text_display)

        self.start_button = Button(
            text="Start Listening",
            size_hint=(1, 0.1),
            font_size=14,
            background_color=(0, 0.5, 0.5, 0.8),  # Semi-transparent button background
            on_press=self.start_listening
        )
        self.add_widget(self.start_button)

        self.stop_button = Button(
            text="Stop Listening",
            size_hint=(1, 0.1),
            font_size=14,
            background_color=(0.5, 0, 0, 0.8),  # Semi-transparent button background
            on_press=self.stop_listening,
            disabled=True
        )
        self.add_widget(self.stop_button)

        self.recognizer = sr.Recognizer()
        self.running = False

    def start_listening(self, instance):
        """Start listening to microphone input in a separate thread."""
        if not self.running:
            self.running = True
            self.start_button.disabled = True
            self.stop_button.disabled = False
            thread = Thread(target=self.listen_and_display)
            thread.daemon = True
            thread.start()

    def listen_and_display(self):
        """Continuously listen and process speech."""
        with sr.Microphone() as source:
            # Dynamically adjust for ambient noise
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            self.text_display.text = ""  # Clear the display at the start

            while self.running:
                try:
                    # Listen for speech until a pause is detected
                    audio = self.recognizer.listen(source, timeout=None)
                    
                    # Recognize speech using Google Speech Recognition
                    text = self.recognizer.recognize_google(audio)
                    self.update_display(text)

                except sr.UnknownValueError:
                    self.update_display("...")
                except sr.RequestError as e:
                    self.update_display(f"Error: {e}")
                except Exception as e:
                    self.update_display(f"Error: {str(e)}")
                    self.running = False  # Stop listening on exception

    def update_display(self, text):
        """Schedule the text update on the main thread."""
        Clock.schedule_once(lambda dt: self._update_display_main_thread(text))

    def _update_display_main_thread(self, text):
        """Perform the actual UI update on the main thread."""
        self.text_display.text += text + " "
        self.text_display.cursor = (len(self.text_display.text), 0)  # Scroll to the end

    def stop_listening(self, instance):
        """Stop listening for speech."""
        self.running = False
        self.start_button.disabled = False
        self.stop_button.disabled = True


class SpeechToTextAppMain(App):
    def build(self):
        # Resize the window to a smaller overlay size
        Window.size = (300, 200)  # Set the window size for the overlay
        Window.top = 50          # Adjust vertical position of the overlay
        Window.left = 50         # Adjust horizontal position of the overlay
        return SpeechToTextApp()


if __name__ == "__main__":
    SpeechToTextAppMain().run()
=======
import speech_recognition as sr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from threading import Thread
from kivy.core.window import Window

# Configure the window to allow transparency and overlay
Window.clearcolor = (0, 0, 0, 0)  # Set the background color to transparent
Window.borderless = True          # Remove window borders for overlay effect


class SpeechToTextApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Set a semi-transparent background for the app layout
        self.opacity = 0.8

        self.text_display = TextInput(
            multiline=True,
            readonly=True,
            font_size=18,
            size_hint=(1, 0.8),
            background_color=(0, 0, 0, 0.5),  # Semi-transparent background
            foreground_color=(1, 1, 1, 1),   # White text
        )
        self.add_widget(self.text_display)

        self.start_button = Button(
            text="Start Listening",
            size_hint=(1, 0.1),
            font_size=14,
            background_color=(0, 0.5, 0.5, 0.8),  # Semi-transparent button background
            on_press=self.start_listening
        )
        self.add_widget(self.start_button)

        self.stop_button = Button(
            text="Stop Listening",
            size_hint=(1, 0.1),
            font_size=14,
            background_color=(0.5, 0, 0, 0.8),  # Semi-transparent button background
            on_press=self.stop_listening,
            disabled=True
        )
        self.add_widget(self.stop_button)

        self.recognizer = sr.Recognizer()
        self.running = False

    def start_listening(self, instance):
        """Start listening to microphone input in a separate thread."""
        if not self.running:
            self.running = True
            self.start_button.disabled = True
            self.stop_button.disabled = False
            thread = Thread(target=self.listen_and_display)
            thread.daemon = True
            thread.start()

    def listen_and_display(self):
        """Continuously listen and process speech."""
        with sr.Microphone() as source:
            # Dynamically adjust for ambient noise
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            self.text_display.text = ""  # Clear the display at the start

            while self.running:
                try:
                    # Listen for speech until a pause is detected
                    audio = self.recognizer.listen(source, timeout=None)
                    
                    # Recognize speech using Google Speech Recognition
                    text = self.recognizer.recognize_google(audio)
                    self.update_display(text)

                except sr.UnknownValueError:
                    self.update_display("...")
                except sr.RequestError as e:
                    self.update_display(f"Error: {e}")
                except Exception as e:
                    self.update_display(f"Error: {str(e)}")
                    self.running = False  # Stop listening on exception

    def update_display(self, text):
        """Schedule the text update on the main thread."""
        Clock.schedule_once(lambda dt: self._update_display_main_thread(text))

    def _update_display_main_thread(self, text):
        """Perform the actual UI update on the main thread."""
        self.text_display.text += text + " "
        self.text_display.cursor = (len(self.text_display.text), 0)  # Scroll to the end

    def stop_listening(self, instance):
        """Stop listening for speech."""
        self.running = False
        self.start_button.disabled = False
        self.stop_button.disabled = True


class SpeechToTextAppMain(App):
    def build(self):
        # Resize the window to a smaller overlay size
        Window.size = (300, 200)  # Set the window size for the overlay
        Window.top = 50          # Adjust vertical position of the overlay
        Window.left = 50         # Adjust horizontal position of the overlay
        return SpeechToTextApp()


if __name__ == "__main__":
    SpeechToTextAppMain().run()
>>>>>>> a339932 (Initial commit)
