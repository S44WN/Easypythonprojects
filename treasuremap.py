
r1 = ['🌫️', '🌫️', '🌫️', '🌫️', '🌫️']
r2 = ['🌫️', '🌫️', '🌫️', '🌫️', '🌫️']
r3 = ['🌫️', '🌫️', '🌫️', '🌫️', '🌫️']
r4 = ['🌫️', '🌫️', '🌫️', '🌫️', '🌫️']
r5 = ['🌫️', '🌫️', '🌫️', '🌫️', '🌫️']

map = [r1, r2, r3, r4, r5]

print(f"{r1}\n{r2}\n{r3}\n{r4}\n{r5}")

position = input('where do u want to put the treasure (give xy)? : ')

horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = '📍'

print(f"{r1}\n{r2}\n{r3}\n{r4}\n{r5}")
