import os
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SubwayPatcher(App):
    def build(self):
        self.title = "JORDAN PATCHER v1"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # UI Styling
        self.status = Label(text="READY TO INJECT", color=(0, 0.5, 1, 1), font_size='20sp')
        layout.add_widget(self.status)

        patch_btn = Button(
            text="MAX COINS & KEYS", 
            background_color=(0, 0.5, 1, 1),
            font_size='18sp',
            bold=True
        )
        patch_btn.bind(on_press=self.apply_hack)
        layout.add_widget(patch_btn)

        return layout

    def apply_hack(self, instance):
        # The secret path to Subway Surfers data on Android
        path = "/sdcard/Android/data/com.kiloo.subwaysurf/files/profile/wallet.json"
        
        if not os.path.exists(path):
            self.status.text = "ERROR: GAME NOT FOUND"
            return

        try:
            # 1. Read the current file
            with open(path, 'r') as f:
                data = json.load(f)

            # 2. Inject the 999 Million values
            # Currency 1 = Coins, 2 = Keys
            for item in data.get('currencies', {}).values():
                item['amount'] = 999999999

            # 3. Save the modded file
            with open(path, 'w') as f:
                json.dump(data, f)

            self.status.text = "HACK SUCCESSFUL! RESTART GAME"
            self.status.color = (0, 1, 0, 1) # Green
        except Exception as e:
            self.status.text = "PATCH FAILED: ACCESS DENIED"

if __name__ == '__main__':
    SubwayPatcher().run()