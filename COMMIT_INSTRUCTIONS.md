# Инструкция для коммита изменений CI workflow

## Изменения в `.github/workflows/ci.yml`

Workflow был обновлен для поддержки:
- ✅ Накопительного Allure отчета (история сохраняется между запусками)
- ✅ Публикации на GitHub Pages
- ✅ Правильных permissions для GitHub Pages

## Команды для коммита и пуша

```bash
cd /Users/ufadev/Documents/lectures/cicd/lecture2/lab2

# Добавить изменения
git add .github/workflows/ci.yml

# Создать коммит
git commit -m "Настроен CI с накопительным Allure отчетом и публикацией на GitHub Pages"

# Запушить в репозиторий
git push origin master
```

## После пуша

1. CI workflow автоматически запустится
2. После первого успешного запуска:
   - Перейдите в Settings → Pages
   - Выберите Source: GitHub Actions
3. Отчет будет доступен по адресу:
   - `https://ufadev.github.io/cis-lab1-2025/`

## Проверка через act (локально)

```bash
# Dry-run проверка
act push -W .github/workflows/ci.yml --dryrun

# Полный запуск (если нужно)
act push -W .github/workflows/ci.yml
```

