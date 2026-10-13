from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch
from kivymd.uix.screen import MDScreen
from kivymd.uix.slider import MDSlider, MDSliderHandle
from kivymd.uix.tab import (
    MDTabsCarousel,
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsPrimary,
)
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText


class SchoolToolsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        root = MDScreen()
        layout = MDBoxLayout(orientation="vertical")
        tabs = MDTabsPrimary(
            MDDivider(),
            MDTabsCarousel(
                id="pages",
                size_hint_y=1,
            ),
            id="tabs",
            size_hint=(1, 1),
        )
        layout.add_widget(tabs)
        root.add_widget(layout)
        return root

    def on_start(self):
        tabs = self.root.ids.tabs
        pages = self.root.ids.pages

        tabs.add_widget(
            MDTabsItem(
                MDTabsItemIcon(icon="home-outline"),
                MDTabsItemText(text="Приветствие"),
            )
        )
        pages.add_widget(self.make_welcome_page())

        tabs.add_widget(
            MDTabsItem(
                MDTabsItemIcon(icon="widgets-outline"),
                MDTabsItemText(text="Material 3"),
            )
        )
        pages.add_widget(self.make_components_page())

    def make_page(self):
        screen = MDScreen()
        scroll = ScrollView()
        content = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(16),
            size_hint_y=None,
        )
        content.bind(minimum_height=content.setter("height"))
        scroll.add_widget(content)
        screen.add_widget(scroll)
        return screen, content

    def make_welcome_page(self):
        screen, content = self.make_page()
        self.welcome_message = MDLabel(
            text="Привет! Это твоё первое приложение.",
            halign="center",
            size_hint_y=None,
            height=dp(100),
        )
        self.tap_count = 0

        button = MDButton(
            MDButtonText(text="Нажми меня"),
            style="filled",
            pos_hint={"center_x": 0.5},
            on_release=self.on_welcome_button,
        )
        content.add_widget(
            MDLabel(
                text="Добро пожаловать в SchoolTools",
                role="headline",
                size_hint_y=None,
                height=dp(64),
            )
        )
        content.add_widget(self.welcome_message)
        content.add_widget(button)
        return screen

    def on_welcome_button(self, *_args):
        self.tap_count += 1
        self.welcome_message.text = f"Кнопка нажата {self.tap_count} раз"

    def make_components_page(self):
        screen, content = self.make_page()
        content.add_widget(
            MDLabel(
                text="Основные компоненты Material 3",
                role="headline",
                size_hint_y=None,
                height=dp(64),
            )
        )

        content.add_widget(self.section_title("Кнопки"))
        for style in ("elevated", "filled", "tonal", "outlined", "text"):
            content.add_widget(
                MDButton(
                    MDButtonText(text=style.capitalize()),
                    style=style,
                    pos_hint={"center_x": 0.5},
                )
            )

        content.add_widget(self.section_title("Поле ввода"))
        content.add_widget(
            MDTextField(
                MDTextFieldHintText(text="Напиши что-нибудь"),
                mode="outlined",
                size_hint_y=None,
                height=dp(64),
            )
        )

        content.add_widget(self.section_title("Карточка"))
        content.add_widget(
            MDCard(
                MDLabel(
                    text="Карточка Material 3",
                    halign="center",
                ),
                style="elevated",
                padding=dp(20),
                size_hint_y=None,
                height=dp(96),
            )
        )

        content.add_widget(self.section_title("Чип"))
        content.add_widget(
            MDChip(
                MDChipText(text="Пример чипа"),
                pos_hint={"center_x": 0.5},
            )
        )

        content.add_widget(self.section_title("Переключатели"))
        for label, control, width in (
            ("Флажок", MDCheckbox(), dp(48)),
            ("Переключатель", MDSwitch(), dp(64)),
        ):
            row = MDBoxLayout(
                orientation="horizontal",
                spacing=dp(12),
                size_hint_y=None,
                height=dp(48),
            )
            row.add_widget(MDLabel(text=label))
            control.size_hint_x = None
            control.width = width
            row.add_widget(control)
            content.add_widget(row)

        content.add_widget(self.section_title("Слайдер"))
        content.add_widget(
            MDSlider(
                MDSliderHandle(),
                min=0,
                max=100,
                step=10,
                value=40,
            )
        )
        return screen

    @staticmethod
    def section_title(text):
        return MDLabel(
            text=text,
            role="title",
            size_hint_y=None,
            height=dp(40),
        )


if __name__ == "__main__":
    SchoolToolsApp().run()
