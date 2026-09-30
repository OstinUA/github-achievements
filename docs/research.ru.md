# Исследование достижений GitHub

[Каталог на русском](../catalog/russian.md) · [English research](research.en.md)

Проверено **30 сентября 2026 года**. В каталоге **14 публично известных типов достижений**: 7 доступных, 2 исторических, 2 экспериментальных и 3 внутренних. Ещё 7 записей описывают отметки профиля Highlights. Уровни, оттенки кожи и прежние названия не увеличивают эти числа.

## Что именно удалось установить

GitHub не даёт полного официального перечня условий. В [объявлении 2022 года](https://github.blog/news-insights/product-news/introducing-achievements-recognizing-the-many-stages-of-a-developers-coding-journey/) компания предлагает узнавать условия из карточек. Поэтому каталог различает официальные публикации, реально выданные награды и наблюдения сообщества. Это максимально полный результат по найденным публичным свидетельствам; доступа ко всем закрытым экспериментам GitHub нет.

Проверены исходный репозиторий и его переводы, GitHub Docs, публикации и changelog GitHub, сообщения сотрудников в Community, карточки профилей и [общественный архив](https://github.com/Schweinepriester/github-profile-achievements). Дополнительных подтверждённых типов сверх перечисленных 14 не обнаружено. Имя или картинка в стороннем списке само по себе не доказывает существование награды.

<a id="proxima"></a>
## Почему у JakubOleksy необычные награды

Его [публичный профиль](https://github.com/JakubOleksy) указывает работу в GitHub. Карточки подтверждают конкретные события:

| Награда | Надпись карточки | За что выдана | Дата события, UTC |
| --- | --- | --- | --- |
| [Proxima Pioneer](https://github.com/JakubOleksy?achievement=proxima-pioneer&tab=achievements) | M0 Participant | Вклад в прототип Proxima, то есть proof of concept | 2023-06-01 17:34:35 |
| [Proxima Staffshipper](https://github.com/JakubOleksy?achievement=proxima-staffshipper&tab=achievements) | M8 Participant | Запуск экземпляра Proxima Staffship | 2024-08-21 22:28:27 |
| [Proxima Staffuser](https://github.com/timrogers?achievement=proxima-staffuser&tab=achievements) | When your team is on Proxima | Подключение команды к Proxima; пример у @timrogers | 2023-08-16 18:28:07 |

Это внутренние награды за работу над Proxima и его использование сотрудниками GitHub. Вывод следует из текста карточек, принадлежности профилей и характера этапов; официального публичного регламента выдачи не найдено. Получение за обычную работу в публичных репозиториях не подтверждено. **Нельзя уверенно говорить, что награды «больше не существуют»: они видны в профилях, но недоступны обычным пользователям, а дата прекращения внутренней выдачи неизвестна.**

`inaccessible` на месте ссылки события — отсутствие прав доступа к соответствующему репозиторию или организации, согласно [GitHub Docs](https://docs.github.com/en/account-and-profile/reference/profile-reference#earning-achievements). Само слово не означает удаление события или награды.

Скриншот Staffshipper показывает 22 августа 2024 года, карточка возвращает 21 августа в UTC. Различие согласуется с отображением в другом часовом поясе; часовой пояс исходного снимка не установлен. Даты пользователей не являются датами публичного запуска наград.

[Скриншот Pioneer](../assets/evidence/jakub-proxima-pioneer.png) и [Staffshipper](../assets/evidence/jakub-proxima-staffshipper.png) сохранены без изменений. URL карточек, тексты событий и отметки времени находятся в `proxima_evidence` файла [data/achievements.json](../data/achievements.json). Для чтения detail-фрагментов использован `Accept: text/fragment+html`: обычный запрос возвращал HTTP 406.

Публичная [статья об Enterprise Cloud с data residency](https://github.blog/engineering/engineering-principles/github-enterprise-cloud-with-data-residency/) описывает близкий инфраструктурный контекст, но не называет Proxima и не устанавливает правила наград. Связь названия с конкретным продуктом нельзя считать доказанной только этой статьёй. Полные значения этапов M0/M8 и закрытые документы недоступны: реконструкция задач ограничена формулировками карточек.

## Что действительно уже нельзя получить

**Arctic Code Vault Contributor.** Награда за вклад в подходящие публичные репозитории снимка от **2 февраля 2020 года**. [GitHub описал критерии отбора репозиториев](https://github.blog/open-source/maintainers/the-arctic-code-vault-starts-production-and-your-open-source-projects-are-being-archived/): активность после объявления 13 ноября 2019 года; либо минимум одна звезда и активность за предыдущий год; либо минимум 250 звёзд независимо от свежести активности. Это критерии включения репозиториев в архив, а не возможность получить награду сейчас. [Программа архива](https://archiveprogram.github.com/) продолжает сохранять код, но старый снимок не дополняется текущими коммитами.

**Mars 2020 Contributor.** Награждены авторы коммитов в конкретных версиях проектов, использованных NASA/JPL для Ingenuity. GitHub [официально указывает, что событие завершено](https://docs.github.com/en/account-and-profile/reference/profile-reference#list-of-qualifying-repositories-for-mars-2020-helicopter-contributor-achievement). Важны версии и теги, а не участие в современном Linux, Python или другом проекте. Полная таблица вынесена в [историческое приложение](mars-2020-repositories.md).

## Эксперименты и неизвестные условия

**Heart On Your Sleeve** связан в наблюдениях с реакциями ❤️; **Open Sourcerer** — с PR, принятыми в разных публичных репозиториях. Изображения базовых, бронзовых, серебряных и золотых вариантов сохранены. Картинка на CDN подтверждает наличие дизайна, а не право на получение или точный порог.

27 марта 2026 года сотрудник GitHub [подтвердил ошибочное временное включение](https://github.com/orgs/community/discussions/190746). Это были эксперименты, которые не предполагалось открывать всем; после обнаружения ошибки их снова убрали. Официального срока общего запуска не найдено. Статус — «экспериментальные / отключённые», без обещания релиза и без утверждения об окончательной отмене.

В [общественном архиве](https://github.com/Schweinepriester/github-profile-achievements) есть предварительные пороги: Heart On Your Sleeve — 16 реакций на бронзу и 128 на серебро; Open Sourcerer — 8, 16 и 64 на бронзу, серебро и золото. Базовые пороги и золотой порог Heart On Your Sleeve там не определены. Метод подсчёта Open Sourcerer не подтверждён: количество PR нельзя приравнивать к числу разных репозиториев. Эти сведения сохранены как **сообщения сообщества**, отдельно от правил доступных наград.

## Публичные награды: уточнения

| Награда | База → бронза → серебро → золото | Что считается |
| --- | --- | --- |
| Starstruck | 16 → 128 → 512 → 4096 | Звёзды конкретного созданного репозитория |
| Pull Shark | 2 → 16 → 128 → 1024 | Принятые PR, открытые пользователем |
| Pair Extraordinaire | 1 → 10 → 24 → 48 | Принятые PR с соавторством коммитов |
| Galaxy Brain | 2 → 8 → 16 → 32 | Принятые ответы в Discussions |

Числа происходят из наблюдений и историй наград. Примеры: [Starstruck у torvalds](https://github.com/torvalds?achievement=starstruck&tab=achievements), [Pull Shark](https://github.com/ljharb?achievement=pull-shark&tab=achievements) и [Galaxy Brain у ljharb](https://github.com/ljharb?achievement=galaxy-brain&tab=achievements), [Pair Extraordinaire у Rongronggg9](https://github.com/Rongronggg9?achievement=pair-extraordinaire&tab=achievements). Для соавторства важен корректный [`Co-authored-by`](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors).

Quickdraw связан с закрытием issue или PR за пять минут; YOLO — со слиянием собственного PR без review; Public Sponsor — с публичной поддержкой через [GitHub Sponsors](https://github.com/sponsors). Подтверждённых бронзовых, серебряных и золотых уровней у них нет. Точные сроки появления, исключения, обработка ботов и повторный подсчёт старой активности официально не раскрыты: мгновенная выдача не гарантируется.

Galaxy Brain не отменён глобально. С **6 февраля 2024 года** GitHub [отключил достижения внутри своей Community](https://github.com/orgs/community/discussions/106536). Ограничение касается `github.com/orgs/community`, а не всех Discussions.

Метки x2/x3/x4 означают бронзу/серебро/золото, а не умножение базового порога. Цвета: `#F9BFA7`, `#E1E4E4`, `#FAE57E`. Оттенки кожи сохранены для Starstruck и Quickdraw и не являются новыми наградами. [Настройки оформления](https://github.com/settings/appearance).

## Старые названия и другие отметки

19 апреля 2021 года GitHub [представил раздел Achievements](https://github.blog/news-insights/company-news/open-source-goes-to-mars/), а 9 июня 2022 года [обновил систему](https://github.blog/news-insights/product-news/introducing-achievements-recognizing-the-many-stages-of-a-developers-coding-journey/). Сохранены старые изображения и алиасы:

- **GitHub Sponsor** → **Public Sponsor**.
- **Mars 2020 Helicopter Contributor** / **Mars 2020 Helicopter Mission** → **Mars 2020 Contributor**.
- **Arctic Code Vault Contributor** сохранил название, изменив оформление. «2020 GitHub Archive Program» относится к тому же событию.

Первое событие может предшествовать запуску системы: учитывается историческая активность. Это не доказывает существование современного оформления в раннюю дату.

[GitHub Docs](https://docs.github.com/en/account-and-profile/reference/profile-reference#displaying-badges-on-your-profile) описывает Pro, Developer Program Member, Security Bug Bounty Hunter, GitHub Campus Expert и Security Advisory Credit. [GitHub Stars](https://stars.github.com/) добавлен как отметка участия в программе, а не автоматическая медаль за звёзды. Старый **Discussion answered** исторический: о замене на Galaxy Brain [сообщил пользователь со ссылкой на поддержку](https://github.com/orgs/community/discussions/31629). Это свидетельство сообщества, а не официальный анонс.

Сертификаты GitHub, Hacktoberfest, Shields.io, картинки в README, роли в организации, подтверждённые коммиты и компания в профиле относятся к другим системам. Они не входят в число медалей Achievements. Закрытый набор внутренних тестов остаётся неизвестным.

## Ограничения на дату проверки

[11 сентября 2026 года](https://github.blog/changelog/2026-09-11-profiles-now-show-your-highest-achievement-badge-tier/) GitHub перешёл к показу высшего уровня. В [обновлении от 23 сентября](https://github.com/orgs/community/discussions/203416) сотрудники сообщили о задержках выдачи и появления достижений, иногда на несколько дней, без срока исправления. Отсутствие награды не позволяет автоматически назвать её недоступной.

[Параметры видимости](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/manage-visibility-settings-for-private-contributions-and-achievements) управляют показом достижений и приватного вклада. Можно скрыть награду или весь раздел. Проверка ссылок в репозитории локальная; дата исследования не обещает неизменности источников в будущем.
