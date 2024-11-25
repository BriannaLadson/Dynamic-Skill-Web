from tkinter import *
import math
import random

class Root(Tk):
	def __init__(self):
		super().__init__()
		self.title("Skill Web")
		self.state("zoomed")
		
		self.skill_web = SkillWeb(self)
		self.skill_web.pack(fill=BOTH, expand=1)
		self.skill_web.draw()
		
		
class SkillWeb(Canvas):
	def __init__(self, parent):
		super().__init__(parent, bg="#FED6D3")
		
		#Must Have at Least 3 Skills!
		self.skills = {
			"Python": random.randint(0, 100),
			"Javascript": random.randint(0, 100),
			"Java": random.randint(0, 100),
			#"C++": random.randint(0, 100),
			#"C#": random.randint(0, 100),
			#"Ruby": random.randint(0, 100),
			#"PHP": random.randint(0, 100),
			#"Swift": random.randint(0, 100),
			#"Go": random.randint(0, 100),
			#"Rust": random.randint(0, 100),
		}
		
		#N-gon (# of vertices/edges/skills)
		self.n_gon = len(self.skills)
		
		#Angle Between Vertices
		self.angle_radians = 2 * math.pi / self.n_gon
		
		#Rotates N-gon
		self.offset = (math.pi / 2) * -1
		
		#Number of Sub-Ngons
		self.layers = 5
		
		self.outer_radius = 200
		self.inner_radius = 50
		
	def draw(self):
		#Update Canvas
		self.update()
		
		#Set Imaginary Circle Center
		self.center_x = self.winfo_width() / 2
		self.center_y = self.winfo_height() / 2
		
		self.draw_ngons()
		
	def draw_ngons(self):
		decrement = (self.outer_radius - self.inner_radius) / (self.layers - 1)
		
		skill_names = list(self.skills.keys())
		skill_levels = list(self.skills.values())
		
		for layer in range(self.layers):
			cur_radius = self.outer_radius - layer * decrement
			
			#Calc Vertices
			vertices = []
			
			for i in range(self.n_gon):
				angle = self.offset + i * self.angle_radians
				
				x = self.center_x + cur_radius * math.cos(angle)
				y = self.center_y + cur_radius * math.sin(angle)
				
				vertices.append([x, y])
				
			#Draw Line Between Vertices Per Layer
			self.create_polygon(vertices, fill="", outline="black", width=3)
				
			#Draw Diagonal Lines
			if layer == 0:
				for k in range(self.n_gon):
					x, y = vertices[k]
					
					self.create_line(x, y, self.center_x, self.center_y, width=3)
		
					lbl_r = self.outer_radius + 30
					
					lbl_x = self.center_x + lbl_r *math.cos(self.offset + k * self.angle_radians)
					lbl_y = self.center_y + lbl_r * math.sin(self.offset + k * self.angle_radians)
					
					self.create_text(lbl_x, lbl_y, text=skill_names[k])
					
		#Calc Skill Level Vertices
		skill_vertices = []
		
		for l, level in enumerate(skill_levels):
			max_lvl = min(level, 100)
			
			if level == 0:
				r = 0
				
			else:
				normalized_lvl = (max_lvl - 1) / (100 - 1)
				
				r = self.inner_radius + normalized_lvl * (self.outer_radius - self.inner_radius)
				
			angle = self.offset + l * self.angle_radians
			x = self.center_x + r * math.cos(angle)
			y = self.center_y + r * math.sin(angle)
			skill_vertices.append([x, y])
			
		#Fill Shape Formed by Skill Vertices
		coordinates = [coords for vertex in skill_vertices for coords in vertex]
		
		self.create_polygon(coordinates, fill="#9D8A88")
			
		#Draw Lines Between Skill Vertices
		for i in range(len(skill_vertices)):
			x, y = skill_vertices[i]
			x1, y1 = skill_vertices[(i + 1) % len(skill_vertices)]
			self.create_polygon(skill_vertices, fill="", outline="black", width=2)
			
		#Draw Skill Vertices
		for x, y in skill_vertices:
			self.create_oval(x - 10, y - 10, x + 10, y + 10, fill="#9D8A88", outline="black", width=2)
			
		
		
if __name__ == "__main__":
	root = Root()
	root.mainloop()