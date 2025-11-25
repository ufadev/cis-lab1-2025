# Решение лабораторной работы

## Исправленные тесты

### Frontend тест

**Файл**: `frontend/src/App.test.tsx`

**Проблема**: После клика на кнопку счетчик увеличивается до 1, но тест проверяет, что значение осталось 0.

**Исправление**:
```typescript
// Было (строка 21):
expect(button).toHaveTextContent('count is 0')

// Стало:
expect(button).toHaveTextContent('count is 1')
```

### Backend тест

**Файл**: `backend/Tests/WeatherForecastControllerTests.cs`

**Проблема**: Переменная `id` имеет значение 1, но тест проверяет, что она равна 0.

**Исправление**:
```csharp
// Было:
Assert.Equal(0, id);

// Стало:
Assert.Equal(1, id);
```

## Эталонный пайплайн

Эталонный пайплайн находится в файле `.github/workflows/ci.reference.yml`.

Основные особенности:
- Запуск тестов для frontend и backend
- Генерация Allure отчетов
- Накопительный отчет (сохранение истории)
- Публикация в GitHub Pages

## Проверка решения

После исправления тестов:

1. **Локальное тестирование**:
   ```bash
   # Frontend
   cd frontend && npm test
   
   # Backend
   cd backend && dotnet test
   ```

2. **Запуск через act**:
   ```bash
   act push
   ```

3. **Проверка Allure отчета**:
   ```bash
   allure open allure-report
   ```

Все тесты должны быть зелеными в отчете.

## Структура Allure отчета

После успешного выполнения пайплайна Allure отчет содержит:

- **Overview**: Общая статистика по тестам
- **Suites**: Группировка тестов по наборам (Frontend/Backend)
- **Graphs**: Графики успешности тестов
- **Timeline**: Временная шкала выполнения тестов
- **Behaviors**: Поведенческие сценарии
- **Packages**: Группировка по пакетам/модулям

## Накопительный отчет

Allure поддерживает накопительные отчеты через механизм истории:

1. При первой генерации отчета создается история
2. При последующих запусках история сохраняется
3. В отчете отображается тренд выполнения тестов

Для работы накопительного отчета в пайплайне:
- История сохраняется в `allure-history`
- При генерации нового отчета история копируется обратно
- GitHub Pages сохраняет историю между деплоями

## Дополнительные улучшения

Можно добавить в пайплайн:

1. **Кэширование зависимостей**:
   ```yaml
   - uses: actions/cache@v3
     with:
       path: frontend/node_modules
       key: ${{ runner.os }}-node-${{ hashFiles('frontend/package-lock.json') }}
   ```

2. **Матричное тестирование**:
   ```yaml
   strategy:
     matrix:
       node-version: [18, 20, 22]
   ```

3. **Уведомления**:
   ```yaml
   - name: Notify on failure
     if: failure()
     uses: 8398a7/action-slack@v3
   ```

4. **Покрытие кода**:
   ```yaml
   - name: Generate coverage
     run: npm run test:coverage
   ```

