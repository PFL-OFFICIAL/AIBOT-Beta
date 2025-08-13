import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from transformers import pipeline

class AIBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Bot")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Ask me anything:")
        layout.addWidget(self.label)

        self.text_input = QTextEdit()
        layout.addWidget(self.text_input)

        self.button = QPushButton("Send")
        self.button.clicked.connect(self.get_response)
        layout.addWidget(self.button)

        self.response_label = QLabel("Response will appear here.")
        layout.addWidget(self.response_label)

        self.setLayout(layout)

        # Load AI model
        self.chatbot = pipeline("text-generation", model="distilgpt2")

    def get_response(self):
        user_text = self.text_input.toPlainText().strip()
        if not user_text:
            self.response_label.setText("Please type something!")
            return
        response = self.chatbot(user_text, max_length=100, do_sample=True, temperature=0.7)
        self.response_label.setText(response[0]["generated_text"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AIBotApp()
    window.show()
    sys.exit(app.exec_())
