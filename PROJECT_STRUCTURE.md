# Структура проекта лабораторной работы

```
lab2/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Основной пайплайн GitHub Actions
│       └── ci.reference.yml    # Эталонный пайплайн
│
├── frontend/                   # React TypeScript приложение (Vite)
│   ├── src/
│   │   ├── App.tsx            # Основной компонент
│   │   ├── App.test.tsx       # Тесты (содержит сломанный тест)
│   │   ├── App.test.fixed.tsx # Исправленная версия тестов
│   │   ├── App.css
│   │   ├── main.tsx
│   │   ├── index.css
│   │   └── test/
│   │       └── setup.ts       # Настройка тестового окружения
│   ├── index.html
│   ├── package.json           # Зависимости и скрипты
│   ├── vite.config.ts         # Конфигурация Vite и Vitest
│   ├── tsconfig.json
│   └── tsconfig.node.json
│
├── backend/                    # .NET 8 Web API
│   ├── Controllers/
│   │   └── WeatherForecastController.cs
│   ├── Tests/
│   │   ├── AllureConfig.cs                    # Конфигурация Allure
│   │   ├── WeatherForecastControllerTests.cs # Тесты (содержит сломанный тест)
│   │   ├── WeatherForecastControllerTests.fixed.cs # Исправленная версия
│   │   └── Tests.csproj
│   ├── Backend.csproj
│   ├── Program.cs
│   └── Properties/
│       └── launchSettings.json
│
├── scripts/
│   └── convert_trx_to_allure.py  # Конвертер TRX в Allure формат
│
├── README.md                    # Основная инструкция для студентов
├── QUICKSTART.md               # Быстрый старт
├── TESTING.md                  # Инструкция по тестированию с act
├── SOLUTION.md                 # Решение лабораторной работы
├── LAB_INSTRUCTIONS.md         # Инструкция для преподавателя
├── PROJECT_STRUCTURE.md        # Этот файл
├── .actrc                      # Конфигурация act
└── .gitignore                  # Игнорируемые файлы
```

## Описание компонентов

### Frontend

- **Технологии**: React 18, TypeScript, Vite, Vitest
- **Тестирование**: Vitest с поддержкой Allure через `allure-vitest`
- **Сломанный тест**: Проверка счетчика после клика (ожидает 0 вместо 1)

### Backend

- **Технологии**: .NET 8, ASP.NET Core Web API, xUnit
- **Тестирование**: xUnit с поддержкой Allure через `allure.xunit`
- **Сломанный тест**: Проверка значения id (ожидает 0 вместо 1)

### GitHub Actions пайплайн

Основные этапы:
1. Checkout кода
2. Setup .NET и Node.js
3. Установка зависимостей
4. Запуск тестов (frontend и backend)
5. Конвертация результатов в Allure формат
6. Генерация Allure отчета
7. Публикация в GitHub Pages

### Скрипты

- `convert_trx_to_allure.py` - конвертирует результаты тестов .NET (TRX формат) в формат Allure JSON

## Файлы с решениями

Для проверки правильности решения используются файлы с суффиксом `.fixed`:
- `frontend/src/App.test.fixed.tsx`
- `backend/Tests/WeatherForecastControllerTests.fixed.cs`

Эти файлы содержат исправленные версии тестов и могут использоваться для сравнения с решением студентов.

## Конфигурационные файлы

- `.actrc` - конфигурация для act (локальное тестирование GitHub Actions)
- `.gitignore` - игнорируемые файлы (node_modules, build artifacts, test results)
- `vite.config.ts` - конфигурация Vite и Vitest с поддержкой Allure
- `AllureConfig.cs` - конфигурация Allure для .NET тестов

## Документация

- `README.md` - основная инструкция с подробным описанием задач
- `QUICKSTART.md` - краткая инструкция для быстрого старта
- `TESTING.md` - подробная инструкция по тестированию с act
- `SOLUTION.md` - описание решения с исправлениями тестов
- `LAB_INSTRUCTIONS.md` - инструкция для преподавателя

## Зависимости

### Frontend
- `react`, `react-dom` - React библиотеки
- `vitest` - тестовый фреймворк
- `@testing-library/react` - утилиты для тестирования React компонентов
- `allure-vitest` - интеграция Vitest с Allure

### Backend
- `Microsoft.AspNetCore.OpenApi` - OpenAPI поддержка
- `Swashbuckle.AspNetCore` - Swagger UI
- `xunit` - тестовый фреймворк
- `allure.xunit` - интеграция xUnit с Allure

## Результаты выполнения

После выполнения пайплайна создаются:
- `allure-results/` - сырые результаты тестов
- `allure-report/` - сгенерированный HTML отчет
- `allure-history/` - история выполнения тестов (для накопительного отчета)

Эти директории должны быть в `.gitignore` и не коммититься в репозиторий.

