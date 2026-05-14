from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gym.models import (
    CompanyInfo, Trainer, Client, MembershipType, TrainingType,
    Equipment, FAQ, Article, Vacancy
)
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Загрузка тестовых данных для FitLife Gym'

    def handle(self, *args, **kwargs):
        self.stdout.write('Загрузка тестовых данных...')

        # Информация о компании
        if not CompanyInfo.objects.exists():
            CompanyInfo.objects.create(
                name='FitLife Gym',
                history='FitLife Gym - это современный фитнес-центр, основанный в 2015 году. '
                        'Мы предлагаем широкий спектр услуг для достижения ваших фитнес-целей.',
                founding_year=2015,
                address='г. Минск, ул. Победителей, 123',
                phone='+375 29 123-45-67',
                email='info@fitlifegym.by',
                requisites='УНП: 123456789\nР/с: BY12ALFA30120000000000000000\nБанк: ЗАО "Альфа-Банк"'
            )
            self.stdout.write(self.style.SUCCESS('[OK] Информация о компании создана'))

        # Тренеры
        if not Trainer.objects.exists():
            trainers_data = [
                {
                    'first_name': 'Иван',
                    'last_name': 'Петров',
                    'specialization': 'Силовые тренировки',
                    'experience_years': 8,
                    'phone': '+375 29 111-11-11',
                    'email': 'petrov@fitlifegym.by',
                    'bio': 'Мастер спорта по тяжелой атлетике. Специализируюсь на силовых тренировках и бодибилдинге.',
                    'birth_date': date(1990, 5, 15)
                },
                {
                    'first_name': 'Анна',
                    'last_name': 'Сидорова',
                    'specialization': 'Йога и пилатес',
                    'experience_years': 5,
                    'phone': '+375 29 222-22-22',
                    'email': 'sidorova@fitlifegym.by',
                    'bio': 'Сертифицированный инструктор по йоге и пилатесу. Помогу вам обрести гибкость и гармонию.',
                    'birth_date': date(1992, 8, 20)
                },
                {
                    'first_name': 'Дмитрий',
                    'last_name': 'Козлов',
                    'specialization': 'Кардио и функциональный тренинг',
                    'experience_years': 6,
                    'phone': '+375 29 333-33-33',
                    'email': 'kozlov@fitlifegym.by',
                    'bio': 'Специалист по кардио-тренировкам и функциональному тренингу. Помогу вам сжечь калории!',
                    'birth_date': date(1988, 3, 10)
                }
            ]
            for data in trainers_data:
                Trainer.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] Тренеры созданы'))

        # Типы абонементов
        if not MembershipType.objects.exists():
            memberships_data = [
                {
                    'name': 'Базовый',
                    'duration_months': 1,
                    'price': 50.00,
                    'description': 'Доступ в тренажерный зал в любое время',
                    'includes_trainer': False
                },
                {
                    'name': 'Стандарт',
                    'duration_months': 3,
                    'price': 130.00,
                    'description': 'Доступ в тренажерный зал + групповые занятия',
                    'includes_trainer': False
                },
                {
                    'name': 'Премиум',
                    'duration_months': 6,
                    'price': 240.00,
                    'description': 'Полный доступ + 4 персональные тренировки в месяц',
                    'includes_trainer': True
                },
                {
                    'name': 'VIP',
                    'duration_months': 12,
                    'price': 450.00,
                    'description': 'Безлимитный доступ + персональный тренер + массаж',
                    'includes_trainer': True
                }
            ]
            for data in memberships_data:
                MembershipType.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] Типы абонементов созданы'))

        # Типы тренировок
        if not TrainingType.objects.exists():
            trainings_data = [
                {
                    'name': 'Силовая тренировка',
                    'description': 'Тренировка с отягощениями для развития силы и мышечной массы',
                    'duration_minutes': 60,
                    'max_participants': 10,
                    'difficulty_level': 'intermediate'
                },
                {
                    'name': 'Йога для начинающих',
                    'description': 'Базовые асаны и дыхательные практики',
                    'duration_minutes': 90,
                    'max_participants': 15,
                    'difficulty_level': 'beginner'
                },
                {
                    'name': 'HIIT тренировка',
                    'description': 'Высокоинтенсивная интервальная тренировка для сжигания жира',
                    'duration_minutes': 45,
                    'max_participants': 12,
                    'difficulty_level': 'advanced'
                },
                {
                    'name': 'Пилатес',
                    'description': 'Упражнения для укрепления мышц кора и улучшения осанки',
                    'duration_minutes': 60,
                    'max_participants': 12,
                    'difficulty_level': 'beginner'
                },
                {
                    'name': 'Кроссфит',
                    'description': 'Функциональный тренинг высокой интенсивности',
                    'duration_minutes': 60,
                    'max_participants': 8,
                    'difficulty_level': 'advanced'
                }
            ]
            for data in trainings_data:
                TrainingType.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] Типы тренировок созданы'))

        # Оборудование
        if not Equipment.objects.exists():
            equipment_data = [
                {
                    'name': 'Беговая дорожка',
                    'description': 'Профессиональная беговая дорожка с регулировкой наклона',
                    'quantity': 10,
                    'condition': 'excellent',
                    'purchase_date': date(2023, 1, 15)
                },
                {
                    'name': 'Силовая рама',
                    'description': 'Многофункциональная силовая рама для приседаний и жимов',
                    'quantity': 5,
                    'condition': 'good',
                    'purchase_date': date(2022, 6, 10)
                },
                {
                    'name': 'Гантели',
                    'description': 'Набор гантелей от 2 до 50 кг',
                    'quantity': 50,
                    'condition': 'excellent',
                    'purchase_date': date(2023, 3, 20)
                },
                {
                    'name': 'Велотренажер',
                    'description': 'Велотренажер с программами тренировок',
                    'quantity': 8,
                    'condition': 'good',
                    'purchase_date': date(2022, 9, 5)
                }
            ]
            for data in equipment_data:
                Equipment.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] Оборудование создано'))

        # FAQ
        if not FAQ.objects.exists():
            faq_data = [
                {
                    'question': 'Какой абонемент выбрать новичку?',
                    'answer': 'Для начинающих рекомендуем абонемент "Базовый" на 1 месяц. '
                             'Это позволит вам попробовать тренажерный зал и понять, подходит ли он вам.'
                },
                {
                    'question': 'Нужна ли справка от врача?',
                    'answer': 'Справка от врача не обязательна, но мы рекомендуем проконсультироваться '
                             'с врачом перед началом интенсивных тренировок.'
                },
                {
                    'question': 'Можно ли заморозить абонемент?',
                    'answer': 'Да, вы можете заморозить абонемент на срок до 14 дней при наличии '
                             'уважительной причины (болезнь, командировка).'
                },
                {
                    'question': 'Есть ли пробное занятие?',
                    'answer': 'Да, мы предлагаем бесплатное пробное занятие для всех новых клиентов. '
                             'Запишитесь по телефону или через сайт.'
                }
            ]
            for data in faq_data:
                FAQ.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] FAQ создан'))

        # Статьи/Новости
        if not Article.objects.exists():
            admin_user = User.objects.filter(is_superuser=True).first()
            articles_data = [
                {
                    'title': 'Открытие нового зала для групповых занятий',
                    'short_description': 'Мы рады сообщить об открытии нового просторного зала для групповых тренировок',
                    'content': 'С 1 июня в FitLife Gym открывается новый зал площадью 200 кв.м для групповых занятий. '
                              'Здесь будут проходить занятия по йоге, пилатесу, HIIT и другим направлениям. '
                              'Зал оборудован современной звуковой системой и кондиционерами.',
                    'author': admin_user
                },
                {
                    'title': '5 советов для эффективной тренировки',
                    'short_description': 'Как сделать ваши тренировки максимально эффективными',
                    'content': '1. Разминка обязательна\n2. Следите за техникой выполнения\n'
                              '3. Пейте достаточно воды\n4. Не забывайте про отдых\n5. Правильное питание',
                    'author': admin_user
                },
                {
                    'title': 'Новые тренеры в нашей команде',
                    'short_description': 'Познакомьтесь с нашими новыми специалистами',
                    'content': 'Мы рады представить двух новых тренеров, которые присоединились к команде FitLife Gym. '
                              'Они помогут вам достичь ваших фитнес-целей!',
                    'author': admin_user
                }
            ]
            for data in articles_data:
                Article.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] Статьи созданы'))

        # Вакансии
        if not Vacancy.objects.exists():
            vacancies_data = [
                {
                    'title': 'Тренер по фитнесу',
                    'description': 'Ищем опытного тренера для проведения групповых и персональных тренировок',
                    'requirements': '- Опыт работы от 2 лет\n- Сертификат тренера\n- Коммуникабельность',
                    'salary': 800.00,
                    'is_active': True
                },
                {
                    'title': 'Администратор',
                    'description': 'Требуется администратор на ресепшн',
                    'requirements': '- Опыт работы с клиентами\n- Знание ПК\n- Ответственность',
                    'salary': 600.00,
                    'is_active': True
                }
            ]
            for data in vacancies_data:
                Vacancy.objects.create(**data)
            self.stdout.write(self.style.SUCCESS('[OK] Вакансии созданы'))

        self.stdout.write(self.style.SUCCESS('\n[SUCCESS] Все тестовые данные успешно загружены!'))
        self.stdout.write(self.style.WARNING('\nДля входа в админ-панель используйте:'))
        self.stdout.write('Username: admin')
        self.stdout.write('Password: admin (установите пароль командой: python manage.py changepassword admin)')
