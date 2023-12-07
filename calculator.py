import pygame
pygame.init()
screen = pygame.display.set_mode((400, 600))
font = pygame.font.SysFont("arial", 50)
text_box = ""
running = True

calculator = [["","","","d"],
			  [1,2,3,"+"],
			  [4,5,6,"-"],
			  [7,8,9,"x"],
			  ["c",0,"=","/"]]

def get_num_oper(expression):
	number = ""
	numbers = []
	operators = []
	for i in range(len(expression)):
		if expression[i] == "+" or expression[i] == "-" or expression[i] == "x" or expression[i] == "/":
			operators.append(expression[i])
			numbers.append(float(number))
			number = ""
		elif i == len(expression)-1:
			number += expression[i]
			numbers.append(float(number))
		else:
			number += expression[i]
	return numbers, operators

def mul_div_plus_minus(mdpm):
	if mdpm == "x":
		number = numbers[operators.index(mdpm)] * numbers[operators.index(mdpm)+1]
	elif mdpm == "/":
		number = numbers[operators.index(mdpm)] / numbers[operators.index(mdpm)+1]
	elif mdpm == "+":
		number = numbers[operators.index(mdpm)] + numbers[operators.index(mdpm)+1]
	elif mdpm == "-":
		number = numbers[operators.index(mdpm)] - numbers[operators.index(mdpm)+1]

	numbers.remove(numbers[operators.index(mdpm)+1])
	numbers.remove(numbers[operators.index(mdpm)])
	numbers.insert(operators.index(mdpm), number)
	operators.remove(operators[operators.index(mdpm)])

def calculate(expression):
	global numbers, operators
	try:
		numbers, operators = get_num_oper(expression)
		while "x" in operators or "/" in operators:
			if "x" in operators and "/" in operators:
				if operators.index("x") < operators.index("/"):
					mul_div_plus_minus("x")
				elif operators.index("x") > operators.index("/"):
					mul_div_plus_minus("/")
			elif "x" in operators:
				mul_div_plus_minus("x")
			elif "/" in operators:
				mul_div_plus_minus("/")

		while "+" in operators or "-" in operators:
			if "+" in operators and "-" in operators:
				if operators.index("+") < operators.index("-"):
					mul_div_plus_minus("+")
				elif operators.index("+") > operators.index("-"):
					mul_div_plus_minus("-")
			elif "+" in operators:
				mul_div_plus_minus("+")
			elif "-" in operators:
				mul_div_plus_minus("-")

		return str(numbers[0])
	except:
		return "ERROR"

def draw_buttons(rows, columns):
	for i in range(rows):
		for j in range(columns):
			pygame.draw.rect(screen, (255, 255,255), (0 + i*100,100 + j*100,100-1,100-1))
			text = font.render(str(calculator[j][i]), True, (0,0,0))
			screen.blit(text, (0+i*100+50, 100+j*100))
			screen.blit(font.render(text_box, True, (255,255,255)), (0,0))

while running:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				for i in range(4):
					for j in range(5):
						if mouse_x > 0 + i*100 and mouse_x < 0 + i*100 + 100 and mouse_y > 100 + j*100 and mouse_y < 100 + j*100 + 100:
							if calculator[j][i] == "=":
								text_box = calculate(text_box)
								screen.fill((0,0,0))
							elif calculator[j][i] == "c":
								text_box = ""
								screen.fill((0,0,0))
							elif calculator[j][i] == "d":
								if text_box == "ERROR":
									text_box = ""
									screen.fill((0,0,0))
								text_box = text_box[:-1]
								screen.fill((0,0,0))
							else:
								if text_box == "ERROR":
									text_box = ""
									screen.fill((0,0,0))
								text_box += str(calculator[j][i])
	draw_buttons(4,5)
	pygame.display.flip()