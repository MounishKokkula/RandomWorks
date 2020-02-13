#!/usr/bin/env python
# coding: utf-8
"""
This program is to convert values from '.xlsx' file to a bar chart.
The inputs are parsed and to check for empty values and format.
The bar chart is plotted using "turtle" a inbuilt library with python.

"""
import pandas as pd
import turtle
class DrawGraph():
    def set_data(self,year,employees,profit):
        """
        Data format/setup for the chart input
        :param year: year input from the excel sheet - format: list
        :param employees: year input from the excel sheet - format: list
        :param profit: year input from the excel sheet - format: list
        """
        # Assigning X axis values
        for i in range(len(year)):
            xList.append(str(year[i]))

        # Assigning Y axis values
        # for i in range(y_axis_min, y_axis_max, int(y_axis_max/len(employees))):
        for i in range(1,int(y_axis_max/5)+1):
            yList.append(int(i*5))

        # Assigning employee bar values
        for i in range(len(employees)):
            empbarList.append(employees[i])

        # Assigning profit bar values
        for i in range(len(profit)):
            profitbarList.append(profit[i])

    def setup(self):
        """
        Setup the initial turtle positions and values
        """
        tG.hideturtle()
        tG2.hideturtle()
        tGL.hideturtle()
        tL.hideturtle()

        tX.up()
        tY.up()
        tG.up()
        tG2.up()
        tGL.up()
        tL.up()

        tX.setpos(-500, -250)
        tY.setpos(-500, -250)
        tG.setpos(-500, -250)
        tG2.setpos(-500, -250)
        tGL.setpos(-500, -250)

    def x_axis(self):
        """
        Draw the x-axis with input values
        """
        tX.down()
        for i in range(len(xList)):
            tX.forward(100)
            tX.right(90)
            tX.forward(20)
            tX.up()
            tX.forward(XYmargin)
            tX.write(xList[i], False, align="center", font=(fontname, 10, "normal"))
            tX.right(180)
            tX.forward(20 + XYmargin)
            tX.down()
            tX.right(90)
        tX.forward(50)

    def y_axis(self):
        """
        Draw y-xis with the input values given.
        Step1) Draw the positive axis
        Step2) Draw the negative axis
        """
        # Write only 0 at the beginning
        tY.up()
        tY.setpos(-500 + zero_pos, -250 + zero_pos)
        tY.write("0", True, align="center", font=(fontname, 10, "normal"))
        tY.setpos(-500, -250)
        tY.down()

        # Fill in positive Y Axis values
        tY.left(90)
        for i in range(int(y_axis_max/5)):
            tY.forward(60)
            tY.left(90)
            tY.forward(20)
            tY.up()
            tY.forward(XYmargin)
            tY.write(yList[i], False, align="center", font=(fontname, 10, "normal"))
            tY.left(180)
            tY.forward(20 + XYmargin)
            tY.down()
            tY.left(90)
        tY.forward(50)

        # Fill in negative Y Axis values
        if y_axis_min < 0:
            tY.up()
            tY.setpos(-500, -250)
            tY.down()

            tY.left(180)
            for i in range(int(abs(y_axis_min)/5)):
                tY.forward(60)
                tY.right(90)
                tY.forward(20)
                tY.up()
                tY.forward(XYmargin)
                tY.write(-yList[i], False, align="center", font=(fontname, 10, "normal"))
                tY.right(180)
                tY.forward(20 + XYmargin)
                tY.down()
                tY.right(90)
            tY.forward(50)


    def draw_emp_bar(self):
        """
        Draw bar for employee data input
        """
        tG.fillcolor('blue')
        tG.forward(100 - int(bar_width)/ 2)
        for i in range(len(employees)):
            tG.begin_fill()
            tG.left(90)
            tG.down()
            tG.forward(int(empbarList[i])*12) # match the size of the y axis bar
            tG.right(90)
            tG.forward(bar_width/2)
            tG.right(90)
            tG.forward(int(empbarList[i])*12) # match the size of the y axis bar
            tG.left(90)
            tG.end_fill()
            tG.up()
            tG.forward(100 - int(bar_width)/ 2)


    def draw_profit_bar(self):
        """
        Draw bar for profit data input
        """
        tG2.fillcolor('green')
        tG2.forward(100)
        for i in range(len(profit)):
            tG2.begin_fill()
            tG2.left(90)
            tG2.down()
            tG2.forward(int(profitbarList[i])*12) # match the size of the y axis bar
            tG2.right(90)
            tG2.forward(bar_width/2)
            tG2.right(90)
            tG2.forward(int(profitbarList[i])*12) # match the size of the y axis bar
            tG2.left(90)
            tG2.end_fill()
            tG2.up()
            tG2.forward(100 - int(bar_width)/ 2)



    def label(self):
        tL.sety(-250 + 500 +10)
        tL.write(title, False, align="center", font=(fontname, 20, "normal"))
        tL.sety(-250 - 20 - XYmargin - 30)
        tL.write(xlabel, False, align="center", font=(fontname, 10, "normal"))
        tL.setpos(-500, 250 + 10)
        tL.write(ylabel, False, align="center", font=(fontname, 10, "normal"))


if __name__ == '__main__':

    # Read the the csv input using pandas

    excel_file = input("Please input the absolute location to the '.xlsx' file : \n")
    # Supply filename as input argument
    header = pd.read_excel(excel_file)
    print("Columns in the xlsx file: {}".format(header.columns.ravel()))
    print("Turtle draw in progress")
    year = list(header.year.fillna('n/a')) # filling 'n/a' when year is empty
    profit = list(header.profit.fillna(0)) # filling '0' when profit is empty
    employees = list(header.employees.fillna(0)) # Filling '0' when employees is empty
    y_axis_min = min(min(profit), min(employees)) # Computing Min value for positive Y axis
    y_axis_max = max(max(profit), max(employees)) # Computing Max value for negative Y axis


    turtle.screensize(1200, 900)

    tX = turtle.Pen()
    tY = turtle.Pen()
    tG = turtle.Pen() # Bar 1 - Employee
    tG2 = turtle.Pen() # Bar 2 - Profit
    tGL = turtle.Pen()
    tL = turtle.Pen()

    xList = []
    yList = []
    profitbarList= []
    empbarList= []
    zero_pos = -10
    # Bar width
    bar_width = 40
    XYmargin = 20
    fontname = "Times New Roman"
    # Graph title, label name
    title = "Employees vs Profit"
    xlabel = "Year"
    ylabel = "Employees/Profit"

    graph = DrawGraph()
    graph.set_data(year,employees,profit)
    graph.setup() # initial setup of the chart

    graph.label() # labels for the chart
    graph.x_axis() # draw x axis
    graph.y_axis() # draw y axis
    graph.draw_emp_bar() # draw employee bar
    graph.draw_profit_bar() # draw profit bar

    turtle.mainloop()
