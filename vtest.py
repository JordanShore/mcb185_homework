import mcb185
import json

mypwm = mcb185.make_pwm('acggcggtcatgg')
print(json.dumps(mypwm, indent=4))