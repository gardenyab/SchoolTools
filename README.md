# SchoolTools

Стартовый проект Android-приложения на Python с Kivy и KivyMD 2 (Material Design 3). В приложении есть вкладка приветствия и вкладка с примерами основных компонентов Material 3.

## Что понадобится

- Windows 10/11 с включённым WSL2 и Ubuntu. Buildozer собирает Android-приложение в Linux; не запускайте сборку из обычного Windows PowerShell.
- Python 3 и Java 17 в Ubuntu.
- Интернет и несколько гигабайт свободного места для Android SDK/NDK, которые Buildozer скачает при первой сборке.

Храните проект в файловой системе Ubuntu, например `~/projects/SchoolTools`, а не в `/mnt/c`, чтобы сборка работала быстрее и надёжнее. Из Ubuntu папка Windows доступна в `/mnt/c/Projects/SchoolTools`.

## Установка инструментов в Ubuntu

```bash
sudo apt update
sudo apt install -y \
  python3 python3-pip python3-venv git zip unzip \
  openjdk-17-jdk build-essential autoconf libtool pkg-config \
  zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo6 \
  cmake libffi-dev libssl-dev
```

Перейдите в копию проекта в Ubuntu и установите Buildozer в виртуальное окружение:

```bash
mkdir -p ~/projects/SchoolTools
cp /mnt/c/Projects/SchoolTools/{main.py,buildozer.spec,README.md,.gitignore} ~/projects/SchoolTools/
cd ~/projects/SchoolTools
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install buildozer cython
```

## Сборка APK

Из папки проекта и с активированным виртуальным окружением выполните:

```bash
buildozer -v android debug
```

При первой сборке Buildozer загрузит Android SDK и NDK. Готовый APK появится в папке `bin/`. Чтобы установить его на подключённый Android-телефон с включённой USB-отладкой, можно выполнить:

```bash
buildozer android deploy run
```

Имя приложения, пакет, версия и Android-настройки находятся в `buildozer.spec`. В зависимостях закреплён `kivymd==2.0.0`, версия с Material Design 3 API.

Если проект уже копировали в Ubuntu, после изменений в Windows обновите исходные файлы в WSL:

```bash
cp /mnt/c/Projects/SchoolTools/{main.py,buildozer.spec,README.md} ~/projects/SchoolTools/
cd ~/projects/SchoolTools
source .venv/bin/activate
```

После этого запустите команду сборки из раздела выше. Если APK уже был собран, Buildozer пересоберёт его с обновлённым кодом.

## Запуск на компьютере (необязательно)

Для запуска на компьютере установите Kivy и ту же версию KivyMD в активированное виртуальное окружение:

```bash
python -m pip install kivy kivymd==2.0.0
python main.py
```
