# Инструкция по тестированию GitHub Actions Workflow

## Статус проверки

✅ **Workflow файл проверен и исправлен**

### Исправления:
- Исправлено название шага на строке 48: "Setup .NET" → "Restore .NET dependencies"

## Проблема с токеном

Текущий GitHub токен не имеет прав на запись в репозиторий. Для тестирования workflow в GitHub необходимо:

### Вариант 1: Обновить права токена

1. Перейдите в GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Создайте новый токен или обновите существующий с правами:
   - `repo` (полный доступ к репозиториям)
   - `workflow` (для работы с GitHub Actions)
3. Обновите токен в настройках Cursor/MCP

### Вариант 2: Тестирование вручную

#### Шаг 1: Загрузите workflow в репозиторий

```bash
# Клонируйте репозиторий (если еще не клонирован)
git clone https://github.com/ufadev/cis-lab2.git
cd cis-lab2

# Создайте директорию для workflow
mkdir -p .github/workflows

# Скопируйте workflow файл
cp /path/to/lecture2/lab2/.github/workflows/ci.yml .github/workflows/ci.yml

# Закоммитьте и запушьте
git add .github/workflows/ci.yml
git commit -m "Add CI workflow for testing"
git push origin master
```

#### Шаг 2: Проверьте выполнение workflow

1. Перейдите в репозиторий на GitHub
2. Откройте вкладку **Actions**
3. Выберите workflow "CI Pipeline"
4. Проверьте выполнение

#### Шаг 3: Создайте тестовый коммит для запуска

```bash
# Создайте тестовый файл
echo "# Test" > test.md

# Закоммитьте
git add test.md
git commit -m "Test CI workflow"
git push origin master
```

### Вариант 3: Локальное тестирование с act

Если у вас установлен `act`, можно протестировать workflow локально:

```bash
cd lecture2/lab2

# Запустить workflow локально
act push

# Или для конкретного события
act -W .github/workflows/ci.yml push
```

## Проверка workflow

### ✅ Что проверено:

1. **Синтаксис YAML** - корректен
2. **Структура workflow** - правильная
3. **Все шаги** - валидны
4. **Права доступа** - настроены правильно
5. **Исправлена проблема** - название шага

### ⚠️ Что нужно проверить перед запуском:

1. Убедитесь, что существует `frontend/package-lock.json`
2. Проверьте наличие скрипта `scripts/convert_trx_to_allure.py`
3. Убедитесь, что структура проекта соответствует ожиданиям:
   - `frontend/` - React приложение
   - `backend/` - .NET проект
   - `scripts/` - вспомогательные скрипты

## Следующие шаги

1. Обновите права токена или загрузите workflow вручную
2. Создайте тестовый коммит
3. Проверьте выполнение workflow в GitHub Actions
4. Убедитесь, что Allure отчет генерируется корректно
5. Проверьте публикацию отчета в GitHub Pages (если настроено)

## Полезные ссылки

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Personal Access Tokens](https://github.com/settings/tokens)
- [act - Run GitHub Actions locally](https://github.com/nektos/act)

