// Устанавливаем значение ШИМ (от 0 до 255)
int pwmValue = 255;

void setup()
{
  // Устанавливаем пин 9 как выход
  pinMode(9, OUTPUT);

  // Выводим значен на 9 пин
  analogWrite(9, pwmValue);
}

void loop()
{

}
