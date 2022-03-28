"""
File: buttondemo.py
"""


from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):

    
    def __init__(self):
        EasyFrame.__init__(self)

        self.label = self.addLabel(text = "Hello world!",
                                   row = 0, column = 0,
                                   columnspan = 2,
                                   sticky = "NSEW")
        self.clearBtn = self.addButton(text = "Clear",
                                       row = 1, column = 0)

        self.restoreBtn = self.addButton(text = "Restore",
                                         row = 1, column = 1,
                                         state = "disabled")

        def clear(self):
            self.label["text"] = ""
            self.clearBtn["state"] = "disabled"
            self.restoreBtn["state"] = "normal"


        def restore(self):
            self.label["text"] = "hello world!"
            self.clearBtn["state"] = "normal"
            self.restoreBtn["state"] = "disabled"
        
def main():
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()          
