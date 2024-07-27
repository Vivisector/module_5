from sys import exit
from time import sleep
import hashlib


class User:
    def __init__(self, nickname, password_hash, age):
        self.nickname = nickname
        self.password_hash = password_hash
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []

    def __init__(self, current_user=None):
        self.current_user = current_user

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, nickname, password):
        password_hash = self.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password_hash == password_hash:
                self.current_user = user
                print(f'Пользователь {user.nickname} успешно вошел в систему')
                return True
        print('Неверный логин или пароль')
        return False

    def register(self, nickname, password, age):
        if not any(user.nickname == nickname for user in self.users):
            password_hash = self.hash_password(password)
            new_user = User(nickname, password_hash, age)
            self.users.append(new_user)
            print(f'Пользователь {nickname} ({new_user.age} лет) успешно зарегистрирован')
        else:
            print(f'Пользователь с никнеймом "{nickname}" уже существует')

    def logout(self):
        if self.current_user:
            print(f'{self.current_user.nickname} вышел из системы')
            current_user = None
        else:
            print('Нет текущего пользователя для выхода')

    def add(self, *videonames):
        for videoname in videonames:
            if videoname not in self.videos:
                self.videos.append(videoname)
                print(f'Добавили видео "{videoname.title}"')
            else:
                print(f'Видео с названием {videoname.title} уже есть. Придумайте другое название')

    def get_videos(self, keyword):
        found_videos = [video for video in self.videos if keyword.lower() in video.title.lower()]
        if found_videos:
            result = "\n".join(video.title for video in found_videos)
            # for video in found_videos:
            #     print(video.title)
        else:
            result = f'Видео с ключевым словом "{keyword}" не найдено'

        return result

    def watch_video(self, videoname):
        if self.current_user:
            # print(self.current_user)
            video = None
            for vid in self.videos:
                if vid.title == videoname:
                    video = vid
                    break
            # video = next((video for video in self.videos if video.title == videoname), None)
            if video:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам еще нет 18 лет, пожалуйста покиньте страницу\n')
                else:
                    for t in range(video.time_now, video.duration):
                        print(
                            f'Просмотр "{video.title}" пользователем {self.current_user.nickname} ведется на {t} секунде')
                        sleep(1)
                    if video.time_now == video.duration:
                        video.time_now = 0
                    print(f'{self.current_user.nickname} просмотрел "{video.title}" до конца\n')
            else:
                print(f'Видео с названием "{videoname}" не существует')
        else:
            print(f'Войдите в аккаунт, чтобы смотреть видео "{videoname}"')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года!', 20)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)

# Добавление видео
print('\n--- Добавление видео ---')
ur.add(v1, v2)

# Проверка поиска
print('\n--- Проверка поиска ---')
print('Видео по слову "test":')
print(ur.get_videos('test'))
print('Видео по слову "лучший":')
print(ur.get_videos('лучший'))
print('Видео по слову "ПРОГ":')
print(ur.get_videos('ПРОГ'))

# exit()
# Проверка на вход пользователя и возрастное ограничение
print('\n--- Попытка просмотра вне логина ---')
ur.watch_video('Для чего девушкам парень программист?')

# Регистрация пользователей
print('\n--- Регистрация пользователей ---')
ur.register('Peter', 'password123', 20)
ur.register('vasya_pupkin', 'pass12345', 13)
ur.register('urban_pythonist', 'password54321', 25)

# Попытка входа и просмотра видео
print('\n--- Проверка на вход и возраст ---')
ur.login('Peter', 'password123')
ur.watch_video('Для чего девушкам парень программист?')

ur.login('vasya_pupkin', 'pass12345')
ur.watch_video('Для чего девушкам парень программист?')

ur.login('urban_pythonist', 'password54321')
ur.watch_video('Для чего девушкам парень программист?')

print('\n--- Попытка регистрации по занятому нику ---')
ur.register('vasya_pupkin', 'password123456789', 55)

# Попытка воспроизведения несуществующего видео
print('\n--- Попытка воспроизведения несуществующего видео ---')
ur.watch_video('Самый наилучший язык программирувания')
