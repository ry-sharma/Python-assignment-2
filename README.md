# Python-assignment-2
This repository contains solutions to three Python programming assignments:

1) Text Encryption and Decryption: A program that reads a text file, encrypts its contents using a custom encryption method based on user input, and writes the encrypted text to a new file. It also includes functions to decrypt the text and check the correctness of the decryption.
   
   Question 1: Encrypt and decrypt text with custom rules.
      > Takes two user inputs (n, m) for encryption.
      > Encrypts lowercase and uppercase letters with different rules, leaving special characters unchanged.
      > **Note**: Ensure that raw_text.txt should be in the same directory as python script as the program uses "Relative Path" method to acces the .txt file.
  
2) Temperature Data Analysis: A program that analyzes temperature data collected from multiple weather stations in Australia. The program calculates monthly average temperatures across multiple years and generates statistics such as the warmest and coolest stations, and the station with the largest temperature range.
  
   Question 2: Analyze temperature data from multiple weather stations.
      > Calculates monthly and seasonal average temperatures.
      > Identifies the station with the largest temperature range, the warmest, and the coolest stations.
      > **Note**: # Specify the folder containing temperature data
      > temperature_folder = "temperatures"  # <-- Replace "temperatures" with the actual folder path
    Specify the output files
      > seasonal_output_file = "average_temp.txt"
      > largest_range_output_file = "largest_temp_range_station.txt"
      > warmest_coolest_output_file = "warmest_and_coolest_station.txt"
      > Relative Path: If the folder is within the same directory as your Python script, you can simply use the folder name (e.g., "temperatures").
                        Example: temperature_folder = "temperatures"
      > Absolute Path: If the folder is located somewhere else on your system, use the full path to the folder.
         temperature_folder =  "C:\\Users\\YourUsername\\Documents\\temperatures"
     
3) Recursive Tree Graphics with Turtle: A Python program that uses recursive functions to generate a tree pattern with customizable angles, branch lengths, and recursion depth using the turtle graphics library.
   
   Question 3: Create a recursive tree pattern with turtle graphics.
      > User-defined branch angles, starting length, recursion depth, and length reduction factor.


