import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
browser = QWebEngineView()
browser.setUrl("https://google.co.jp")
browser.show()
sys.exit(app.exec_())
