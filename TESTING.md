# Инструкция по тестированию пайплайна с act

## Подготовка

1. Убедитесь, что установлен Docker:
   ```bash
   docker --version
   ```

2. Установите act:
   ```bash
   # macOS
   brew install act
   
   # Linux
   curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
   
   # Windows (через Chocolatey)
   choco install act-cli
   ```

3. Загрузите необходимые Docker образы:
   ```bash
   docker pull catthehacker/ubuntu:full-latest
   docker pull node:20
   docker pull mcr.microsoft.com/dotnet/sdk:8.0
   ```

## Тестирование пайплайна

### Базовый запуск

```bash
# Запуск пайплайна для события push
act push

# Запуск для конкретного workflow файла
act -W .github/workflows/ci.yml push

# Запуск с выводом всех шагов
act push -v
```

### Запуск с конкретным событием

```bash
# Симуляция push в main ветку
act push -e push.json

# Где push.json:
# {
#   "ref": "refs/heads/main",
#   "repository": {
#     "name": "test-repo"
#   }
# }
```

### Отладка

```bash
# Запуск с подробным выводом
act push -v

# Запуск конкретного job
act push -j test

# Запуск конкретного шага
act push -l

# Просмотр списка доступных событий
act -l
```

## Ожидаемый результат

При первом запуске вы должны увидеть:

1. ✅ Установку зависимостей (frontend и backend)
2. ❌ Падение тестов (frontend и backend)
3. ✅ Генерацию Allure отчета с информацией об упавших тестах

После исправления тестов:

1. ✅ Все тесты проходят успешно
2. ✅ Allure отчет показывает все тесты зелеными
3. ✅ Отчет готов к публикации в GitHub Pages

## Решение проблем

### Проблема: act не может найти образы

**Решение**: Убедитесь, что образы загружены:
```bash
docker images | grep catthehacker
docker images | grep node
docker images | grep dotnet
```

### Проблема: Тесты не запускаются

**Решение**: Проверьте, что зависимости установлены:
```bash
# Frontend
cd frontend && npm install

# Backend
cd backend && dotnet restore
```

### Проблема: Allure отчет не генерируется

**Решение**: 
1. Проверьте, что директория `allure-results` создается
2. Убедитесь, что Allure CLI загружается в пайплайне
3. Проверьте права доступа к файлам

## Проверка результатов

После успешного выполнения пайплайна:

1. Проверьте наличие директории `allure-report`
2. Откройте отчет локально:
   ```bash
   allure open allure-report
   ```
   
   Или если allure не установлен глобально:
   ```bash
   # Используйте Docker
   docker run --rm -v $(pwd)/allure-report:/app -p 8080:8080 frankescobar/allure-docker-service
   ```

3. Убедитесь, что в отчете отображаются:
   - Все тесты из frontend
   - Все тесты из backend
   - Правильный статус (passed/failed)
   - История выполнения (если это не первый запуск)

## Эталонный запуск

Для проверки эталонного решения:

1. Исправьте тесты (замените файлы на `.fixed` версии)
2. Запустите пайплайн:
   ```bash
   act push
   ```
3. Убедитесь, что все тесты проходят
4. Проверьте Allure отчет - все тесты должны быть зелеными

