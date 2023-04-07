class Mailbox:
    mails = []
    def receiveMail(self, mail: str):
        self.mails.append(mail)

    def readMail(self, number: int):
        if number < len(self.mails):
            return self.mails[number]
        else:
            return "Письма с таким номером не существует"

mailbox = Mailbox()
mailbox.receiveMail("Привет")
mailbox.receiveMail("Как")
mailbox.receiveMail("Дела")
mailbox.receiveMail("Богдан")
mailbox.receiveMail("Где")
mailbox.receiveMail("Стримы")
mailbox.receiveMail("Пока")

print(mailbox.readMail(0)) # Выводит "Привет"
print(mailbox.readMail(5)) # Выводит "Стримы"
print(mailbox.readMail(7)) # Выводит "Письма с таким номером не существует"