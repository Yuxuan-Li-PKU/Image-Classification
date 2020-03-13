correct = 0.115
end = 0.115

for i in range(9):
	
	correct = correct - 0.01

	end = correct + (1-correct)*(end)

print(end)