# Maintaining the catalogue / Обновление каталога

The catalogue is built from one set of records and 25 complete translations. Edit the source files, then regenerate the Markdown; do not edit `catalog/*.md` or `lang/*.md` directly.

Каталог собирается из единой базы и 25 полных переводов. Редактируйте исходные данные и переводы, затем пересобирайте Markdown. Страницы в `catalog/` и ссылки в `lang/` генерируются автоматически.

## Update a record / Изменить запись

1. Edit [data/achievements.json](data/achievements.json): preserve the stable `id`; update status, tiers, evidence and `checked_on` only after checking sources.
2. Add a source with a unique ID and a direct URL. Use `official` for GitHub documentation or staff announcements, `observed` for an actual awarded profile card, and `community` for an independently reported observation.
3. Update the description in **every** locale under [i18n/](i18n/). Keep GitHub badge names unchanged. Translate explanations and navigation; preserve factual values, dates and uncertainty.
4. Add original artwork to [assets/](assets/) and record its origin in [assets/manifest.json](assets/manifest.json). A PNG on a CDN proves artwork exists, not that a badge is publicly obtainable.
5. Rebuild and check with Python 3.10 or newer:

```bash
python scripts/build_catalog.py
python scripts/check_catalog.py
```

Измените запись, добавьте прямой источник, обновите описание во всех переводах и происхождение новых изображений. Само наличие PNG на CDN не доказывает доступность награды. После этого выполните команды выше.

The checker runs `build_catalog.py --check` too. It performs local verification without contacting GitHub. Link availability and badge status must be researched separately; the recorded date is a research date, not a live-status guarantee.

Проверка работает локально и не обращается к GitHub. Актуальность внешних ссылок и статуса наград проверяется отдельно; дата означает дату исследования.

## Add a translation / Добавить перевод

Copy [i18n/en.json](i18n/en.json), translate every field, and add a unique language entry to [i18n/languages.json](i18n/languages.json). Update the language table in the root README. The generator includes the new language in every catalogue’s navigation. English fallback is intentionally not used.

Скопируйте структуру `i18n/en.json`, переведите все поля и добавьте язык в `i18n/languages.json` и таблицу главного README. Генератор включит язык в навигацию всех каталогов. Пропуски переводов считаются ошибками.

## Evidence rules / Работа с доказательствами

- Treat hidden event links as a visibility restriction, not an indication that the badge is deleted.
- Keep experimental thresholds separate from the earnable tier table. Mark unknown values as unknown instead of guessing.
- Do not count renamed designs, badge tiers or skin-tone variants as new achievement types.
- Separate program labels, external certificates and README graphics from native achievements.
- Record timestamps in UTC. A viewer’s displayed date may differ by time zone.
- Review translations with fluent speakers when possible; synchronized keys establish coverage, not linguistic certification.

Скрытые события не означают удаление награды. Экспериментальные пороги храните отдельно, неизвестные значения не выдумывайте. Старые названия и варианты оформления не увеличивают число достижений. Для дат сохраняйте UTC. Синхронизация полей проверяет полноту, но не заменяет языковую редактуру носителями.
