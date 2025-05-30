""" Desiree Cele created this program that generates a vibrant geometric pattern on a 600x600 pixel canvas. 
The geometric design features a 6x6 grid of alternating rectangles and ovals, each filled with a different color from 
the rainbow spectrum. Within every larger shape sits a smaller white shape of the opposite type, creating an eye-catching contrast. 
This simple yet visually appealing pattern demonstrates the use of basic shapes and color sequencing in graphical programming. 
"""

from graphics import Canvas

def main():
    # Create a canvas
    canvas = Canvas(600, 600)

    # Colors
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # Create a grid pattern
    size = 100
    for row in range(6):
        for col in range(6):
            left = col * size
            top = row * size
            right = left + size
            bottom = top + size
            
            # Alternate between rectangles and ovals
            if (row + col) % 2 == 0:
                canvas.create_rectangle(
                    left, top, right, bottom,
                    colors[(row + col) % len(colors)]
                )
            else:
                canvas.create_oval(
                    left, top, right, bottom,
                colors[(row + col) % len(colors)]
                )
                
            # Add a smaller shape inside each main shape
            inset = 20
            if (row + col) % 2 == 0:
                canvas.create_oval(
                    left + inset, top + inset, right - inset, bottom - inset,
                    'white'
                )
            else:
                canvas.create_rectangle(
                    left + inset, top + inset, right - inset, bottom - inset,
                    'white'
                )

# Call the main function
if __name__ == '__main__':
    main()