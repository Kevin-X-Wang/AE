import sys
import os
import shutil

def getFiles(directory):
	return [os.path.join(directory, f) for f in os.listdir(directory) 
            if os.path.isfile(os.path.join(directory, f)) and "mp4" not in f]

index = open("./index.html", "w")

html = ""

for i in range(0, 1197):
	name = str(i).zfill(6)
	folder = "./associated_frames_test/{}/".format(name)
	files = filter(lambda f: "img" in f, getFiles(folder))
	to_add = """
		<table border="1" style="table-layout: fixed;">
		  <h5>frame{}</h5></tr>
		""".format(name)
	to_add += """
	</tr>
	"""
	to_add += """
		<td halign="center" style="word-wrap: break-word;" valign="top"> 
		{}
		</td>
	""".format("frame{}".format(name))
	for f in files:
		if name not in f.split("/")[-1]:
			to_add += """		
			      	<td halign="center" style="word-wrap: break-word;" valign="top"> 
			          {}
			        </td>
			      """.format(f.split("/")[-1][:-8])
	to_add += """
		</tr>
	"""
	to_add += """
		<td halign="center" style="word-wrap: break-word;" valign="top"> 
			 <img src = {}>
		</td>
	""".format(folder + "frame{}_img.png".format(name))
	files = filter(lambda f: "img" in f, getFiles(folder))
	for f in files:
		if f != folder + "frame{}_img.png".format(name):
			to_add += """		
			      	<td halign="center" style="word-wrap: break-word;" valign="top"> 
			          <img src = {}>
			        </td>
			      """.format(f)
	to_add += """
		</tr>
		</table>
		<table border="1" style="table-layout: fixed;">  	
		</tr>
	"""

	to_add += "</tr></table>"
	html = html + to_add

final = """  
</body>
</html>
"""
html = html + final

index.write(html)
index.close()
