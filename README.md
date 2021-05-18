# C++ / Python translator

This repository is for a small, simple project which aims to convert a simple c++ code to a runnable python script. 

Example : 

    #C++                                     #Python
    int number = 0;                          number = 0
    printf("test");                          print("test")
    while(true)                              while True:
    {                                             if number == 0:
        if(number == 0)                               break;
        {
            break;
        }
    }
    
What is implemented so far : 

  1) Automatic indentation for Python
  2) Printf conversion
  3) Simple while / for loop conversion
  4) Vector to list conversion
  5) Cleaning curly brackets
