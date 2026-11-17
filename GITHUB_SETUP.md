# Чек-лист первого запуска на GitHub

Этот файл нужен ровно один раз — после создания репозитория. Потом его
можно удалить (или оставить, он никому не мешает).

## 1. Создать репозиторий

Открой <https://github.com/new>:

- имя: `dsa-python-notes`;
- видимость: **Public** (README задуман как портфолио);
- **не** добавляй README/`.gitignore`/лицензию — они уже есть в коммитах.

```bash
cd D:\codes\dsa-python-notes
git remote add origin https://github.com/dskil/dsa-python-notes.git
git push -u origin main
```

## 2. Заменить плейсхолдер бейджа

В README строка бейджа tests содержит `USERNAME`. Замени на свой логин
`dskil`, иначе картинка не отрисуется:

```bash
# Windows PowerShell
(Get-Content README.md) -replace 'USERNAME', 'dskil' | Set-Content README.md
```

## 3. Включить Actions

- Settings → Actions → General → Workflow permissions: **Read and write**
  (нужно `docs.yml`, чтобы проверять, что `docs/tasks.md` не устарел).
- Вкладка Actions: дождись зелёного `tests` на `main`.

## 4. Заполнить описание репозитория

В правой колонке «About»:

> Алгоритмический тренажёр на Python: 86 задач, у каждой — условие, решение
> и автотесты. CLI для запуска проверок и отслеживания прогресса.

Topics (тоже в About):

`python` `algorithms` `learning` `pytest` `cli` `education` `trainer` `dsa`

## 5. Releases (PyPI по желанию)

Публикация в PyPI работает по тегу `v*.*.*` и нужен секрет
`PYPI_API_TOKEN` (Settings → Secrets → Actions). Если публиковать
не планируешь — просто не создавай тег, workflow не запустится.

Если хочешь настоящий GitHub Release без PyPI — создай тег:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## 6. Защита ветки (по желанию)

Settings → Branches → Add rule для `main`:

- Require status checks to pass: `test (ubuntu-latest, 3.12)`;
- Require pull request before merging.

## Готово

Проверить, что всё живое, можно локально:

```bash
pytest -q
python tools/build_catalog.py --check
python tools/smoke_cli.py --full
```
