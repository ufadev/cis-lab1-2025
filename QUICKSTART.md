# Быстрый старт

## Шаг 1: Подготовка окружения

```bash
# Установите act (если еще не установлен)
brew install act  # macOS
# или
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash  # Linux

# Загрузите Docker образы
docker pull catthehacker/ubuntu:full-latest
docker pull node:20
docker pull mcr.microsoft.com/dotnet/sdk:8.0
```

## Шаг 2: Установите зависимости проектов

```bash
# Frontend
cd frontend
npm install
cd ..

# Backend
cd backend
dotnet restore
cd ..
```

## Шаг 3: Запустите тесты локально (чтобы увидеть ошибки)

```bash
# Frontend тесты (должен упасть один тест)
cd frontend && npm test

# Backend тесты (должен упасть один тест)
cd backend && dotnet test
```

## Шаг 4: Запустите пайплайн через act

```bash
# Из корневой директории проекта
act push
```

Вы должны увидеть:
- Установку зависимостей
- Запуск тестов (некоторые упадут)
- Генерацию Allure отчета

## Шаг 5: Исправьте тесты

### Frontend (`frontend/src/App.test.tsx`)
Измените строку 21:
```typescript
// Было:
expect(button).toHaveTextContent('count is 0')

// Должно быть:
expect(button).toHaveTextContent('count is 1')
```

### Backend (`backend/Tests/WeatherForecastControllerTests.cs`)
Измените строку с Assert.Equal:
```csharp
// Было:
Assert.Equal(0, id);

// Должно быть:
Assert.Equal(1, id);
```

## Шаг 6: Повторно запустите пайплайн

```bash
act push
```

Теперь все тесты должны пройти успешно!

## Шаг 7: Просмотрите Allure отчет

```bash
# Если allure установлен глобально
allure open allure-report

# Или через Docker
docker run --rm -v $(pwd)/allure-report:/app -p 8080:8080 frankescobar/allure-docker-service
# Откройте http://localhost:8080
```

## Полезные команды act

```bash
# Список доступных событий
act -l

# Запуск с подробным выводом
act push -v

# Запуск конкретного job
act push -j test

# Просмотр плана выполнения без запуска
act push --dry-run
```

