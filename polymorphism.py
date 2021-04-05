#implementing a  program to demonstrate polymorphism


class IOS():
    def source(self):
        print("It is not free source and it is platform dependent")
   
    def language(self):
        print("Swift is used in it and it is a powerful and intuitive programming language for macOS, iOS, watchOS, tvOS and beyond")
   
    def Advantages(self):
        print("Excellent UI and fluid responsive.")
        print("Developers can design apps because less number of models.")
        print("Metal and shiny coating are ultimate for Apple devices.")
        print("Jailbreaking for customization.")
        print("Generates less heat when compared to Android.")
        print("Excellent for media entertainment.")
        print("Suits for business and gaming.")
        print("iOS Is More Intuitive")
   
class Android():
    def source(self):
        print("It is free source and it is platform independent")
   
    def language(self):
        print("The official language for Android development is Java.")
   
    def Advantages(self):
        print("Universal Chargers")
        print("More Phone Choices Are a Clear Advantage of Android.")
        print("Removable Storage and Battery.")
        print("Access to the Best Android Widgets.")
        print("Better Hardware.")
        print("Better Charging Options are Another Android Pro.")
        print("Infrared")
        print("Why Android is Better Than iPhone: More App Choices.")
  
def func(obj):
    obj.source()
    obj.language()
    obj.Advantage()
   
obj_ios = IOS()
obj_Android = Android()
   
func(obj_ios)
func(obj_Android)