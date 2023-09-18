from PyQt6.QtWidgets import *
import sys
import pyshorteners
import pyperclip
import validators 

#URL application
class URLshortner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("URL Shortnner")
        self.setFixedSize(300,300)

        self.grid=QGridLayout()
        #URL Input 
        namelable=QLabel("URL:")
        self.name_line_edit=QLineEdit()
        self.grid.addWidget(namelable,0,0)
        self.grid.addWidget(self.name_line_edit,0,1)
        #URls shortner button
        cal_button=QPushButton("Short URL")
        cal_button.clicked.connect(self.url_shortner)
        self.grid.addWidget(cal_button,1,0,1,2)
        #URL Output 
        self.shorten_url=QLineEdit()
        self.grid.addWidget( self.shorten_url,2,0,1,2)
        #Copy Button
        copy_btn=QPushButton("Copy URL")
        copy_btn.clicked.connect(self.copy_url)
        self.grid.addWidget(copy_btn,3,0,1,2)

        #Copy button
        clear_button=QPushButton("Clear")
        clear_button.clicked.connect(self.clear_txt)
        self.grid.addWidget(clear_button,4,0,1,2)




        self.setLayout(self.grid)

    def url_shortner(self):
        short_obj=pyshorteners.Shortener() #create an object of the pyshorteners.Shortener() 
        if self.name_line_edit.text(): #check if Input is present
            org_url=self.name_line_edit.text()
            validation = validators.url(org_url) #Store the output of the validators.url() in a variable.
            if validation: 

        
            
                self.short_url=short_obj.tinyurl.short(self.name_line_edit.text())

                self.shorten_url.setText(self.short_url)
            else:
                self.shorten_url.setText("Error URL not valid") 
        else:
            self.shorten_url.setText("Error No input")

            

    def copy_url(self):
        pyperclip.copy(self.short_url)
    
    def clear_txt(self):
        self.shorten_url.clear()
        self.name_line_edit.clear()
        



        


        


app=QApplication(sys.argv)  
agecal=URLshortner()
agecal.show()
sys.exit(app.exec())