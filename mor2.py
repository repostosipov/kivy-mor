
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, ThreeLineListItem, ThreeLineAvatarListItem
from kivy.core.window import Window
from kivymd.uix.list import ImageLeftWidget

import requests


r = requests.get('https://moryak.site/api/adverts/')
data_vak = r.json()

r = requests.get('https://moryak.site/api/companys/')
data_company = r.json()

Window.size = (500,800)

KV = '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightblue"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Вакансии'
            icon: 'ship-wheel'

            MDScrollView:
                MDList:
                    id: container


        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Компании'
            icon: 'domain'

            MDScrollView:
                MDList:
                    id: container2

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Флот'
            icon: 'ferry'

            MDLabel:
                text: 'Флот'
                halign: 'center'
'''

class Test(MDApp):

    def build(self):
        self.title = 'Моряк Инфо'
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        '''СЛАВА'''
        # for item in data_vak:
        #     self.root.ids.container.add_widget(
        #         ThreeLineAvatarListItem(
        #             text=f"{item['name']}",
        #             secondary_text=f"Должность: {item['position']}",
        #             tertiary_text= f"{item['salary']} ₽",
        #         )
        #     )
        for item in data_vak:
            items = ThreeLineAvatarListItem(
                                text=f"{item['name']}",
                                secondary_text=f"Должность: {item['position']}",
                                tertiary_text= f"{item['salary']} ₽",
                            )
            image = ImageLeftWidget(source='logo.png')
            items.add_widget(image)
            self.root.ids.container.add_widget(items)


        for item in data_company:
            self.root.ids.container2.add_widget(
                ThreeLineAvatarListItem(
                    text=f"{item['name']}",
                    secondary_text=f"Телефон: {item['tel']}",
                    tertiary_text= f"{item['des']}",
                )
            )

Test().run()