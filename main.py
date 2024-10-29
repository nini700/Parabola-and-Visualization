import numpy as np #math operations ფესვის ამოღება
import matplotlib.pyplot as plt #ბიბლიოთეკა

class Parabola:  #კლასის ინიციალიზაცია
    def __init__(self, a, b, c):
        """Initialize parabola with coefficients of ax^2 + bx + c"""
        self.a = a
        self.b = b
        self.c = c
    
    def get_vertex(self): #ითვლის პარაბოლის წერტილს(x = -b/(2a))
        """Calculate the vertex of the parabola"""
        x = -self.b / (2 * self.a)
        y = self.evaluate(x)
        return (x, y)
    
    def evaluate(self, x): #ითვლის y მნიშვნელობას x-ისთვის (ax² + bx + c)

        """Evaluate the parabola at a given x value"""
        return self.a * x**2 + self.b * x + self.c
    
    def get_axis_of_symmetry(self): #სიმეტრიის ღერძის დაგენერირება
        """Get the x-coordinate of the axis of symmetry"""
        return -self.b / (2 * self.a)
    
    def get_roots(self):  #ფესვები
        """Calculate the roots of the parabola"""
        discriminant = self.b**2 - 4*self.a*self.c
        
        if discriminant < 0:
            return "No real roots" #დათვლის დისკრიმინანტს
        elif discriminant == 0:
            x = -self.b / (2*self.a)
            return (x, x)
        else:
            x1 = (-self.b + np.sqrt(discriminant)) / (2*self.a)
            x2 = (-self.b - np.sqrt(discriminant)) / (2*self.a)
            return (x1, x2)
    
    def get_direction(self):
        """Determine if parabola opens up or down"""
        return "Up" if self.a > 0 else "Down"  #a > 0 თუ < 0 (პარაბოლის მიმართულება)
    
    def plot(self, x_range=(-10, 10)):
        """Plot the parabola"""
        x = np.linspace(x_range[0], x_range[1], 1000)
        y = self.evaluate(x)
        
        plt.figure(figsize=(10, 8))
        plt.plot(x, y, 'b-', label=f'{self.a}x² + {self.b}x + {self.c}')
        
#Vertex - წვერო
        vertex = self.get_vertex()
        plt.plot(vertex[0], vertex[1], 'ro', label='Vertex')
        
#Axis of symmetry - სიმეტრიის ღერძი
        axis_x = self.get_axis_of_symmetry()
        plt.axvline(x=axis_x, color='g', linestyle='--', label='Axis of Symmetry')
        
#Roots - ფესვები
        roots = self.get_roots()
        if isinstance(roots, tuple):
            plt.plot([roots[0], roots[1]], [0, 0], 'ko', label='Roots')
        
        plt.grid(True)
        plt.legend()
        plt.title('Parabola Analysis')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        plt.show()

def analyze_parabola():
    """Function to interact with user and analyze parabola"""
    print("Enter the coefficients of the quadratic equation (ax² + bx + c)")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    
    parabola = Parabola(a, b, c)
    
    print("\nParabola Analysis:")
    print("-----------------")
    print(f"Equation: {a}x² + {b}x + {c}")
    print(f"Vertex: {parabola.get_vertex()}")
    print(f"Axis of Symmetry: x = {parabola.get_axis_of_symmetry()}")
    print(f"Roots: {parabola.get_roots()}")
    print(f"Opens: {parabola.get_direction()}")
    
    parabola.plot()

if __name__ == "__main__":
    analyze_parabola()