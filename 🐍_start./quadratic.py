import math
#8x2 + 16x + 8 = 0
print("Quadratic Equation:");
a=float(input("Enter a:"));
b=float(input("Enter b:"));
c=float(input("Enter c:"));
delta = ((b*b) - (4*c));
if (delta < 0): #if complex roots
	print("complex roots!\n"); 
else: #if roots are not complex
	t = math.sqrt(delta);
	r1 = (-b - t) / (2*a);
	r2 = (-b + t) / (2*a);
	print(f"The first root: {round(r1,3)}");
	print(f"The second root: {round(r2,3)}");