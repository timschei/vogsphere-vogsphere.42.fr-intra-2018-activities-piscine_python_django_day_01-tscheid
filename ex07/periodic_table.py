#!/usr/local/bin/python3

def tri (ligne, sortie, compteur):
	nom = ligne.split('=')
	case = nom[1].split(',')
	d = dict()
	for i in range(len(case)):
		donnee = case[i].split(':')
		d[donnee[0].strip()] = donnee[1].strip("\n")
	if compteur + 1 < int(d['position']):
		for x in range(int(d['position'])-compteur-1):
			sortie.write("""
					<td></td>""")
	sortie.write("""
					<td style="border: 1px solid black; padding:10px">
						<h4>"""+nom[0]+"""</h4>
						<ul>
							<li>No """+d['number']+"""</li>
							<li>"""+d['small']+"""</li>
							<li>"""+d['molar']+"""</li>
							<li>"""+d['electron']+""" electron</li>
						</ul>
					</td>""")
	if int(d['position']) > 16 and int(d['number']) < 118:
		sortie.write("""
			</tr>
			<tr>""")
	return int(d['position'])

if __name__ == '__main__':
	compteur = 0
	with open("periodic_table.html", 'w') as sortie0:
		sortie0.write("")
	with open("periodic_table.html", 'a') as sortie1:
		sortie1.write("""<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Periodic table</title>
		<style>
		table {
			border-collapse: collapse;
		}
		ul {
			list-style: none;
		}
		</style>
	</head>
	<body>
		<table>
			<tr>""")
		with  open ("periodic_table.txt", 'r') as f:
			for ligne in f :
				compteur = tri (ligne, sortie1, compteur)
		sortie1.write("""	
			</tr>
		</table>
	</body>
</html>
""")