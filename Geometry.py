#!usr/bin/python

"""
Lines have attributes 'slope' and 'y-intercept' unless the Line is vertical -> see vertLine class.
  - Methods are: intersect(line) - which will return a point at the intersection of the self line and the line given as a parameter. I may overload the '+' parameter for the intersection method.
    also, goesThrough(point) -> boolean will return true when the self line goes through the point given as parameter.
  I may overload the __init__ method so that we can have:
   slope-intercept initialization __init__(slope, intercept) if type(s) and type(i) are both numbers type(num)==int or type(num)==float.
   point-slope form: __init__(point, slope) if (isinstance(point,Point)) && (type(slope)==int or type(slope)==float)
   point-point -> __init__(p1, p2) if (isinstance(p1,Point)&&isinstance(p2,Point))
else, return error


Circles have center(a point) and a radius(a number)
  __init__(point, number)
    center = point
    radius = number
  __init__(number1, number2, number3)
    center = Point(number1, number2)
    radius = number3
"""
import math
import Tkinter

class Point(object):
   """
    The Point class is defined by an x and a y coordinate.
    The coordinates may be positive or negative  -
    Integers or Floats.
    Points sort of form the basis of the Geometry module.
   """
    
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __str__(self):
      return "("+`self.x`+","+`self.y`+")"

   def __add__(self, other):
       if isinstance(other, Point):
           return Line(self, other)
       elif isinstance(other, Line) or isinstance(other, vertLine):
           return self.IsOnLine(other)
       elif isinstance(other, Circle):
           return self.IsOnCircle(other)
       else:
           self.x = self.x+other
           self.y = self.y+other

   def IsOnLine(self, line):
        if isinstance(line, vertLine):
            return self.x == line.x
        elif isinstance(line, Line):
            return self.y==line.slope*self.x+line.intercept
      
   def IsOnCircle(self, circle):
      return distance(self, circle.center)==circle.radius
   def draw(self, canvas, color="black"):
      canvas.create_oval((canvas.winfo_width()/2)+self.x-2, (canvas.winfo_height()/2)-self.y-2, (canvas.winfo_width()/2)+self.x+2, (canvas.winfo_height()/2)-self.y+2, fill=color)

class Line(object):
   """
   Line class refers to all lines except vertical lines.
   So each of these lines have the atributes of slope and intercept.
   Horizontal lines have a slope of zero.  
  
   Both slopes and intercepts can be positive or negative, integers or floats.
   When you print a Line object a string is returned:
   "y = <slope>x+<intercept>"
   for example:
       >>>  line = Line(3,6)
       >>>  print line
       y = 3x+6

  
   For vertical lines see: vertLine class.
   """
   def __init__(self,param1, param2):
       """
       Line instances may be initiated by several ways:
         'Slope-Intercept' which is initiated thusly:
             line = Line(integer or float, integer or float)
         'Point-Slope' which is initaied thusly:
             line = Line(point_object, integer or float)
         'Euclidianly' or 'Two Points determine a line':
             line = Line(point_object, point_object) 
       """
       if type(param1)==int or type(param1)==float:
           if type(param2)==int or type(param2)==float:
               self.slope = param1
               self.intercept = param2
           else:
               #throw an error
               print("ERROR")
       elif isinstance(param1,Point):
           if type(param2)==int or type(param2)==float:
                self.slope = param2
                a = param1.x
                b = param1.y
                self.intercept = b-(param2*a)
           elif isinstance(param2,Point):
                x1 = param1.x
                y1 = param1.y
                x2 = param2.x
                y2 = param2.y
                slope = (y2-y1)*1.0/(x2-x1)
                self.slope = slope
                self.intercept = y1-(slope*x1)
           else:
               pass

   def __str__(self):
      if self.slope!=0:
        if self.intercept>0:
          return "y="+`self.slope`+"x+"+`self.intercept`
        elif self.intercept==0:
          return "y="+`self.slope`+"x"
        else: 
          return "y="+`self.slope`+"x"+`self.intercept`
      else:
        return "y="+`self.intercept`

   def Intersect(self, other):
      if isinstance(other, vertLine):
          x = other.x
          y = self.slope*x+self.intercept

          return Point(x,y)

      elif isinstance(other,Line):
          
          x=(other.intercept-self.intercept)*(1.0)/(self.slope-other.slope)
          y=self.slope*x+self.intercept
          
          return Point(x,y)

      else:
          pass

   def draw(self, canvas):
      height = canvas.winfo_height()
      width = canvas.winfo_width()
      startX = 0
      startY = (height/2)-(self.slope*(-width/2)+self.intercept)
      endX = width
      endY = (height/2)-(self.slope*(width/2)+self.intercept)
      canvas.create_line(startX, startY, endX, endY)
              
class vertLine(Line):
    
    def __init__(self,x):
        self.x =  x
         
    def __str__(self):
        return "x="+`self.x`

    def Intersect(self, line):
        x = self.x
        y = line.slope*x+line.intercept
        return Point(x,y)

    def draw(self, canvas):
        height = canvas.winfo_height()
        width = canvas.winfo_width()
        startX = width/2 + self.x
        startY = 0
        endX = startX
        endY = height
        canvas.create_line(startX, startY, endX, endY)

  
class Circle(object):
  
   def __init__(self, center, radius):
       if isinstance(center,Point):
         self.center = center
         self.radius = radius
       else:
         print "ERROR!"

   def __str__(self):
       return "Center: ("+`self.center.x`+","+`self.center.y`+")\nRadius: "+`self.radius`

   def IntersectCircle(self, circle):
       d = distance(self.center, circle.center)
       x0 = self.center.x
       y0 = self.center.y
       x1 = circle.center.x
       y1 = circle.center.y
       r0 = self.radius
       r1 = circle.radius

       if d > r0 + r1:
           return "No interesection - too far apart"
       elif d < math.fabs(r0-r1):
           return "No intersection - one inside the other"
       else:
           pass

       a = ((r0*r0)-(r1*r1)+(d*d))/(2.0*d)
       dx = x1-x0
       dy = y1-y0
       
       p2x = x0+(dx*a/d)
       p2y = y0+(dy*a/d)

       h = math.sqrt((r0*r0)-(a*a))
       rx = -dy*(h/d)
       ry = dx*(h/d)

       i1 = Point(p2x+rx, p2y+ry)
       i2 = Point(p2x-rx, p2y-ry)

       return i1, i2


   def draw(self, canvas):
       width = canvas.winfo_width()
       height = canvas.winfo_height()
       canvas.create_oval((width/2)+self.center.x-self.radius, (height/2)-self.center.y-self.radius, (width/2)+self.center.x+self.radius, (height/2)-self.center.y+self.radius)

def perBiSector(point1,point2):
    x1 = point1.x
    y1 = point1.y
    x2 = point2.x
    y2 = point2.y

# let's use point slope form - deriving from the line through both points
# and the midpoint of the segment
    
    midpoint = Point((x1+x2)*0.5, (y1+y2)*0.5)

    if x1==x2:
       return Line(midpoint,0)

    lineThruPoints = Line(point1, point2)

    if lineThruPoints.slope == 0: # because we can't raise 0**(-1)
        return vertLine((x1+x2)*0.5)        

    slope = -1*(lineThruPoints.slope**-1) 
    return Line(midpoint,slope)

def distance(point1, point2):
    x1 = point1.x
    y1 = point1.y
    x2 = point2.x
    y2 = point2.y

    return math.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))

def threePointCircle(point1, point2, point3):
#    center = perBiSector(point1, point2).Intersect(perBiSector(point2, point3))
    center = Point(0,0)
    m = Point(0,0)

    if point1.x == point2.x == point3.x:
        return vertLine(point1.x)

    elif point1.x == point2.x and point3.x != point1.x:
        m = midPoint(point1, point2)
        center.y = m.y
        center.x = (m.y - perBiSector(point2, point3).intercept)/perBiSector(point2, point3).slope

    elif point3.IsOnLine(Line(point1, point2)):
        return Line(point1, point2)

    elif point1.x == point2.x and point2.y == point3.y:
      center = Point((point2.x+point3.x)/2,(point1.y+point2.y)/2)

    elif point1.x == point3.x and point3.y == point2.y:
      center = Point((point2.x+point3.x)/2,(point1.y+point3.y)/2)

    elif point2.x == point3.x and point1.y == point2.y:
      center = Point((point1.x+point2.x)/2, (point2.y+point3.y)/2)

    elif point2.x == point3.x and point1.y == point3.y:
      center = Point((point2.x+point3.x)/2, (point2.y+point3.y)/2)
    
    elif point1.y == point2.y and point3.y != point1.y:
        m = midPoint(point1, point2)
        center.x = m.x
        center.y = perBiSector(point2, point3).slope*m.x + perBiSector(point2, point3).intercept 
        
    elif point1.y == point2.y and point2.y == point3.y:
        return Line(A, 0)
    
    elif point1.y == point3.y and point2.y != point3.y:
        m = midPoint(point1, point3)
        center.x = m.x
        center.y = perBiSector(point2, point3).slope*m.x + perBiSector(point2, point3).intercept

    elif point2.y == point3.y and point1.y != point2.y:
        m = midPoint(point2, point3)
        center.x = m.x
        center.y = perBiSector(point1, point3).slope*m.x + perBiSector(point1, point3).intercept
 
    elif point1.x == point3.x and point2.x != point3.x:
        m = midPoint(point1, point3)
        center.y = m.y
        center.x = (m.y- perBiSector(point2, point3).intercept)/perBiSector(point2, point3).slope

 

    else:
      line1 = perBiSector(point1, point2)
      line2 = perBiSector(point2, point3)
      center = line1.Intersect(line2)
    
    radius = distance(center, point1)
    return Circle(center, radius)

def Origin():
   # this returns a point object at the origin
    return Point(0,0)

def papCircle(left,degreeAngle,right):
    m = midPoint(left, right)
    angle = math.radians(degreeAngle)
    base = distance(left,right)

    Cx = 0
    Cy = 0

    # 0 < angle <= pi/2 
    center2mid = math.fabs(base/(2*math.tan(angle)))


    if left.y == right.y and left.x > right.x:
        Cx = m.x
        Cy = m.y + center2mid

    elif left.y == right.y and left.x < right.x:
        Cx = m.x
        Cy = m.y - center2mid

    elif left.x == right.x and left.y < right.y:
        Cx = m.x + center2mid
        Cy = m.y

    elif left.x == right.x and left.y > right.y:
        Cx = m.x - center2mid
        Cy = m.y

    else:
        # make sure gamma angle is between 0 and 2*pi
        pi = math.pi
        gamma = 0
        if math.atan(Line(left,right).slope)< 0:
            gamma = math.pi + math.atan(Line(left, right).slope)
        else:
            gamma = math.atan(Line(left, right).slope)



        if left.y < right.y and left.x < right.x:
            Cx = m.x+math.cos(gamma-pi/2)*center2mid
            Cy = m.y+math.sin(gamma-pi/2)*center2mid

        elif left.y > right.y and left.x > right.x:
            Cx = m.x-math.cos(gamma-pi/2)*center2mid
            Cy = m.y-math.sin(gamma-pi/2)*center2mid
    
        elif left.y < right.y and left.x > right.x:
            Cx = m.x+math.cos(gamma-pi/2)*center2mid
            Cy = m.y+math.sin(gamma-pi/2)*center2mid

        # if left.y > right.y and left.x < right.x
        else:
            Cx = m.x-math.cos(gamma-pi/2)*center2mid
            Cy = m.y-math.sin(gamma-pi/2)*center2mid

    radius = base/(2*(math.sin(angle)))
    center = Point(Cx, Cy)
    return Circle(center, radius)   
  
def threeCircleLocation(C1, C2, C3):
    A, B = C1.IntersectCircle(C2)
    if A.IsOnCircle(C3):
        return A
    elif B.IsOnCircle(C3):
        return B
    else:
        return "There is no such location"
 

def midPoint(point1, point2):
   return Point((point1.x+point2.x)*0.5,(point1.y+point2.y)*0.5)
