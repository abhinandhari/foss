
from PIL import Image
import os
os.chdir('/home/abhinand/fossgit/amfoss-freshers-test/assets')
oswald.rotate(270).save('corrected.png')
oswald = Image.open('/home/abhinand/fossgit/amfoss-freshers-test/assets/corrected.png').convert('LA')
oswald.save('newos.png')

