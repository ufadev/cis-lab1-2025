# Лабораторная работа: CI/CD пайплайн с GitHub Actions и Allure

## Цель работы

1. Реализовать пайплайн GitHub Actions для проектов на .NET 8 Web API и React TypeScript (Vite)
2. Настроить выполнение модульных тестов в обоих проектах
3. Настроить генерацию накопительного отчета Allure и публикацию его в GitHub Pages
4. Протестировать пайплайн локально с помощью `act`

## Структура проекта

```
lab2/
├── frontend/          # React TypeScript приложение (Vite)
│   ├── src/
│   │   ├── App.tsx
│   │   └── App.test.tsx  # Содержит сломанный тест
│   └── package.json
├── backend/           # .NET 8 Web API
│   ├── Controllers/
│   ├── Tests/
│   │   └── WeatherForecastControllerTests.cs  # Содержит сломанный тест
│   └── Backend.csproj
├── scripts/          # Вспомогательные скрипты
│   └── convert_trx_to_allure.py
└── .github/
    └── workflows/
        └── ci.yml     # GitHub Actions пайплайн
```

## Быстрый старт

См. [QUICKSTART.md](./QUICKSTART.md) для быстрого начала работы.

## Подробная инструкция

См. [README.md](./README.md) для полного описания задач и шагов выполнения.

## Тестирование с act

См. [TESTING.md](./TESTING.md) для подробной инструкции по тестированию пайплайна локально.

## Решение

См. [SOLUTION.md](./SOLUTION.md) для описания исправлений тестов.

## Структура проекта

См. [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) для подробного описания структуры проекта.

## Задачи

### Задача 1: Изучить структуру проекта

1. Изучите структуру frontend проекта
2. Изучите структуру backend проекта
3. Найдите сломанные тесты в обоих проектах

### Задача 2: Запустить тесты локально

#### Frontend:
```bash
cd frontend
npm install
npm test
```

Вы должны увидеть, что один тест падает.

#### Backend:
```bash
cd backend
dotnet restore
dotnet test
```

Вы должны увидеть, что один тест падает.

### Задача 3: Установить и настроить act

1. Установите `act` согласно [официальной документации](https://github.com/nektos/act)

   Для macOS:
   ```bash
   brew install act
   ```

   Для Linux:
   ```bash
   curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
   ```

2. Проверьте установку:
   ```bash
   act --version
   ```

3. Загрузите необходимые Docker образы для act:
   ```bash
   docker pull catthehacker/ubuntu:full-latest
   docker pull node:20
   docker pull mcr.microsoft.com/dotnet/sdk:8.0
   ```

### Задача 4: Запустить пайплайн с помощью act

1. Запустите пайплайн локально:
   ```bash
   act push
   ```

   Или для конкретного события:
   ```bash
   act -W .github/workflows/ci.yml push
   ```

2. Изучите вывод. Вы должны увидеть:
   - Установку зависимостей
   - Запуск тестов (некоторые должны упасть)
   - Генерацию Allure отчета

### Задача 5: Изучить Allure отчет

1. После выполнения пайплайна найдите сгенерированный Allure отчет
2. Откройте отчет в браузере:
   ```bash
   allure serve allure-results
   ```

   Или если отчет уже сгенерирован:
   ```bash
   allure open allure-report
   ```

3. Найдите в отчете упавшие тесты:
   - Frontend: тест на инкремент счетчика
   - Backend: тест GetById_ReturnsWeatherForecast

### Задача 6: Исправить сломанные тесты

#### Frontend тест

Откройте `frontend/src/App.test.tsx` и найдите строку:
```typescript
expect(button).toHaveTextContent('count is 0')
```

Исправьте на:
```typescript
expect(button).toHaveTextContent('count is 1')
```

#### Backend тест

Откройте `backend/Tests/WeatherForecastControllerTests.cs` и найдите строку:
```csharp
Assert.Equal(0, id);
```

Исправьте на:
```csharp
Assert.Equal(1, id);
```

### Задача 7: Повторно запустить пайплайн

1. Запустите тесты локально, чтобы убедиться, что они проходят:
   ```bash
   # Frontend
   cd frontend && npm test
   
   # Backend
   cd backend && dotnet test
   ```

2. Запустите пайплайн через act:
   ```bash
   act push
   ```

3. Проверьте, что все тесты проходят успешно

4. Изучите обновленный Allure отчет - все тесты должны быть зелеными

### Задача 8: Настроить публикацию отчета в GitHub Pages

1. Убедитесь, что в пайплайне настроена публикация отчета:
   ```yaml
   - name: Deploy Allure Report to GitHub Pages
     if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
     uses: peaceiris/actions-gh-pages@v3
   ```

2. В настройках репозитория GitHub включите GitHub Pages:
   - Settings → Pages
   - Source: GitHub Actions

3. После пуша в main/master ветку отчет будет доступен по адресу:
   `https://<username>.github.io/<repository>/allure-report/`

## Дополнительные задания

1. **Накопительный отчет**: Изучите, как работает накопительный отчет Allure (история тестов)

2. **Улучшение пайплайна**: Добавьте этапы:
   - Линтинг кода
   - Проверка покрытия тестами
   - Сборка приложений

3. **Матричная сборка**: Настройте тестирование на разных версиях Node.js и .NET

4. **Уведомления**: Добавьте отправку уведомлений при падении тестов

## Вопросы для самопроверки

1. Что такое CI/CD и зачем он нужен?
2. Как работает GitHub Actions?
3. Что такое Allure и для чего он используется?
4. Как работает накопительный отчет в Allure?
5. Что такое `act` и зачем он нужен?
6. Как отлаживать пайплайны GitHub Actions локально?

## Полезные ссылки

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Allure Framework](https://docs.qameta.io/allure/)
- [act - Run GitHub Actions locally](https://github.com/nektos/act)
- [Vitest Documentation](https://vitest.dev/)
- [xUnit Documentation](https://xunit.net/)

## Решение проблем

### Проблема: act не может найти Docker образы

**Решение**: Загрузите необходимые образы вручную:
```bash
docker pull catthehacker/ubuntu:full-latest
docker pull node:20
docker pull mcr.microsoft.com/dotnet/sdk:8.0
```

### Проблема: Тесты не генерируют Allure отчеты

**Решение**: 
1. Проверьте, что установлены необходимые пакеты:
   - Frontend: `allure-vitest`
   - Backend: `allure.xunit`

2. Проверьте конфигурацию:
   - Frontend: `vite.config.ts` должен содержать настройки для Allure
   - Backend: должен быть файл `AllureConfig.cs`

### Проблема: GitHub Pages не публикует отчет

**Решение**:
1. Убедитесь, что в настройках репозитория включен GitHub Pages
2. Проверьте, что пайплайн выполняется на ветке main/master
3. Проверьте права доступа токена GITHUB_TOKEN

## Критерии оценки

- ✅ Пайплайн успешно запускается через act
- ✅ Все тесты проходят после исправления
- ✅ Allure отчет генерируется корректно
- ✅ Отчет публикуется в GitHub Pages
- ✅ Накопительный отчет работает (история тестов сохраняется)
