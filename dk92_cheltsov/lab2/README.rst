Лаболаторная работа 2

Клас который наследует имее теже параметры и функции что и родительский клас
класы battery, accumulator, power_supply наследуют power_supply

определяет поведения больше и меньше для коректного сравнения емкости аккумуляторв
def __lt__(self, other):
        return (self.C * self.volts) < (other.C * other.volts)
def __lt__(self, other):
        return (self.C * self.volts) < (other.C * other.volts)
        
меняет строковое представление на заданое отображение при принт (возврящяет строку)
def __lt__(self, other):
        return (self.C * self.volts) < (other.C * other.volts)
        
2й метод который меняет строковое представление на заданое отображение при принт (используеться также для добавления в контейнеры)
def __lt__(self, other):
        return (self.C * self.volts) < (other.C * other.volts)
        
код в нутрт запускаеться толкько при запуске как модуля, не может импортироваться и запускатьмся другим скриптом
if __name__ == "__main__":
    print("This code do not rum from call from another code")
    _demo_()
