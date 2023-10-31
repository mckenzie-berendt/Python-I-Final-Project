import matplotlib.pyplot as plt

global option

def greeting ():
    """user selects option 1, 2, or quit"""
    print("Welcome to the chartmaker! \n Option 1 -  Manual data entry to create chart : Please enter '1' \n Option 2 - Enter data from file to create chart : please enter '2'  ")
    global option
    option = input("please enter 1, 2, or 'Q' to exit program: ").strip()
    while option not in ["1", "2", "q", "Q"]:
        print("Not a valid input - please try again")
        option = input("please enter 1, 2, or 'Q' to exit program").strip()
    return option

def get_manual_entry_x(): #option 1 function
    """user selects how many datapoints they need and enters their x-values using a loop"""
    print("Option 1 selected - Manual entry")
    global x_values
    x_values = []
    global data_points
    reasonable_number_datapoints = ['2', '3', '4', '5', '6', '7', '8', '9', '10'] #max of 10 to limit iterations later in this function
    data_points = input("Enter the number of x-axis data points you'd like to enter (whole number; min 2 & max 10)\n ")
    while data_points not in reasonable_number_datapoints:
        print("Invalid entry for number of data points")
        data_points = input("Enter the number of x-axis data points you'd like to enter (whole number; min 2 & max 10)\n")
    data_points = int(data_points) # changes the string to an int so it can function numerically
    counter = 1
    x_point_first = (input("please enter first X-axis value: ")).strip()
    while x_point_first.isnumeric() != True:
        print("data point must be a number!")
        x_point_first = (input("please enter first X-axis value: ")).strip()
    x_values.append(x_point_first)
    while counter != data_points:
        x_point_next = (input("please enter next X-axis value: ")).strip()
        while x_point_next.isnumeric() != True:
            print("data point must be a number!")
            x_point_next = (input("please enter next X-axis value: ")).strip()
        x_values.append(x_point_next)
        counter = counter + 1
    print(x_values)
    return x_values, data_points

def get_y_values(): #option 1 function
    """user enter y-values using a loop"""
    global y_values
    y_values = []
    counter = 1
    print(f"you entered {data_points} x-coordinates. Please now enter {data_points} correspoding y-coordinates.")
    y_point_first = (input("Please enter first Y-axis value: ")).strip()
    while y_point_first.isnumeric() != True:
        print("data point must be a number!")
        y_point_first = (input("please enter first Y-axis value: ")).strip()
    y_values.append(y_point_first)
    while counter != data_points:
        y_point_next = (input("please enter next Y-axis value: ")).strip()
        while y_point_next.isnumeric() != True:
            print("data point must be a number!")
            y_point_next = (input("please enter next Y-axis value: ")).strip()
        y_values.append(y_point_next)
        counter = counter + 1
    print(y_values)
    return y_values

def get_chart_title(): #option 1 function
    """user selects if they want a chart title; if yes then the user is prompted to input a string for the title"""
    global plot_title
    plot_title = ""
    plot_title_choice = input("Would you like a plot title? [Y/N] \n")
    while plot_title_choice not in ["y", "n", "Y", "N"]:
        print("please enter Y or N")
        plot_title_choice = input("Would you like a plot title? [Y/N] \n")
    if plot_title_choice == "y" or plot_title_choice == "Y":
        plot_title = (input("Please enter a plot title \n")).strip()
        while len(plot_title) < 1:
            print("title must be atleast one character in length!")
            plot_title = (input("Please enter a plot title \n")).strip()
    return plot_title

def get_x_axis_label(): #option 1 function
    """user selects if they want a x-axis label; if yes then
     the user is prompted to input a string for the label"""
    global x_label
    x_label = ""
    x_label_choice = input("Would you like an x-axis label? [Y/N] \n")
    while x_label_choice not in ["y", "n", "Y", "N"]:
        print("please enter Y or N")
        x_label_choice = input("Would you like an x-axis label? [Y/N] \n")
    if x_label_choice in ["y","Y"]:
        x_label = (input("Please enter x-axis label \n")).strip()
        while len(x_label) < 1:
            print("title must be atleast one character in length!")
            x_label = (input("Please enter x-axis label \n")).strip()
    return x_label

def get_y_axis_label(): #option 1 function
    """user selects if they want a y-axis label; if yes then the user is prompted to input a string for the label"""
    global y_label
    y_label = ""
    y_label_choice = input("Would you like an y-axis label? [Y/N] \n")
    while y_label_choice not in ["y", "n", "Y", "N"]:
        print("please enter Y or N")
        y_label_choice = input("Would you like an y-axis label? [Y/N] \n")
    if y_label_choice in ["y","Y"]:
        y_label = (input("Please enter y-axis label \n")).strip()
        while len(y_label) < 1:
            print("title must be atleast one character in length!")
            y_label = (input("Please enter y-axis label \n")).strip()
    return y_label

def get_line_style(): #option 1 function
    """user selects if they want a custom line style; if yes then the user is prompted to input a numerical value representing their choice"""
    global line_style
    line_style = '-'
    line_style_choice = input("Would you like to choose a custom line style? [Y/N] \n")
    while line_style_choice not in ["Y", 'y', 'N', 'n']:
        print("please enter Y or N")
        line_style_choice = input("Would you like to choose a custom line style? [Y/N] \n")
    if line_style_choice in ['y', 'Y']:
        print("1- solid line \n2- dotted line\n3-dashed line\n4- dashed/dotted line")
        line_style = input("please choose 1, 2, 3, or 4 \n")
        while line_style not in ['1', '2', '3', '4']:
            print("invalid response!")
            line_style = input("please choose 1, 2, 3, or 4 \n")
        if line_style == "1":
            line_style = '-'
        elif line_style == "2":
            line_style = ':'
        elif line_style == "3":
            line_style = '--'
        elif line_style == "4":
            line_style = '-.'
    return line_style

def get_maker_style(): #option 1 function
    """user selects if they want a custom marker style; if yes then the user is prompted to input a numerical value representing their choice"""
    global marker_style
    marker_style = 'o'
    marker_style_choice = input("Would you like to choose a marker style? [Y/N] \n")
    while marker_style_choice not in ["Y", 'y', 'N', 'n']:
        print("Please enter Y or N")
        marker_style_choice = input("Would you like to choose a marker style? [Y/N] \n")
    if marker_style_choice in ["y","Y"]:
        print("1-Circle\n2-Star\n3-X\n4-Square\n5-diamond")
        marker_style = input("please enter 1, 2, 3, 4, or 5\n")
        while marker_style not in ['1','2','3','4','5']:
            marker_style = input("please enter 1, 2, 3, 4, or 5\n")
        if marker_style == '1':
            marker_style = 'o'
        elif marker_style =='2':
            marker_style ='*'
        elif marker_style =='3':
            marker_style ='x'
        elif marker_style =='4':
            marker_style = 's'
        elif marker_style == '5':
            marker_style = 'D'
    return marker_style




def get_file_name(): #option 2 function
    """user is prompted to input a file name"""
    global file_name
    file_name = (input("please enter the file name (i.e exampledata.txt): ")).strip()
    while file_name != "exampledata.txt":
        print("File doesn't exist!")
        file_name = input("please enter the file name (i.e exampledata.txt): ")
    return file_name

def open_file_name(): #option 2 function
    """file is opened"""
    global examplefile
    examplefile = open(file_name, 'r')
    return examplefile

def get_file_values(): #option 2 function
    """file is read line by line - each line is assigned as a variable"""
    #first line -x values
    global x_values_from_file
    x_values_from_file = (examplefile.readline()).split(", ")
    #second line - y values
    global y_values_from_file
    y_values_from_file = (examplefile.readline()).split(", ")
    #thid line - plot title
    global plot_title
    plot_title = examplefile.readline()
    #fourth line - x-axis
    global x_label  
    x_label = examplefile.readline()
    #fifth line - y-axis
    global y_label
    y_label = examplefile.readline()
    # sixth line - linestyle value
    global linevalue
    linevalue = int(examplefile.readline())
    # seventh line - markerstyle value
    global markervalue
    markervalue = int(examplefile.readline())
    return x_values_from_file, y_values_from_file, plot_title, x_label, y_label, linevalue, markervalue, 

def config_x_values(): #option 2 function
    """x-values variable from previous file is modified so it is a list with only numbers and no '/n' attached to the last item"""
    global x_values
    x_values = []
    for item in x_values_from_file:
        for x in item.split():
            value = ''
            if x.isdigit():
                value = value + x
        x_values.append(value)
        print(x_values)
    return x_values

def config_y_values(): #option 2 function
    """y-values variable from previous file is modified so it is a list with only numbers and no '/n' attached to the last item"""
    global y_values
    y_values = []
    for item in y_values_from_file:
        for x in item.split():
            value = ''
            if x.isdigit():
                value = value + x
        y_values.append(value)
        print(y_values)
    return y_values

def config_linevalue(): #option 2 function
    """Linevalue variable is assessed and the line_style variable is assigned correspondingly."""
    global line_style
    line_style = ''
    if linevalue == 1:
        line_style = '-'
    elif linevalue == 2:
        line_style= ':'
    elif linevalue == 3:
        line_style = '--'
    elif linevalue == 4:
        line_style = '-.'
    else:
        line_style = '-'
    return line_style

def config_markervalue(): #option 2 function
    """Markervalue variable is assessed and the marker_style variable is assigned correspondingly."""
    global marker_style
    marker_style = ""
    if markervalue == 1:
        marker_style = 'o'
    elif markervalue == 2:
        marker_style ='*'
    elif markervalue == 3:
        marker_style = 'x'
    elif markervalue == 4:
        marker_style = 's'
    elif markervalue == 5:
        marker_style = 'D'
    else:
        marker_style = 'o'
    return marker_style

def get_chart(): #option 1 & 2 function
    """uses matplotlib module to create a chart using variables from options 1 and 2"""
    plt.plot(x_values, y_values, marker = marker_style, linestyle = line_style)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

while True: #main program loop

    greeting()

    if option in ["q", "Q"]:
        break
    elif option == "1":
        get_manual_entry_x()
        get_y_values()
        get_chart_title()
        get_x_axis_label()
        get_y_axis_label()
        get_line_style()
        get_maker_style()
        get_chart()
        break
        

    elif option == "2":
        get_file_name()
        open_file_name()
        get_file_values()
        config_x_values()
        config_y_values()
        config_linevalue()
        config_markervalue()
        get_chart()
        break
        

print("goodbye!")