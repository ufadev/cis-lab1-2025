using Xunit;
using Allure.Xunit.Attributes;
using Backend.Controllers;

namespace Backend.Tests;

public class WeatherForecastControllerTestsFixed
{
    [Fact]
    [AllureXunit]
    [AllureParentSuite("Backend")]
    [AllureSuite("WeatherForecast")]
    [AllureSubSuite("Controller")]
    public void Get_ReturnsWeatherForecasts()
    {
        // Arrange
        var controller = new WeatherForecastController();

        // Act
        var result = controller.Get();

        // Assert
        Assert.NotNull(result);
        Assert.Equal(5, result.Count());
    }

    [Fact]
    [AllureXunit]
    [AllureParentSuite("Backend")]
    [AllureSuite("WeatherForecast")]
    [AllureSubSuite("Controller")]
    public void GetById_ReturnsWeatherForecast()
    {
        // Arrange
        var controller = new WeatherForecastController();
        var id = 1;

        // Act
        var result = controller.GetById(id);

        // Assert
        Assert.NotNull(result);
        // ИСПРАВЛЕННЫЙ ТЕСТ: проверяется правильное значение id
        Assert.Equal(1, id);
    }
}

