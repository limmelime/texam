#4c 69 6d 6d 65 6c 69 6d 65
from pynput.keyboard import Controller as keyController
from pynput.keyboard import Key
import time, os, json

keyboard = keyController()

def ascii_art():
	print("\n\n\n\n")
	print(" _________  _______      ___    ___ ________  _____ ______      ")
	print("|\___   ___\\  ___ \    |\  \  /  /|\   __  \|\   _ \  _   \    ")
	print("\|___ \  \_\ \   __/|   \ \  \/  / | \  \|\  \ \  \\\__\ \  \   ")
	print("     \ \  \ \ \  \_|/__  \ \    / / \ \   __  \ \  \\|__| \  \  ")
	print("      \ \  \ \ \  \_|\ \  /     \/   \ \  \ \  \ \  \   \ \  \ ")
	print("       \ \__\ \ \_______\/  /\   \    \ \__\ \__\ \__\   \ \__\\")
	print("        \|__|  \|_______/__/ /\ __\    \|__|\|__|\|__|    \|__|")
	print("                        |__|/ \|__|                             \n\n")
	print("      By Limmelime\n\n")

def main():

	ascii_art()

	def options():
		try:
			print("Open text document and enter the text   0")
			print("Change delay before pasting             1")
			print("Read text document and initiate TEXAM   2")
			print("Close and exit TEXAM                    3")
			print("License and user agreement              4")
			
			inp = input("\nOption > ")
			
			if inp.lower() == "0":
				os.startfile("text.texam")
				print()
				options()
			elif inp.lower() == "1":
				delayy = input("\nEnter preferred delay: ")
				try:
					int(delayy)
				except:
					print("\nThat is not an integer\n")
					options()
				
				with open("txm.texam", 'w') as w:
					w.write("10\n" + delayy)
					w.close()
				
				print()
				options()
			elif inp.lower() == "2":
				pass
			elif inp.lower() == "3":
				print()
				exit(-3)
			elif inp.lower() == "4":
				print("\nThis program is licensed under the GNU GPL License\nYou can find the full license here: https://www.gnu.org/licenses/gpl-3.0.en.html")
				print("TEXAM is only to be used for educational purposes. You cannot use it as a way to bypass systems preventing you from using copy + paste and so on if you are not allowed to.")
				print("The creator of TEXAM will not take any responsibility for misuse of the product. The user takes responsibility for all actions using this program.")
				print("By continuing, you accept the terms and acknowledge that you will take responsibility for all actions.")
				input("\nPress enter to agree and continue\n")
				options()
			else:
				print("\nNot a valid option\n")
				options()
		except Exception as e:
			print("Error during option function: " + e)
		
	options()
		
	try:
		with open("text.texam", "r") as f:
			text = f.read()
			
			try:
				with open("txm.texam") as r:
					delay = r.readlines()[1]
					if int(delay) < 0:
						raise ValueError
					else:
						time.sleep(int(delay))
					
				
					
			except ValueError:
				with open("txm.texam") as r:
					delay = r.readlines()[0]
					time.sleep(int(delay))
				
			except:
				raise RuntimeError
			
			def split(word):
				return list(word)
			
			chars = split(text)
			
			print("┌────START────=\n│\n│")
			
			for i in range(len(chars)):
			
				char = chars[i]
				
				if char == " ":
					print("│")
				elif char == "\n":
					print("│")
				else:
					print("├────" + char + "\n│")
				
				keyboard.press(char)
				keyboard.release(char)
				
			print("│\n└────END─────=\n\n\n\n")
			main()
				
	except Exception as e:
		print(e)
		print("There has been an error: ", e)
		time.sleep(2)
		options()
	

if __name__ == "__main__":
	main()
#4c 69 6d 6d 65 6c 69 6d 65
