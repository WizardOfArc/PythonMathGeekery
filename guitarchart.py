#!/usr/bin/python
import sys

def makeChart(position=0):
    newChart = []
    for i in xrange(5):
        tempRow = []
        for j in xrange(6):
            if j < 4:
                tempRow.append(position+i+(5*j))
            else:
                tempRow.append(position+i+(5*j)-1)
        newChart.append(tempRow)
    return newChart

def displayChart(position=0):
    newChart = makeChart(position)
    displayString = ''
    for i in xrange(5):
        for j in xrange(6):
            num = newChart[i][j]
            if j < 5:
                displayString += str(num)
                if num < 10:
                    displayString += ' '
                displayString += ' '
            else:
                displayString += str(num)
                displayString += "\n"
    print displayString

def displayModChart(position=0):
    newChart = makeChart(position)
    displayString = ''
    for i in xrange(5):
        for j in xrange(6):
            num = newChart[i][j]%12
            if j < 5:
                displayString += str(num)
                if num < 10:
                    displayString += ' '
                displayString += ' '
            else:
                displayString += str(num)
                displayString += "\n"
    print displayString

def displayNoteChart(position=0):
    newChart = makeChart(position)
    displayString = ''
    noteArray = ['E  ','F  ','F# ','G  ','G# ','A  ','Bb ','B  ','C  ','C# ','D  ','Eb ']
    for i in xrange(5):
        for j in xrange(6):
            num = newChart[i][j]%12
            note = noteArray[num]
            if j < 5:
                displayString += note
            else:
                displayString += note
                displayString += "\n"
    print displayString

def main():
    if len(sys.argv) >= 2:
        position = int(sys.argv[1])
        displayNoteChart(position)
    else:
        displayNoteChart()

if __name__ == "__main__":
    main()



