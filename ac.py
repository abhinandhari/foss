
from PIL import Image
import os
os.chdir('/home/abhinand/fossgit/amfoss-freshers-test/assets')
oswald = Image.open('/home/abhinand/fossgit/amfoss-freshers-test/assets/oswald.png').convert('LA')
oswald.rotate(270).save('corrected.png')
oswald.save('newos.png')

