class MidtermChatBot:
  def __init__(self):
      self.subject_name = "AI for Robot System"

  def showSubjectName(self):
      print(f"{self.subject_name}")

  def showStudentYear(self):
      student_id = input(" ")
      year = 67 - (int(student_id[0])* 10 + int(student_id[1]))
      print(f"{year}")

  def calculator(self):
      operator = input(" ")
      num1 = int(input(" "))
      num2 = int(input(" "))
      if operator == "+":
          result = num1 + num2
      elif operator == "-":
          result = num1 - num2
      elif operator == "*":
          result = num1 * num2
      elif operator == "/":
          if num2 == 0:
              print("Division by zero is not allowed.")
              return
          result = num1 / num2
      print(f"{result}")

  def main(self):
      while True:
          command = input(" ")

          if command == "subject":
              self.showSubjectName()
          elif command == "year":
              self.showStudentYear()
          elif command == "calc":
              self.calculator()

if __name__ == "__main__":
  chatbot = MidtermChatBot()
  chatbot.main()
