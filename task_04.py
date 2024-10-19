class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def display(self, indent=0):
        print(" "* indent  + f"{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 4)

    def delete(self):
        self.text = "This plunder is deleted!"
        self.deleted = True

# Створюємо коментарі
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")
reply3 = Comment("Що? Як ви можете таке писати?", "Марія")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)
reply2.add_reply(reply3)

root_comment.display()