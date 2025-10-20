# How many triangles 
num_triangles = int(input("How many triangles? "))
# Total area to 0 to accumulate the areas.
total_area = 0.0
# Loop for each triangle.
for i in range(1, num_triangles + 1):
    # Print a header for the current triangle 
    print(f"\nTriangle {i}:")
    # The base and height 
    # float() for decimal inputs
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    # Calculate the area for the current triangle.
    area = 0.5 * base * height
    # Print the result for the current triangle.
    print(f"Area: {area}")
    # Add the current triangle's area to the total.
    total_area += area
# After all triangles are processed it print the grand total.
print(f"\nTotal area of all triangles: {total_area}")